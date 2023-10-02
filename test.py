import sympy as sp

def convertir_cadena_a_numero(cadena):
    try:
        # Crear un símbolo para pi
        pi = sp.pi
        # Analizar la cadena en una expresión simbólica
        expresion = sp.sympify(cadena)

        # Evaluar la expresión para obtener un número decimal
        resultado = float(expresion)
        return resultado
    except (sp.SympifyError, ValueError):
        return None

cadena = "3*pi/2"
numero = convertir_cadena_a_numero(cadena)

if numero is not None:
    print(f"La cadena '{cadena}' equivale a: {numero}")
else:
    print(f"No se pudo convertir la cadena '{cadena}' a un número.")