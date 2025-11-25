# Brecha Modelo

Este repositorio contiene código y datos base para el modelado y análisis de brechas y proyectos.

## Objetivo
Centralizar el pipeline de procesamiento (limpieza de datos, embeddings, indexación y modelos de texto) manteniendo solo los archivos necesarios para reproducir resultados y evitando versionar artefactos pesados.

## Estructura principal
```
project/
  requirements.txt        Dependencias principales (instalación vía pip)
  data/                   CSV base (fuente limpia y pequeña)
    brechas.csv
    proyectos.csv
  notebooks/              Notebooks exploratorios (pueden mantenerse ligeros)
  predata/                Scripts para procesar insumos (solo código y README)
  outputs/                Salidas derivadas ligeras (se versiona CSV enriquecido)
    brechas_with_idx.csv
  models/                 (IGNORADO) Pesos de modelos y checkpoints
```

## Política de versionado
- Se incluyen: código `.py`, notebooks `.ipynb` relevantes, archivos `.csv` base y enriquecidos pequeños, definiciones de dependencias, documentación.
- Se excluyen: pesos de modelos (`.pt`, `.pth`, `.safetensors`), embeddings (`.npy`), índices FAISS (`.faiss`), tensores y artefactos regenerables, directorios de salida masivos y resultados intermedios.
- Justificación: Reducir el tamaño del repositorio, facilitar clonación y evitar conflictos en binarios que no diffsan bien.

## Regeneración de artefactos
1. Instalar dependencias:
```bash
pip install -r project/requirements.txt
```
2. Procesar datos iniciales (si se requiere regenerar CSV):
```bash
python project/predata/procesar_excel.py
```
3. Generar embeddings e índice (scripts no incluidos aún, se asumirían como `scripts/generar_embeddings.py` y `scripts/construir_indice.py`).

## Extensiones futuras
- Integrar DVC o Git LFS para pesos grandes.
- Añadir scripts de pipeline reproducible (`make` o `invoke`).

## Contacto
Para ajustes de política de datos o inclusión de nuevos artefactos usar Pull Request describiendo tamaño y necesidad.
