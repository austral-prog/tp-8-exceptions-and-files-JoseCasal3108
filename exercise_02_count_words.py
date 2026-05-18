# Ejercicio 2 - Contar palabras en un archivo


def count_words(filename):
    """
    Lee un archivo y retorna un diccionario palabra -> cantidad.

    Reglas:
    - Las palabras se separan por espacios en blanco (cualquier tipo:
      espacios, tabs, saltos de línea). El método .split() sin argumentos
      ya maneja eso.
    - El conteo es case-insensitive: "Hola" y "hola" cuentan como la
      misma palabra. En el diccionario final las claves están en
      minúsculas.
    - Si el archivo está vacío, retornar {}.
    - Si el archivo no existe, propagar FileNotFoundError.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        dict[str, int] - cada palabra (en minúscula) con su frecuencia.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene: "Hola mundo hola\nmundo python\n"
        count_words("texto.txt") -> {"hola": 2, "mundo": 2, "python": 1}
    """

    # Lanzar FileNotFoundError con raise
    import os
    if not os.path.exists(filename):
        raise FileNotFoundError("No existe el archivo")

    dicc = {}

    with open(filename, "r") as archivo:
        for line in archivo:
            line = line.strip()
            line = line.lower()
            palabras = line.split() #si no le pongo nada en el parentesis separa las palabras con espacios en blanco

            for palabra in palabras:
                if palabra in dicc:
                    dicc[palabra] += 1
                else:
                    dicc[palabra] = 1

        return dicc
