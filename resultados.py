from librerias import *
from analitica import analitica  
from Final_Final_Final_ESTE_SI import numerica  

# Tiempo
t = np.linspace(0,20,400)

# Dupla solución analítica
x1_analitica, x2_analitica = analitica(t)

# Dupla soluciones numéricas
euler_result, rk4_result = numerica(t)
# Crear una figura y un arreglo de subgráficas (1 fila con 3 columnas)
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 12))

# Graficar soluciones en un solo gráfico
ax1.plot(t, x1_analitica, label='Solución Analítica x1', linestyle='--', color='blue')
ax1.plot(t, x2_analitica, label='Solución Analítica x2', linestyle='--', color='red')
ax1.set_xlabel("Tiempo (s)")
ax1.set_ylabel("Posición (m)")
ax1.set_title("Oscilador Acoplado - Solución Analítica")
ax1.legend()

ax2.plot(t, euler_result[0], label='x1 (Euler)', linestyle='-', color='green')
ax2.plot(t, euler_result[1], label='x2 (Euler)', linestyle='-', color='orange')
ax2.set_xlabel("Tiempo (s)")
ax2.set_ylabel("Posición (m)")
ax2.set_title("Oscilador Acoplado - Método de Euler")
ax2.legend()

ax3.plot(t, rk4_result[0], label='x1 (RK4)', linestyle='-', color='purple')
ax3.plot(t, rk4_result[1], label='x2 (RK4)', linestyle='-', color='green')
ax3.set_xlabel("Tiempo (s)")
ax3.set_ylabel("Posición (m)")
ax3.set_title("Oscilador Acoplado - Método Runge-Kutta 4")
ax3.legend()

plt.subplots_adjust(hspace=1)  # Espacio entre gráficas.
plt.show()

