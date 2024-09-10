import numpy as np
import matplotlib.pyplot as plt

# Funciones para el sistema acoplado
def f1(x1, x2, v1, v2):
    return v1

def f2(x1, x2, v1, v2):
    return v2

def f3(x1, x2, v1, v2, k1, k2, m):
    return -(k1 + k2) * x1 / m + k2 * x2 / m

def f4(x1, x2, v1, v2, k1, k2, m):
    return -(k1 + k2) * x2 / m + k2 * x1 / m

# Función que ejecuta ambos métodos y devuelve una dupla
def numerica(t):
    # Función para obtener las constantes y condiciones iniciales
    def ingresar_parametros():
        # Constantes del problema
        k1 = float(input("Ingrese la constante del resorte 1 (k1): "))
        k2 = float(input("Ingrese la constante del resorte 2 (k2): "))
        m = float(input("Ingrese la masa (m): "))

        # Condiciones iniciales
        x1_0 = float(input("Ingrese la posición inicial de la masa 1 (x1_0): "))
        x2_0 = float(input("Ingrese la posición inicial de la masa 2 (x2_0): "))
        vx1_0 = float(input("Ingrese la velocidad inicial de la masa 1 (vx1_0): "))
        vx2_0 = float(input("Ingrese la velocidad inicial de la masa 2 (vx2_0): "))

        # Retornar todos los parámetros
        return k1, k2, m, x1_0, x2_0, vx1_0, vx2_0

    # Obtener parámetros
    k1, k2, m, x1_0, x2_0, vx1_0, vx2_0 = ingresar_parametros()

    dt = t[1] - t[0]  # Paso de tiempo, asumimos que t es uniforme
    
    # Inicialización de arrays
    n_steps = len(t)
    x1_euler = np.zeros(n_steps)
    x2_euler = np.zeros(n_steps)
    v1_euler = np.zeros(n_steps)
    v2_euler = np.zeros(n_steps)

    x1_rk4 = np.zeros(n_steps)
    x2_rk4 = np.zeros(n_steps)
    v1_rk4 = np.zeros(n_steps)
    v2_rk4 = np.zeros(n_steps)
    
    # Condiciones iniciales
    x1_euler[0], x2_euler[0], v1_euler[0], v2_euler[0] = x1_0, x2_0, vx1_0, vx2_0
    x1_rk4[0], x2_rk4[0], v1_rk4[0], v2_rk4[0] = x1_0, x2_0, vx1_0, vx2_0
    
    # Método de Euler
    for i in range(n_steps - 1):
        x1_euler[i + 1] = x1_euler[i] + dt * f1(x1_euler[i], x2_euler[i], v1_euler[i], v2_euler[i])
        x2_euler[i + 1] = x2_euler[i] + dt * f2(x1_euler[i], x2_euler[i], v1_euler[i], v2_euler[i])
        v1_euler[i + 1] = v1_euler[i] + dt * f3(x1_euler[i], x2_euler[i], v1_euler[i], v2_euler[i], k1, k2, m)
        v2_euler[i + 1] = v2_euler[i] + dt * f4(x1_euler[i], x2_euler[i], v1_euler[i], v2_euler[i], k1, k2, m)
    
    # Método de Runge-Kutta de cuarto orden (RK4)
    for i in range(n_steps - 1):
        k1_x1 = dt * f1(x1_rk4[i], x2_rk4[i], v1_rk4[i], v2_rk4[i])
        k1_x2 = dt * f2(x1_rk4[i], x2_rk4[i], v1_rk4[i], v2_rk4[i])
        k1_v1 = dt * f3(x1_rk4[i], x2_rk4[i], v1_rk4[i], v2_rk4[i], k1, k2, m)
        k1_v2 = dt * f4(x1_rk4[i], x2_rk4[i], v1_rk4[i], v2_rk4[i], k1, k2, m)
        
        k2_x1 = dt * f1(x1_rk4[i] + 0.5 * k1_x1, x2_rk4[i] + 0.5 * k1_x2, v1_rk4[i] + 0.5 * k1_v1, v2_rk4[i] + 0.5 * k1_v2)
        k2_x2 = dt * f2(x1_rk4[i] + 0.5 * k1_x1, x2_rk4[i] + 0.5 * k1_x2, v1_rk4[i] + 0.5 * k1_v1, v2_rk4[i] + 0.5 * k1_v2)
        k2_v1 = dt * f3(x1_rk4[i] + 0.5 * k1_x1, x2_rk4[i] + 0.5 * k1_x2, v1_rk4[i] + 0.5 * k1_v1, v2_rk4[i] + 0.5 * k1_v2, k1, k2, m)
        k2_v2 = dt * f4(x1_rk4[i] + 0.5 * k1_x1, x2_rk4[i] + 0.5 * k1_x2, v1_rk4[i] + 0.5 * k1_v1, v2_rk4[i] + 0.5 * k1_v2, k1, k2, m)
        
        k3_x1 = dt * f1(x1_rk4[i] + 0.5 * k2_x1, x2_rk4[i] + 0.5 * k2_x2, v1_rk4[i] + 0.5 * k2_v1, v2_rk4[i] + 0.5 * k2_v2)
        k3_x2 = dt * f2(x1_rk4[i] + 0.5 * k2_x1, x2_rk4[i] + 0.5 * k2_x2, v1_rk4[i] + 0.5 * k2_v1, v2_rk4[i] + 0.5 * k2_v2)
        k3_v1 = dt * f3(x1_rk4[i] + 0.5 * k2_x1, x2_rk4[i] + 0.5 * k2_x2, v1_rk4[i] + 0.5 * k2_v1, v2_rk4[i] + 0.5 * k2_v2, k1, k2, m)
        k3_v2 = dt * f4(x1_rk4[i] + 0.5 * k2_x1, x2_rk4[i] + 0.5 * k2_x2, v1_rk4[i] + 0.5 * k2_v1, v2_rk4[i] + 0.5 * k2_v2, k1, k2, m)
        
        k4_x1 = dt * f1(x1_rk4[i] + k3_x1, x2_rk4[i] + k3_x2, v1_rk4[i] + k3_v1, v2_rk4[i] + k3_v2)
        k4_x2 = dt * f2(x1_rk4[i] + k3_x1, x2_rk4[i] + k3_x2, v1_rk4[i] + k3_v1, v2_rk4[i] + k3_v2)
        k4_v1 = dt * f3(x1_rk4[i] + k3_x1, x2_rk4[i] + k3_x2, v1_rk4[i] + k3_v1, v2_rk4[i] + k3_v2, k1, k2, m)
        k4_v2 = dt * f4(x1_rk4[i] + k3_x1, x2_rk4[i] + k3_x2, v1_rk4[i] + k3_v1, v2_rk4[i] + k3_v2, k1, k2, m)
        
        x1_rk4[i + 1] = x1_rk4[i] + (k1_x1 + 2 * k2_x1 + 2 * k3_x1 + k4_x1) / 6
        x2_rk4[i + 1] = x2_rk4[i] + (k1_x2 + 2 * k2_x2 + 2 * k3_x2 + k4_x2) / 6
        v1_rk4[i + 1] = v1_rk4[i] + (k1_v1 + 2 * k2_v1 + 2 * k3_v1 + k4_v1) / 6
        v2_rk4[i + 1] = v2_rk4[i] + (k1_v2 + 2 * k2_v2 + 2 * k3_v2 + k4_v2) / 6

    # Crear y devolver la dupla con los resultados de ambos métodos
    return (x1_euler, x2_euler), (x1_rk4, x2_rk4)


# Tiempo de simulación
t = np.linspace(0, 10, 1000)

# Resultados numéricos
euler_result, rk4_result = numerica(t)

# Gráficas de los resultados
plt.plot(t, euler_result[0], label='x1 (Euler)')
plt.plot(t, euler_result[1], label='x2 (Euler)')
plt.plot(t, rk4_result[0], label='x1 (RK4)')
plt.plot(t, rk4_result[1], label='x2 (RK4)')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.legend()
plt.show()
