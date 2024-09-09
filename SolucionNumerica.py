import numpy as np

# Constantes del problema
k1 = 2.0  # Constante del resorte 1
k2 = 1.5  # Constante del resorte 2
m = 1.0   # Masa

# Condiciones iniciales para Euler y Runge-Kutta
x1_0 = 1.0   # Posición inicial de la masa 1 (x1)
x2_0 = 0.0   # Posición inicial de la masa 2 (x2)
vx1_0 = 0.0  # Velocidad inicial de la masa 1 (v1)
vx2_0 = 1.0  # Velocidad inicial de la masa 2 (v2)

# Tiempo de simulación
t0, tf, dt = 0.0, 10.0, 0.01

# Funciones para el sistema acoplado
def f1(x1, x2, v1, v2, k1, k2, m):
    return v1

def f2(x1, x2, v1, v2, k1, k2, m):
    return v2

def f3(x1, x2, v1, v2, k1, k2, m):
    return -(k1 + k2) * x1 / m + k2 * x2 / m

def f4(x1, x2, v1, v2, k1, k2, m):
    return -(k1 + k2) * x2 / m + k2 * x1 / m

# Método de Euler
def euler(x1_0, x2_0, v1_0, v2_0, t0, tf, dt, k1, k2, m):
    n_steps = int((tf - t0) / dt)
    x1 = np.zeros(n_steps)
    x2 = np.zeros(n_steps)
    v1 = np.zeros(n_steps)
    v2 = np.zeros(n_steps)
    
    x1[0], x2[0], v1[0], v2[0] = x1_0, x2_0, v1_0, v2_0
    
    for i in range(n_steps - 1):
        x1[i + 1] = x1[i] + dt * f1(x1[i], x2[i], v1[i], v2[i], k1, k2, m)
        x2[i + 1] = x2[i] + dt * f2(x1[i], x2[i], v1[i], v2[i], k1, k2, m)
        v1[i + 1] = v1[i] + dt * f3(x1[i], x2[i], v1[i], v2[i], k1, k2, m)
        v2[i + 1] = v2[i] + dt * f4(x1[i], x2[i], v1[i], v2[i], k1, k2, m)
    
    return x1, x2

# Método de Runge-Kutta de cuarto orden (RK4)
def runge_kutta_4(x1_0, x2_0, v1_0, v2_0, t0, tf, dt, k1, k2, m):
    n_steps = int((tf - t0) / dt)
    x1 = np.zeros(n_steps)
    x2 = np.zeros(n_steps)
    v1 = np.zeros(n_steps)
    v2 = np.zeros(n_steps)
    
    x1[0], x2[0], v1[0], v2[0] = x1_0, x2_0, v1_0, v2_0
    
    for i in range(n_steps - 1):
        k1_x1 = dt * f1(x1[i], x2[i], v1[i], v2[i], k1, k2, m)
        k1_x2 = dt * f2(x1[i], x2[i], v1[i], v2[i], k1, k2, m)
        k1_v1 = dt * f3(x1[i], x2[i], v1[i], v2[i], k1, k2, m)
        k1_v2 = dt * f4(x1[i], x2[i], v1[i], v2[i], k1, k2, m)
        
        k2_x1 = dt * f1(x1[i] + 0.5 * k1_x1, x2[i] + 0.5 * k1_x2, v1[i] + 0.5 * k1_v1, v2[i] + 0.5 * k1_v2, k1, k2, m)
        k2_x2 = dt * f2(x1[i] + 0.5 * k1_x1, x2[i] + 0.5 * k1_x2, v1[i] + 0.5 * k1_v1, v2[i] + 0.5 * k1_v2, k1, k2, m)
        k2_v1 = dt * f3(x1[i] + 0.5 * k1_x1, x2[i] + 0.5 * k1_x2, v1[i] + 0.5 * k1_v1, v2[i] + 0.5 * k1_v2, k1, k2, m)
        k2_v2 = dt * f4(x1[i] + 0.5 * k1_x1, x2[i] + 0.5 * k1_x2, v1[i] + 0.5 * k1_v1, v2[i] + 0.5 * k1_v2, k1, k2, m)
        
        k3_x1 = dt * f1(x1[i] + 0.5 * k2_x1, x2[i] + 0.5 * k2_x2, v1[i] + 0.5 * k2_v1, v2[i] + 0.5 * k2_v2, k1, k2, m)
        k3_x2 = dt * f2(x1[i] + 0.5 * k2_x1, x2[i] + 0.5 * k2_x2, v1[i] + 0.5 * k2_v1, v2[i] + 0.5 * k2_v2, k1, k2, m)
        k3_v1 = dt * f3(x1[i] + 0.5 * k2_x1, x2[i] + 0.5 * k2_x2, v1[i] + 0.5 * k2_v1, v2[i] + 0.5 * k2_v2, k1, k2, m)
        k3_v2 = dt * f4(x1[i] + 0.5 * k2_x1, x2[i] + 0.5 * k2_x2, v1[i] + 0.5 * k2_v1, v2[i] + 0.5 * k2_v2, k1, k2, m)
        
        k4_x1 = dt * f1(x1[i] + k3_x1, x2[i] + k3_x2, v1[i] + k3_v1, v2[i] + k3_v2, k1, k2, m)
        k4_x2 = dt * f2(x1[i] + k3_x1, x2[i] + k3_x2, v1[i] + k3_v1, v2[i] + k3_v2, k1, k2, m)
        k4_v1 = dt * f3(x1[i] + k3_x1, x2[i] + k3_x2, v1[i] + k3_v1, v2[i] + k3_v2, k1, k2, m)
        k4_v2 = dt * f4(x1[i] + k3_x1, x2[i] + k3_x2, v1[i] + k3_v1, v2[i] + k3_v2, k1, k2, m)
        
        x1[i + 1] = x1[i] + (k1_x1 + 2 * k2_x1 + 2 * k3_x1 + k4_x1) / 6
        x2[i + 1] = x2[i] + (k1_x2 + 2 * k2_x2 + 2 * k3_x2 + k4_x2) / 6
        v1[i + 1] = v1[i] + (k1_v1 + 2 * k2_v1 + 2 * k3_v1 + k4_v1) / 6
        v2[i + 1] = v2[i] + (k1_v2 + 2 * k2_v2 + 2 * k3_v2 + k4_v2) / 6
    
    return x1, x2

# Ejecutar los métodos numéricos
x1_euler, x2_euler = euler(x1_0, x2_0, vx1_0, vx2_0, t0, tf, dt, k1, k2, m)
x1_rk4, x2_rk4 = runge_kutta_4(x1_0, x2_0, vx1_0, vx2_0, t0, tf, dt, k1, k2, m)

# Guardar resultados en una dupla
resultados = (x1_euler, x1_rk4)

# Ejemplo de impresión de los primeros 5 resultados
for i in range(5):
    print(f"t = {t0 + i * dt:.2f}, Euler: x1 = {resultados[0][i]:.4f}, RK4: x1 = {resultados[1][i]:.4f}")
