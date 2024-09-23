# Osciladores-Acoplados

La ecuación diferencial ordinaria (EDO) para dos osciladores acoplados describe el comportamiento dinámico de dos sistemas oscilatorios que estan interconectados de alguna manera. Estos osciladores pueden ser masa-resorte, pendulums, etec.

En términos generales, si consideramos dos osciladores acoplados con posiciones $$x_1$$ y $$x_2$$, la EDO que descibe su movimiento suele tener la forma: 

$$
x_1 x_1'' = -k_1 x_1 - k_{12} (x_1 - x_2) = m_2 x_2'' = -k_2 x_2 - k_{21} (x_2 - x_1)
$$


donde: 

$$m_1$$ y $$m_2$$ son las masas de los osciladores.

$$k_1$$ y $$k_2$$ son las constantes del resorte de los osciladores individuales.

$$k_12$$ $$k_21$$ son las constantes que describen el acoplamiento entre los dos osciladores.

Hacemos la suposición de un primer tiempo donde $$m_1$$ se desplaza una distancia $$x$$ y una distancia $$y$$ amban en la misma dirección, en este caso se considera la derecha, la prolongación de los resortes son $$x$$ y $$y-x$$, respectivamente, y la comprensión del tercer resorte es $$y$$. Si las velocidades de las masas son $$x'$$ $$ y''$$  tenemos para las energías cinética y potencial:

$$T= 1/2 m x'² + 1/2 my'² $$ 

y

 $$V= 1/2 k_1 x² + 1/2 k_2 (y-x)² + 1/2 k_1 y²$$

 aplicando el lagrangiano, entonces la ecuación  en $$x$$ $$y$$

$$mx''+ (k_1+k_2)x-k_2y=0$$
 
$$my''+ (k_1+k_2)y-k_2x=0$$

Al poner a cero el determinante de los coeficientes, encontramos para las frecuencias de los modos normales

$$\omega ²= k_1/m $$

$$\omega ² k_1 +2k_2 /m$$ ,

correspondiente al desplazamiento: 


$$x/y=1$$
y  
$$x/y =-1$$




En el primer modo, el modo lento, las masas se mueven en fase y no hay extensión ni compresión del resorte de acoplamiento. En el segundo modo, el modo rápido, las masas se mueven en antífase y la compresión o extensión del resorte de acoplamiento es el doble de la extensión o compresión de los resortes exteriores.

El movimiento general es una combinación lineal de los modos normales:


$$
x(t) = (x_0 +y_0 /2) \cos(\omega_1 t + \alpha_1) + (x_0 -y_0 /2) \cos(\omega_2 t + \alpha_2)
$$

$$
y(t) = (x_0 +y_0 /2) \cos(\omega_1 t + \alpha_1) - (x_0 -y_0 /2) \cos(\omega_2 t + \alpha_2)
$$



















Solución analítica: https://phys.libretexts.org/Bookshelves/Classical_Mechanics/Classical_Mechanics_(Tatum)/17%3A_Vibrating_Systems/17.07%3A_Two_Masses%2C_Three_Springs%2C_Two_brick_Walls

# Solución Numérica

## Descripción General

Este módulo implementa un sistema de simulación para un modelo acoplado de masas conectadas mediante resortes. Utiliza dos métodos numéricos:
- El **método de Euler**.
- El **método de Runge-Kutta de cuarto orden (RK4)**.

Ambos métodos se utilizan para resolver las ecuaciones diferenciales del sistema, y se devuelven los resultados de ambas soluciones para su posterior comparación.

El código permite al usuario ingresar parámetros como las constantes de los resortes, la masa y las condiciones iniciales, para simular el comportamiento de las masas en el tiempo.

## Funciones

### Función `f1(x1, x2, v1, v2)`
Calcula la derivada de la posición `x_1` respecto al tiempo, es decir, la velocidad `v_1`.

- **Parámetros**:
  - `x_1` (float): posición de la masa 1.
  - `x_2` (float): posición de la masa 2.
  - `v_1` (float): velocidad de la masa 1.
  - `v_2` (float): velocidad de la masa 2.
