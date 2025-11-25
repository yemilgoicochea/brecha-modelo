# Directorio de Pre-procesamiento de Datos

## Estructura

```
predata/
├── input/
│   └── proyecto_brecha.xlsx    ← COLOCA AQUÍ tu archivo Excel
├── output/
│   ├── brechas.csv             ← Generado automáticamente
│   └── proyectos.csv           ← Generado automáticamente
└── README.md
```

## Instrucciones de Uso

### 1. Preparar el archivo Excel

Coloca tu archivo Excel `proyecto_brecha.xlsx` en la carpeta `input/`.

El archivo debe contener al menos 2 columnas:
- Una columna con el **título del proyecto**
- Una columna con el **nombre de la brecha**
- (Opcional) Una columna con la **descripción del proyecto**

### 2. Ejecutar el script de procesamiento

Desde la carpeta raíz del proyecto (`project/`), ejecuta:

```powershell
python predata\procesar_excel.py
```

El script te pedirá:
1. Nombre de la columna con el título del proyecto → **Responde: `project` o `1`**
2. Nombre de la columna con el nombre de la brecha → **Responde: `brecha` o `2`**
3. (Opcional) Nombre de la columna con la descripción → **Presiona Enter (no hay descripción)**

Puedes responder con el nombre exacto de la columna o con su número (1, 2, 3, etc.).

### 3. Resultado

El script generará dos archivos en `predata/output/`:

- **brechas.csv**: Lista única de brechas con IDs asignados
  ```csv
  id,brecha
  1,"PORCENTAJE DE UNIDADES PRODUCTORAS..."
  2,"PORCENTAJE DE PERSONAS NO MATRICULADAS..."
  ```

- **proyectos.csv**: Lista de proyectos con sus brechas asignadas
  ```csv
  project_id,title,description,brecha_ids
  1,"AMPLIACION DE 01 AULA...","Descripción...","4"
  2,"CREACION DE INSTITUCION...","Descripción...","5"
  ```

### 4. Copiar a la carpeta de datos

Una vez generados los archivos, cópialos a la carpeta `data/`:

```powershell
Copy-Item predata\output\brechas.csv data\brechas.csv
Copy-Item predata\output\proyectos.csv data\proyectos.csv
```

## Notas

- El script automáticamente limpia filas con valores nulos
- Las brechas se ordenan alfabéticamente
- Los IDs se asignan secuencialmente (1, 2, 3, ...)
- Si no hay columna de descripción, se usa el título como descripción
