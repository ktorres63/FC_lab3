#Escriba la ecuación 4 en código computacional para resolver ejercicios
#de Oscilaciones Forzadas de forma generalizada.

#A: amplitud (m)
#t: tiempo(s)
#ω: frecuencia Angular (rad/s)
#φ: angulo de fase (rad)
import math
import sympy as sp

def string_to_number(cadena):
    try:
        expresion = sp.sympify(cadena)
        resultado = float(expresion)
        return resultado
    except (sp.SympifyError, ValueError):
        return None


#x(t) = A*cos(ωt + φ)
def posicion(amp,frAng,t,af):
    return amp*math.cos(frAng*t+af)

def amplitud(fm,m,w,wm,b):
    den = math.sqrt((w**2-wm**2)**2+(b*w/m)**2)
    if m == 0 or den == 0:
        return 0 # cuando la masa es 0
    else: 
        return (fm/m)/den

print("Calculadora MAS forzado")

ch = input("ingrese (x) si desea calcular la posicion o (A) amplitud: ")

if(ch =="x"):
    amp = float(input("Ingrese la amplitud: "))
    frAng = string_to_number(input("Ingrese la frecuencia Angular: "))
    t = float(input("Ingrese el tiempo: "))
    af = string_to_number(input("Ingrese el angulo de fase: "))

    pos = posicion(amp,frAng,t,af)
   
    print("-----------------------------------------------------")
    print(f"la posicion en el tiempo {t} s es {pos} m")

elif(ch == "A"):
    fmax = float(input("ingresa la fuerza maxima: "))
    m = float(input("ingresa la masa: "))
    frAng = string_to_number(input("Ingrese la frecuencia Angular: "))
    frNat = string_to_number(input("Ingrese la frecuencia Natural: "))
    b = float(input("constante de amortiguamiento: "))

    ampl = amplitud(fmax,m,frAng,frNat,b)
    print(f"la amplitud es: {ampl} m")

else:
    print("ingrese una opcion valida")

