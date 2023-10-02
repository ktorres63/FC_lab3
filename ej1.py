#Escriba la ecuación 2 en código computacional para resolver ejercicios
#de Movimiento Armónico Simple de forma generalizada. Tome en cuen-
#ta la velocidad, aceleración, velocidad máxima y aceleración máxima.

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
#T =2π/ω
def periodo(frAng):
    return 2*math.pi/frAng
#v(t) = -A*ω*sen(ωt + φ)
def velocidad(amp,frAng,t,af):
    return -amp*frAng*math.sin(frAng*t+af)
#v(t) = -A*ω^2*sen(ωt + φ)
def aceleración(amp,frAng,t,af):
    return -amp*frAng**2*math.cos(frAng*t+af)
#vMax = ω*A
def vMax(frAng,amp):
    return frAng*amp
#aMax = ω^2*A
def aMax(frAng,amp):
    return frAng**2*amp


print("Calculadora MAS")
amp = float(input("Ingrese la amplitud: "))
frAng = string_to_number(input("Ingrese la frecuencia Angular: "))

ch = input("ingrese (x) si desea calcular la posicion (T) el periodo: ")

if(ch =="x"):
    t = float(input("Ingrese el tiempo: "))
    af = string_to_number(input("Ingrese el angulo de fase: "))

    pos = posicion(amp,frAng,t,af)
    vel =  velocidad(amp,frAng,t,af)
    acel = aceleración(amp,frAng,t,af)
    
    print("-----------------------------------------------------")
    print(f"la posicion en el tiempo {t} s es {pos} m")
    print(f"la velocidad en el tiempo {t} s es {vel} m/s")
    print(f"la aceleracion en el tiempo {t} s es {acel} m/s^2")

elif(ch == "T"):
    per = periodo(frAng)
    print(f"El periodo es {per} seg")

else:
    print("ingrese una opcion valida")

vMax = abs(vMax(frAng,amp))
aMax = abs(aMax(frAng,amp))
print("-----------------------------------------------------")
print(f"la posicion maxima es {amp} m")
print(f"la velocidad maxima es {vMax} m/s")
print(f"la aceleracion maxima es {aMax} m/s^2")