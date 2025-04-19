## 🔍 Network Analyzer

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## 📋 Descripción
**Network Analyzer** es una aplicación web que democratiza el análisis de seguridad en red. Combina captura avanzada de paquetes con inteligencia artificial para permitir que usuarios sin experiencia técnica profunda puedan monitorizar la seguridad de su red mediante consultas en lenguaje natural.

### 🎯 Objetivos
- Capturar y analizar tráfico de red en tiempo real (capas de Red y Transporte)
- Procesar datos para alimentar modelos de IA
- Permitir consultas en lenguaje natural sobre eventos de seguridad
- Visualizar información de manera clara e intuitiva
- Detectar anomalías y posibles amenazas de seguridad

## 🏗️ Arquitectura del Proyecto

```
📦 TFM
 ┣ 📂 src
 ┃ ┣ 📂 packet_capture    # Captura de paquetes con Wireshark/TShark
 ┃ ┣ 📂 data_processing   # Análisis y transformación de datos
 ┃ ┣ 📂 ai_engine         # Motor IA para consultas en lenguaje natural
 ┃ ┗ 📂 web_interface     # Interfaz web y API REST
 ┣ 📂 docs                # Documentación
 ┣ 📂 tests               # Pruebas unitarias y de integración
 ┣ 📂 config              # Configuración del sistema
 ┣ 📄 requirements.txt    # Dependencias Python
 ┗ 📄 README.md           # Este documento
```

## 💻 Tecnologías

- **Backend**: Python, FastAPI
- **Frontend**: React/Next.js, Tailwind CSS
- **Captura de paquetes**: TShark/Wireshark, Pyshark, Scapy
- **Análisis de datos**: Pandas, NumPy, scikit-learn
- **Inteligencia Artificial**: LangChain, Claude API
- **Base de datos**: PostgreSQL, ChromaDB (vectorial)

## ✅ Requisitos

- Python 3.10+
- TShark/Wireshark (instalado y en PATH)
- Docker (recomendado para despliegue)
- Acceso a API de Claude (para funciones de IA)

## 🚀 Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/Joncarre/TFM.git
   cd TFM
   ```

2. **Configurar entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   ```bash
   cp .env.example .env
   # Editar .env con las credenciales necesarias
   ```

5. **Verificar instalación**
   ```bash
   python -m src.packet_capture.test_capture
   ```

## 🔧 Uso

### Captura de paquetes
```python
from src.packet_capture.capture_manager import CaptureManager

# Iniciar captura en interfaz predeterminada
manager = CaptureManager()
manager.start_capture()

# Detener después de 60 segundos
import time
time.sleep(60)
manager.stop_capture()

# Guardar captura
manager.save_capture("mi_captura.pcap")
```

### Consultas en lenguaje natural
```python
from src.ai_engine.query_processor import QueryProcessor

processor = QueryProcessor()
result = processor.process_query("¿Ha habido algún intento de ataque de fuerza bruta?")
print(result)
```


## Comandos
listar las capturas pcap
python tests/test_capture.py --list-captures

listar las interfaces
python tests/test_capture.py --list-interfaces

capturar paquetes
python tests/test_capture.py --capture --interface "nombre_de_tu_interfaz" --duration 100

generar la base de datos
python tests/test_capture.py --open captures/nombre_de_tu_captura.pcap

ver datos en detalle
python tests/query_test.py --db databases/database_20250418_141938.db 

generar json con información
python tests\test_analyzer.py --db_path databases\nombre_de_tu_bbdd.db --analyze_all --output analysis_results\

visualizar información
python tests/visualize_analysis.py analysis_results/nombre_de_tu_json.json

ver datos en lenguaje natural
python tests/test_integrated.py databases/database_20250418_141938.db --interactive 
python tests/test_integrated.py databases/database_20250418_141938.db "Dame un resumen del tráfico de red"

## 📊 Casos de uso

- **Monitoreo de seguridad para pequeñas empresas**: Permite a administradores IT con conocimientos limitados detectar amenazas.
- **Análisis forense**: Examinar capturas de tráfico histórico para investigar incidentes.
- **Educación**: Herramienta didáctica para aprender sobre protocolos y seguridad de red.


## 📝 Licencia

Distribuido bajo la Licencia MIT. Ver `LICENSE` para más información.
