import numpy as np

# Constantes del problema
k1 = 2.0  # Constante del resorte 1
k2 = 1.5  # Constante del resorte 2
m = 1.0   # Masa

# Condiciones iniciales
x1_0 = 1.0   # Posición inicial de la masa 1 (x1)
x2_0 = 0.0   # Posición inicial de la masa 2 (x2)
vx1_0 = 0.0  # Velocidad inicial de la masa 1 (v1)
vx2_0 = 1.0  # Velocidad inicial de la masa 2 (v2)

# Funciones para el sistema acoplado
def f1(x1, x2, v1, v2):
    return v1

def f2(x1, x2, v1, v2):
    return v2

def f3(x1, x2, v1, v2):
    return -(k1 + k2) * x1 / m + k2 * x2 / m

def f4(x1, x2, v1, v2):
    return -(k1 + k2) * x2 / m + k2 * x1 / m

# Función que ejecuta ambos métodos y devuelve una dupla
def ejecutar_metodos(t0, tf, dt):
    # Generar el array de tiempos usando linspace
    t = np.linspace(t0, tf, int((tf - t0) / dt) + 1)
    n_steps = len(t)
    
    # Inicialización de arrays
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
        v1_euler[i + 1] = v1_euler[i] + dt * f3(x1_euler[i], x2_euler[i], v1_euler[i], v2_euler[i])
        v2_euler[i + 1] = v2_euler[i] + dt * f4(x1_euler[i], x2_euler[i], v1_euler[i], v2_euler[i])
    
    # Método de Runge-Kutta de cuarto orden (RK4)
    for i in range(n_steps - 1):
        k1_x1 = dt * f1(x1_rk4[i], x2_rk4[i], v1_rk4[i], v2_rk4[i])
        k1_x2 = dt * f2(x1_rk4[i], x2_rk4[i], v1_rk4[i], v2_rk4[i])
        k1_v1 = dt * f3(x1_rk4[i], x2_rk4[i], v1_rk4[i], v2_rk4[i])
        k1_v2 = dt * f4(x1_rk4[i], x2_rk4[i], v1_rk4[i], v2_rk4[i])
        
        k2_x1 = dt * f1(x1_rk4[i] + 0.5 * k1_x1, x2_rk4[i] + 0.5 * k1_x2, v1_rk4[i] + 0.5 * k1_v1, v2_rk4[i] + 0.5 * k1_v2)
        k2_x2 = dt * f2(x1_rk4[i] + 0.5 * k1_x1, x2_rk4[i] + 0.5 * k1_x2, v1_rk4[i] + 0.5 * k1_v1, v2_rk4[i] + 0.5 * k1_v2)
        k2_v1 = dt * f3(x1_rk4[i] + 0.5 * k1_x1, x2_rk4[i] + 0.5 * k1_x2, v1_rk4[i] + 0.5 * k1_v1, v2_rk4[i] + 0.5 * k1_v2)
        k2_v2 = dt * f4(x1_rk4[i] + 0.5 * k1_x1, x2_rk4[i] + 0.5 * k1_x2, v1_rk4[i] + 0.5 * k1_v1, v2_rk4[i] + 0.5 * k1_v2)
        
        k3_x1 = dt * f1(x1_rk4[i] + 0.5 * k2_x1, x2_rk4[i] + 0.5 * k2_x2, v1_rk4[i] + 0.5 * k2_v1, v2_rk4[i] + 0.5 * k2_v2)
        k3_x2 = dt * f2(x1_rk4[i] + 0.5 * k2_x1, x2_rk4[i] + 0.5 * k2_x2, v1_rk4[i] + 0.5 * k2_v1, v2_rk4[i] + 0.5 * k2_v2)
        k3_v1 = dt * f3(x1_rk4[i] + 0.5 * k2_x1, x2_rk4[i] + 0.5 * k2_x2, v1_rk4[i] + 0.5 * k2_v1, v2_rk4[i] + 0.5 * k2_v2)
        k3_v2 = dt * f4(x1_rk4[i] + 0.5 * k2_x1, x2_rk4[i] + 0.5 * k2_x2, v1_rk4[i] + 0.5 * k2_v1, v2_rk4[i] + 0.5 * k2_v2)
        
        k4_x1 = dt * f1(x1_rk4[i] + k3_x1, x2_rk4[i] + k3_x2, v1_rk4[i] + k3_v1, v2_rk4[i] + k3_v2)
        k4_x2 = dt * f2(x1_rk4[i] + k3_x1, x2_rk4[i] + k3_x2, v1_rk4[i] + k3_v1, v2_rk4[i] + k3_v2)
        k4_v1 = dt * f3(x1_rk4[i] + k3_x1, x2_rk4[i] + k3_x2, v1_rk4[i] + k3_v1, v2_rk4[i] + k3_v2)
        k4_v2 = dt * f4(x1_rk4[i] + k3_x1, x2_rk4[i] + k3_x2, v1_rk4[i] + k3_v1, v2_rk4[i] + k3_v2)
        
        x1_rk4[i + 1] = x1_rk4[i] + (k1_x1 + 2 * k2_x1 + 2 * k3_x1 + k4_x1) / 6
        x2_rk4[i + 1] = x2_rk4[i] + (k1_x2 + 2 * k2_x2 + 2 * k3_x2 + k4_x2) / 6
        v1_rk4[i + 1] = v1_rk4[i] + (k1_v1 + 2 * k2_v1 + 2 * k3_v1 + k4_v1) / 6
        v2_rk4[i + 1] = v2_rk4[i] + (k1_v2 + 2 * k2_v2 + 2 * k3_v2 + k4_v2) / 6

    # Crear y devolver la dupla con los resultados de ambos métodos
    return (x1_euler, x2_euler), (x1_rk4, x2_rk4)

# Ejecutar ambos métodos usando tiempo final tf = 10, tiempo inicial t0 = 0, y paso dt = 0.01
resultados_euler, resultados_rk4 = ejecutar_metodos(0, 10, 0.01)

# Ejemplo de impresión de los primeros 5 resultados
for i in range(5):
    print(f"t = {i * 0.01:.2f}, Euler: x1 = {resultados_euler[0][i]:.4f}, x2 = {resultados_euler[1][i]:.4f}")
    print(f"t = {i * 0.01:.2f}, RK4: x1 = {resultados_rk4[0][i]:.4f}, x2 = {resultados_rk4[1][i]:.4f}")