- **Retorno**: la velocidad de la masa 1, `v_1`.

### Función `f2(x1, x2, v1, v2)`
Calcula la derivada de la posición `x_2` respecto al tiempo, es decir, la velocidad `v_2`.

- **Parámetros**: mismos que `f1`.
- **Retorno**: velocidad de la masa 2, `v_2`.

### Función `f3(x1, x2, v1, v2, k1, k2, m)`
Calcula la aceleración de la masa 1 basada en las posiciones de ambas masas y las constantes de los resortes.

- **Parámetros**:
  - `x_1`, `x_2` (float): posiciones de las masas.
  - `v_1`, `v_2` (float): velocidades de las masas.
  - `k_1`, `k_2` (float): constantes de los resortes.
  - `m` (float): masa del sistema.
- **Retorno**: aceleración de la masa 1.

### Función `f4(x1, x2, v1, v2, k1, k2, m)`
Calcula la aceleración de la masa 2 en base a las posiciones de ambas masas y las constantes de los resortes.

- **Parámetros**: mismos que `f3`.
- **Retorno**: aceleración de la masa 2.

### Función `numerica(t)`
Ejecuta las simulaciones tanto con el método de Euler como con el método de Runge-Kutta de cuarto orden, devolviendo los resultados de ambos.

- **Parámetros**:
  - `t` (array-like): un array de tiempo uniformemente distribuido.
- **Retorno**: una dupla de tuplas:
  - `(x1_euler, x2_euler)`: posiciones calculadas mediante el método de Euler.
  - `(x1_rk4, x2_rk4)`: posiciones calculadas mediante el método de RK4.

### Función `ingresar_parametros()`
Solicita al usuario que ingrese los parámetros del sistema (constantes de los resortes, masa y condiciones iniciales) y devuelve estos valores.

- **Retorno**:
  - `k_1`, `k_2`, `m`, `x1_0`, `x2_0`, `vx1_0`, `vx2_0`: constantes del sistema y condiciones iniciales.

## Métodos Numéricos Implementados

### Método de Euler
Este método resuelve las ecuaciones diferenciales de manera iterativa, utilizando una aproximación de primer orden. Se actualizan las posiciones y velocidades de ambas masas en cada paso de tiempo.

### Método de Runge-Kutta de Cuarto Orden (RK4)
Este método es más preciso que el método de Euler, ya que utiliza una combinación ponderada de estimaciones intermedias para calcular los valores de las posiciones y velocidades en cada paso de tiempo.

## Ejecución del Programa

1. **Ingreso de Parámetros**: El programa solicita al usuario que ingrese las constantes del sistema y las condiciones iniciales.
2. **Simulación**: Se ejecutan las simulaciones utilizando tanto el método de Euler como RK4.
3. **Resultados**: El programa devuelve las posiciones de las masas en función del tiempo para ambos métodos.

## Consideraciones

- **Estabilidad numérica**: El método de Euler puede ser menos preciso y menos estable que el método de RK4, por lo que los resultados de RK4 deberían ser preferidos en simulaciones que requieren alta precisión.
- **Tiempo de Simulación**: El array `t` define el rango de tiempo para la simulación, y su longitud define el número de pasos temporales que se utilizarán.

## Ejemplo de Uso

```python
# Definir el intervalo de tiempo
t = np.linspace(0, 10, 1000)

# Ejecutar la simulación
euler_result, rk4_result = numerica(t)

# Graficar los resultados
plt.plot(t, euler_result[0], label="Masa 1 - Euler")
plt.plot(t, rk4_result[0], label="Masa 1 - RK4")
plt.legend()
plt.show()
```

# Graficador

Con ayuda del archivo resultados.py se pueden realizar las gráficas correspondientes a las soluciones del oscilador acoplado. Se importan las librerías necesarias y las respectivas funciones de los archivos que se encargaron de la solución teórica y las soluciones numéricas,se define el paso del tiempo y luego se genera la visualización de tres gráficas: Solución analítica, Método de Euler y Método Runge-Kutta 4 en una sola imagen.
