# src/query_engine/language_model.py
import os
import json
import requests
import logging
from typing import Dict, Any, List, Optional, Union
import anthropic

class LLMClient:
    """
    Cliente para interactuar con modelos de lenguaje (Claude)
    """
    
    def __init__(self, api_key=None, model="claude-3-opus-20240229"):
        """
        Inicializa el cliente de modelo de lenguaje.
        
        Args:
            api_key (str, optional): API key para Claude. Si es None, se usa la variable de entorno ANTHROPIC_API_KEY
            model (str): Modelo de Claude a utilizar
        """
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("Se requiere una API key para Claude. Establece la variable de entorno ANTHROPIC_API_KEY o pásala como parámetro.")
        
        self.model = model
        self.logger = logging.getLogger("LLMClient")
        self.client = anthropic.Anthropic(api_key=self.api_key)
    
    def process_query(self, query: str, context: Dict[str, Any], system_prompt: str = None) -> str:
        """
        Procesa una consulta en lenguaje natural usando Claude.
        
        Args:
            query (str): Consulta del usuario en lenguaje natural
            context (Dict): Contexto relevante para la consulta (estadísticas, datos, etc.)
            system_prompt (str, optional): Prompt del sistema para orientar a Claude
            
        Returns:
            str: Respuesta generada por Claude
        """
        try:
            # Preparar el sistema de prompt por defecto si no se proporciona uno
            if system_prompt is None:
                system_prompt = self._build_default_system_prompt()
            
            # Preparar el mensaje con contexto
            query_with_context = self._prepare_query_with_context(query, context)
            
            # Llamar a la API de Claude
            response = self.client.messages.create(
                model=self.model,
                system=system_prompt,
                messages=[{"role": "user", "content": query_with_context}],
                max_tokens=2000
            )
            
            # Extraer y devolver la respuesta
            return response.content[0].text
            
        except Exception as e:
            self.logger.error(f"Error al procesar consulta con Claude: {e}")
            return f"Error al procesar la consulta: {str(e)}"
    
    def _build_default_system_prompt(self) -> str:
        """
        Construye el prompt de sistema por defecto para Claude.
        """
        return """
        Eres un asistente especializado en ciberseguridad y análisis de tráfico de red.
        Tu tarea es analizar datos de tráfico de red e identificar posibles amenazas o problemas de seguridad.
        
        Debes proporcionar respuestas precisas, técnicas y útiles basadas en los datos disponibles.
        
        - Cuando proporciones respuestas numéricas, incluye estadísticas y métricas relevantes.
        - Cuando identifiques amenazas, clasifícalas por severidad y proporciona recomendaciones.
        - Organiza la información de forma clara y estructurada.
        - Si los datos son insuficientes para responder con certeza, indica qué información adicional sería necesaria.
        - Evita usar jerga excesivamente técnica. Explica los conceptos en términos claros y comprensibles.
        - Tu objetivo es ayudar a usuarios sin experiencia avanzada en ciberseguridad a entender su tráfico de red.
        """
    
    def _prepare_query_with_context(self, query: str, context: Dict[str, Any]) -> str:
        """
        Prepara la consulta incorporando el contexto relevante en un formato estructurado.
        
        Args:
            query (str): Consulta original del usuario
            context (Dict): Datos de contexto
            
        Returns:
            str: Consulta enriquecida con contexto
        """
        # Convertir el contexto a formato de texto estructurado
        context_str = json.dumps(context, indent=2)
        
        # Preparar el mensaje completo
        full_query = f"""
        Consulta del usuario: {query}
        
        Contexto disponible:
        ```json
        {context_str}
        ```
        
        Basándote en la consulta y el contexto proporcionado, genera una respuesta detallada.
        """
        
        return full_query