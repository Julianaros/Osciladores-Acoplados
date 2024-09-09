import matplotlib.pyplot as plt

# Definir el tiempo
t = np.linspace(0, 20, 400)

# Dupla solución analítica
x1_analitica, x2_analitica = analitica(t)

# Dupla solución numérica
x1_numerica, x2_numerica = numerica(t)


# Crear una figura y un arreglo de subgráficas (2 filas, 1 columna)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

#Graficar soluciones en un solo gráfico

ax1.plot(t, x1_analitica, label='Solución Analítica x1', linestyle='--', color='blue')
ax1.plot(t, x2_analitica, label='Solución Analítica x2', linestyle='--', color='red')
ax1.set_xlabel("Tiempo (s)")
ax1.set_ylabel("Posición (m)")
ax1.set_title("Oscilador Acoplado Solución Analítica")
ax1.legend()



# Definir el tiempo
t = np.linspace(0, 20, 400)

# Obtener soluciones numéricas
resultados_euler, resultados_rk4 = numerica(t)

# Crear una figura y un arreglo de subgráficas (2 filas, 1 columna)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Graficar soluciones numéricas para Euler
ax1.plot(t, resultados_euler[0], label='Euler x1', linestyle='--', color='green')
ax1.plot(t, resultados_euler[1], label='Euler x2', linestyle='--', color='orange')
ax1.set_xlabel("Tiempo (s)")
ax1.set_ylabel("Posición (m)")
ax1.set_title("Oscilador Acoplado - Solución Numérica (Euler)")
ax1.legend()

# Graficar soluciones numéricas para RK4
ax2.plot(t, resultados_rk4[0], label='RK4 x1', linestyle='-.', color='purple')
ax2.plot(t, resultados_rk4[1], label='RK4 x2', linestyle=':', color='cyan')
ax2.set_xlabel("Tiempo (s)")
ax2.set_ylabel("Posición (m)")
ax2.set_title("Oscilador Acoplado - Solución Numérica (RK4)")
ax2.legend()

# Ajustar el espaciado entre subgráficas
plt.tight_layout()

plt.show()
