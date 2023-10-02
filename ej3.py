#3. Escriba las ecuaciones 6 y 8 en código computacional para resolver
#ejercicios de Oscilaciones Eléctricas de forma generalizada

#Qo: carga inicial (C) coulomb
#t: tiempo(s)
#ω: frecuencia Angular (rad/s)
#φ: angulo de fase (rad)
#L : Inductancia  (H)henrios
#C : Capacitancia (F) faradios
#R : Resistencia  (Ω) ohmios
import math
import sympy as sp

def string_to_number(cadena):
    try:
        expresion = sp.sympify(cadena)
        resultado = float(expresion)
        return resultado
    except (sp.SympifyError, ValueError):
        return None


#Q(t) = Qo*Sen(ωt + φ)
def cargaLC(carIn,frAng,t,af):
    return carIn*math.sin(frAng*t+af)

#Q(t) = Q0e−^γtSen(ωt + φ)
def cargaLCR(carIn,t,af,l,c,r):
    gamma = r/(2 * l)
    frAng = 1/math.sqrt(l * c)
    return (carIn * math.exp(-gamma * t) * math.sin(frAng*t + af))

print("calculo de circuito LC o LCR")
ch = input("ingrese (LC) o (LCR) de acuerdo al circuito que desee resolver ")
if(ch == "LC"):
    cargIn = float(input("Ingrese la carga Inicial: "))
    frAng = string_to_number(input("Ingrese la frecuencia Angular: "))
    t = float(input("Ingrese el tiempo: "))
    af = string_to_number(input("Ingrese el angulo de fase: "))

    q = carga(cargIn,frAng,t,af)
   
    print("-----------------------------------------------------")
    print(f"la carga en el tiempo {t} s es {q} C")
elif(ch == "LCR"):
    ##L : Inductancia  (H)henrios
    #C : Capacitancia (F) faradios
    #R : Resistencia  (Ω) ohmios
    cargIn = float(input("Ingrese la carga Inicial: "))
    t = float(input("Ingrese el tiempo: "))
    af = string_to_number(input("Ingrese el angulo de fase: "))
    l = float(input("ingrese la inductancia: "))
    c = float(input("ingrese la capacitancia: "))
    r = float(input("ingrese la resistencia: "))

    q = cargaLCR(cargIn,t,af,l,c,r)
   
    print("-----------------------------------------------------")
    print(f"la carga en el tiempo {t} s es {q} C")

else:
    print("ingrese una opcion valida")
