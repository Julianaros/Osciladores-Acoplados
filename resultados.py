import matplotlib.pyplot as plt

# Tiempo
t = np.linespace(0,20,400)

# Dupla solución analítica
x1_anaitica, x2_analitica = analitica(t)

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

plt.plot(t, x1_numerica, label='Solución Numérica x1', linestyle='--', color='green')
plt.plot(t, x2_numerica, label='Solución Numérica x2', linestyle='--', color='orange')
plt.set_xlabel("Posición (m)")
plt.set_ylabel("Tiempo (s)")
plt.set_title("Oscilador Acopado Solución Numérica")
ax2.legend() 

# Ajustar el espaciado entre subgráficas
plt.tight_layout()

plt.show()
