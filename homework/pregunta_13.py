"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """


    import pandas as pd

    # Rutas de los archivos .tsv
    archivo_tbl0 = "files/input/tbl0.tsv"
    archivo_tbl2 = "files/input/tbl2.tsv"
    
    # Leer los archivos .tsv
    df_tbl0 = pd.read_csv(archivo_tbl0, sep="\t")
    df_tbl2 = pd.read_csv(archivo_tbl2, sep="\t")
    
    # Agrupar y sumar 'c5b' en 'tbl2.tsv' por 'c0'
    suma_c5b = df_tbl2.groupby('c0')['c5b'].sum().reset_index()

    # Unir la suma de 'c5b' con 'tbl0' por la columna 'c0' y obtener la columna 'c1'
    resultado = pd.merge(df_tbl0[['c0', 'c1']], suma_c5b, on='c0', how='left')

    # Agrupar por 'c1' y sumar los valores de 'c5b'
    suma_por_c1 = resultado.groupby('c1')['c5b'].sum()

    return suma_por_c1

if __name__ == "__main__":
    print(pregunta_13())
