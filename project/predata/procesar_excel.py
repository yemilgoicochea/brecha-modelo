"""
Script para procesar archivo Excel de proyectos y brechas.

Entrada:
    predata/input/proyecto_brecha.xlsx
    Columnas esperadas:
    - Columna con título del proyecto
    - Columna con nombre de la brecha

Salida:
    predata/output/brechas.csv (id, brecha)
    predata/output/proyectos.csv (project_id, title, description, brecha_ids)
"""

import pandas as pd
from pathlib import Path
import sys

def procesar_excel():
    """
    Procesa el archivo Excel de proyectos y brechas.
    Genera dos archivos CSV en el formato requerido.
    """
    # ====================================================================
    # CONFIGURACIÓN DE RUTAS
    # ====================================================================
    
    # Obtener directorio raíz del proyecto (asumiendo que el script está en project/predata/)
    PROJECT_ROOT = Path(__file__).parent.parent
    
    # Rutas de entrada y salida
    input_file = PROJECT_ROOT / "predata" / "input" / "proyecto_brecha.xlsx"
    output_dir = PROJECT_ROOT / "predata" / "output"
    
    # Crear directorio de salida si no existe
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # ====================================================================
    # VERIFICAR QUE EXISTE EL ARCHIVO DE ENTRADA
    # ====================================================================
    
    if not input_file.exists():
        print(f"❌ ERROR: No se encontró el archivo {input_file}")
        print(f"   Asegúrate de que el archivo existe en la ruta correcta.")
        sys.exit(1)
    
    print(f"📂 Leyendo archivo: {input_file}")
    
    # ====================================================================
    # LEER ARCHIVO EXCEL
    # ====================================================================
    
    try:
        # Leer el Excel (detecta automáticamente la primera hoja)
        df = pd.read_excel(input_file)
        print(f"✅ Archivo cargado: {len(df)} filas encontradas")
        
        # Mostrar columnas disponibles
        print(f"\n📋 Columnas encontradas en el Excel:")
        for i, col in enumerate(df.columns, 1):
            print(f"   {i}. {col}")
        
    except Exception as e:
        print(f"❌ ERROR al leer el archivo Excel: {e}")
        sys.exit(1)
    
    # ====================================================================
    # SOLICITAR NOMBRES DE COLUMNAS AL USUARIO
    # ====================================================================
    
    print("\n" + "="*80)
    print("CONFIGURACIÓN DE COLUMNAS")
    print("="*80)
    
    # Solicitar nombre de la columna de título del proyecto
    print("\n¿Cuál es el nombre de la columna con el TÍTULO DEL PROYECTO?")
    titulo_col = input("Escribe el nombre exacto (o número): ").strip()
    
    # Si el usuario ingresó un número, convertir a nombre de columna
    if titulo_col.isdigit():
        titulo_col = df.columns[int(titulo_col) - 1]
    
    # Verificar que la columna existe
    if titulo_col not in df.columns:
        print(f"❌ ERROR: La columna '{titulo_col}' no existe en el Excel")
        sys.exit(1)
    
    # Solicitar nombre de la columna de brecha
    print("\n¿Cuál es el nombre de la columna con el NOMBRE DE LA BRECHA?")
    brecha_col = input("Escribe el nombre exacto (o número): ").strip()
    
    # Si el usuario ingresó un número, convertir a nombre de columna
    if brecha_col.isdigit():
        brecha_col = df.columns[int(brecha_col) - 1]
    
    # Verificar que la columna existe
    if brecha_col not in df.columns:
        print(f"❌ ERROR: La columna '{brecha_col}' no existe en el Excel")
        sys.exit(1)
    
    # Verificar si hay columna de descripción (opcional)
    print("\n¿Hay una columna con DESCRIPCIÓN del proyecto? (opcional)")
    print("Si no hay, presiona Enter para omitir")
    descripcion_col = input("Escribe el nombre exacto (o número, o Enter para omitir): ").strip()
    
    if descripcion_col:
        if descripcion_col.isdigit():
            descripcion_col = df.columns[int(descripcion_col) - 1]
        
        if descripcion_col not in df.columns:
            print(f"⚠️ ADVERTENCIA: La columna '{descripcion_col}' no existe. Se usará el título como descripción.")
            descripcion_col = None
    else:
        descripcion_col = None
    
    # ====================================================================
    # PROCESAR DATOS
    # ====================================================================
    
    print("\n" + "="*80)
    print("PROCESANDO DATOS...")
    print("="*80)
    
    # Limpiar datos: eliminar filas con valores nulos en columnas críticas
    df_clean = df.dropna(subset=[titulo_col, brecha_col]).copy()
    print(f"✅ Filas después de limpiar valores nulos: {len(df_clean)}")
    
    # ====================================================================
    # GENERAR brechas.csv
    # ====================================================================
    
    # Obtener lista única de brechas
    brechas_unicas = df_clean[brecha_col].unique()
    
    # Crear DataFrame de brechas con IDs
    brechas_df = pd.DataFrame({
        'id': range(1, len(brechas_unicas) + 1),
        'brecha': brechas_unicas
    })
    
    # Ordenar alfabéticamente por nombre de brecha (opcional)
    brechas_df = brechas_df.sort_values('brecha').reset_index(drop=True)
    brechas_df['id'] = range(1, len(brechas_df) + 1)
    
    # Guardar brechas.csv
    brechas_output = output_dir / "brechas.csv"
    brechas_df.to_csv(brechas_output, index=False, encoding='utf-8-sig')
    print(f"\n✅ Generado: {brechas_output}")
    print(f"   Total de brechas únicas: {len(brechas_df)}")
    
    # ====================================================================
    # GENERAR proyectos.csv
    # ====================================================================
    
    # Crear diccionario para mapear brecha -> brecha_id
    brecha_to_id = dict(zip(brechas_df['brecha'], brechas_df['id']))
    
    # Asignar project_id secuencial
    df_clean['project_id'] = range(1, len(df_clean) + 1)
    
    # Mapear nombre de brecha a brecha_id
    df_clean['brecha_ids'] = df_clean[brecha_col].map(brecha_to_id)
    
    # Crear columna de descripción
    if descripcion_col:
        df_clean['description'] = df_clean[descripcion_col].fillna(df_clean[titulo_col])
    else:
        # Si no hay columna de descripción, usar el título como descripción
        df_clean['description'] = df_clean[titulo_col]
    
    # Crear DataFrame final de proyectos
    proyectos_df = df_clean[[
        'project_id',
        titulo_col,
        'description',
        'brecha_ids'
    ]].copy()
    
    # Renombrar columnas al formato requerido
    proyectos_df.columns = ['project_id', 'title', 'description', 'brecha_ids']
    
    # Convertir brecha_ids a string (formato "1" o "1,3" para multi-label)
    proyectos_df['brecha_ids'] = proyectos_df['brecha_ids'].astype(str)
    
    # Guardar proyectos.csv
    proyectos_output = output_dir / "proyectos.csv"
    proyectos_df.to_csv(proyectos_output, index=False, encoding='utf-8-sig')
    print(f"\n✅ Generado: {proyectos_output}")
    print(f"   Total de proyectos: {len(proyectos_df)}")
    
    # ====================================================================
    # RESUMEN Y ESTADÍSTICAS
    # ====================================================================
    
    print("\n" + "="*80)
    print("📊 RESUMEN DE PROCESAMIENTO")
    print("="*80)
    print(f"✅ Brechas únicas: {len(brechas_df)}")
    print(f"✅ Proyectos procesados: {len(proyectos_df)}")
    print(f"\n📂 Archivos generados:")
    print(f"   - {brechas_output}")
    print(f"   - {proyectos_output}")
    
    # Mostrar distribución de proyectos por brecha
    print("\n📊 Distribución de proyectos por brecha:")
    distribucion = proyectos_df['brecha_ids'].value_counts().sort_index()
    for brecha_id, count in distribucion.items():
        brecha_id_int = int(brecha_id) if brecha_id.isdigit() else None
        if brecha_id_int and brecha_id_int in brechas_df['id'].values:
            brecha_nombre = brechas_df[brechas_df['id'] == brecha_id_int]['brecha'].iloc[0]
            print(f"   Brecha {brecha_id}: {count} proyectos - {brecha_nombre[:60]}...")
    
    print("\n" + "="*80)
    print("✅ PROCESAMIENTO COMPLETADO EXITOSAMENTE")
    print("="*80)
    print("\n💡 Próximo paso:")
    print("   Copia los archivos generados a la carpeta 'data/':")
    print(f"   - Copiar {brechas_output} → data/brechas.csv")
    print(f"   - Copiar {proyectos_output} → data/proyectos.csv")
    print("="*80)


if __name__ == "__main__":
    procesar_excel()
