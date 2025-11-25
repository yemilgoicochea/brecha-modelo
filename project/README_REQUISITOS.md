# Pipeline Híbrido - Guía de Requisitos

## 📋 Requisitos Locales (Desarrollo)

### 1. Software Base
```bash
- Python 3.9, 3.10 o 3.11
- pip (gestor de paquetes)
- Git (control de versiones)
- VS Code con extensión Jupyter
```

### 2. Instalación de Dependencias
```bash
# Desde la carpeta del proyecto:
pip install -r requirements.txt
```

### 3. Estructura de Archivos Necesaria
```
project/
├── data/
│   ├── brechas.csv          # Archivo con catálogo de brechas
│   │   └── Columnas: id, brecha
│   └── proyectos.csv        # Dataset de entrenamiento
│       └── Columnas: project_id, title, description, brecha_ids
├── models/                  # Se crea automáticamente
├── outputs/                 # Se crea automáticamente
├── notebooks/
│   └── hybrid_pipeline.ipynb
└── requirements.txt
```

### 4. Hardware Recomendado
- **RAM**: 8GB mínimo, 16GB recomendado
- **CPU**: 4+ cores
- **GPU** (opcional): NVIDIA con 6GB+ VRAM
- **Disco**: 10GB libres

### 5. Archivos CSV Requeridos

#### `data/brechas.csv`:
```csv
id,brecha
1,Acceso a servicios de salud
2,Infraestructura educativa
3,Saneamiento básico
...
```

#### `data/proyectos.csv`:
```csv
project_id,title,description,brecha_ids
1,Hospital Regional,"Construcción de hospital...",1
2,Escuela Primaria,"Ampliación de aulas...",2
3,Agua Potable,"Sistema de agua...",3
...
```

---

## ☁️ Despliegue en Google Cloud Platform

### Entorno de Ejecución
- **Servicio**: Vertex AI Workbench / AI Platform Notebooks
- **Imagen**: PyTorch preconfigurada con CUDA
- **GPU**: Tesla T4 o V100
- **Storage**: Google Cloud Storage para datos y modelos

### No Necesitas Instalar Localmente
Los siguientes componentes ya están en GCP:
- ✅ PyTorch con CUDA
- ✅ Transformers
- ✅ CUDA Toolkit
- ✅ cuDNN
- ✅ Google Cloud libraries

### Flujo de Trabajo
1. **Desarrollo local**: Prueba la lógica con un subset pequeño de datos
2. **Subir a GCS**: Datos completos a Google Cloud Storage
3. **Notebook en Vertex AI**: Ejecutar entrenamiento completo
4. **Deploy modelo**: Vertex AI Endpoints para inferencia

---

## 🚀 Pasos para Empezar (Local)

1. **Instalar Python 3.10+**
2. **Clonar/crear el proyecto**
3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Preparar tus archivos CSV** en la carpeta `data/`
5. **Ejecutar el notebook** celda por celda

---

## ⚠️ Nota Importante

- **Para desarrollo local**: Solo necesitas los paquetes de `requirements.txt`
- **Para Google Cloud**: El entorno ya está configurado, solo sube tu código y datos
- **GPU local**: Opcional, solo acelera el proceso (no es obligatorio)
