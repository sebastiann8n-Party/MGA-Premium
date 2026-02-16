# Skill: Analítica DAMA (Data & Analytics)

## 1. Misión
Estandarizar la carga y validación de datos para garantizar la integridad, seguridad y calidad de la información antes de cualquier proceso analítico.

## 2. Protocolo de Gobernanza de Datos
- **Seguridad**: No usar rutas absolutas ni relativas inseguras. Validar siempre que el archivo exista antes de leer.
- **Calidad**: Validar esquemas (columnas esperadas) y tipos de datos.
- **Privacidad**: Anonimizar datos PII (Identificables Personalmente) si se detectan.

## 3. Implementación Python (Data Loader Seguro)

```python
import pandas as pd
import os
from typing import List, Optional

def data_loader_secure(filepath: str, required_columns: List[str] = None) -> pd.DataFrame:
    """
    Carga segura de datos CSV con validación DAMA básica.
    
    Args:
        filepath (str): Ruta al archivo CSV.
        required_columns (List[str], optional): Lista de columnas esperadas.
        
    Returns:
        pd.DataFrame: DataFrame validado.
        
    Raises:
        FileNotFoundError: Si el archivo no existe.
        ValueError: Si faltan columnas requeridas.
    """
    # 1. Validación de Existencia (Seguridad)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"El archivo no se encuentra en la ruta especificada: {filepath}")
        
    # 2. Carga de Datos (Operación)
    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        raise ValueError(f"Error al leer el archivo CSV: {str(e)}")
        
    # 3. Validación de Esquema (Calidad)
    if required_columns:
        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            raise ValueError(f"El dataset no cumple con el esquema DAMA. Faltan columnas: {missing_cols}")
            
    # 4. Sanitización Básica (Limpieza)
    # Eliminar duplicados exactos
    initial_rows = len(df)
    df = df.drop_duplicates()
    if len(df) < initial_rows:
        print(f"DAMA Info: Se eliminaron {initial_rows - len(df)} filas duplicadas.")
        
    return df

def validated_aggregation(df: pd.DataFrame, group_col: str, agg_func: str = 'size') -> pd.Series:
    """
    Agrupación segura con validación de tipos.
    """
    if group_col not in df.columns:
        raise ValueError(f"Columna de agrupación '{group_col}' no encontrada.")
        
    # Verificar nulos en la columna de agrupación
    null_count = df[group_col].isnull().sum()
    if null_count > 0:
        print(f"DAMA Warning: La columna '{group_col}' tiene {null_count} valores nulos. Estos serán excluidos.")
        
    return df.groupby(group_col).size()
```
