"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """


    import pandas as pd

    archivo_tsv = "files/input/tbl0.tsv"
    df = pd.read_csv(archivo_tsv, sep="\t")


    numero_filas = len(df)

    return numero_filas



if __name__ == "__main__":
    print(pregunta_01())

