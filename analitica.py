from librerias import *

def analitica(t):
    k1 = float(input("Ingrese el valor de k_1 en unidades internacionales: "))
    k2 = float(input("Ingrese el valor de k_2 en unidades internacionales: "))
    m = float(input("Ingrese el valor de la masa en unidades internacionales: "))
    x0 = float(input("Ingrese la condición inicial para la primera masa: "))
    y0 = float(input("Ingrese la condición inicial para la segunda masa: "))

    w1 = np.sqrt(k1/m)
    w2 = np.sqrt((k1+2*k2)/m)

    x = ((x0 + y0)/2)*np.cos(w1*t) + ((x0 - y0)/2)*np.cos(w2*t)
    y = ((x0 + y0)/2)*np.cos(w1*t) - ((x0 - y0)/2)*np.cos(w2*t)

    return x,y