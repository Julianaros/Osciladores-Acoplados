# Osciladores-Acoplados

La ecuación diferencial ordinaria (EDO) para dos osciladores acoplados describe el comportamiento dinámico de dos sistemas oscilatorios que estan interconectados de alguna manera. Estos osciladores pueden ser masa-resorte, pendulums, etec.

En términos generales, si consideramos dos osciladores acoplados con posiciones $$x_1$$ y $$x_2$$, la EDO que descibe su movimiento suele tener la forma: 

$$x_1 x''_1= -k_1 x_1 - k_{12} (x_1 - x_2)m_2 x''_2 = -k_2 x_2 - k_{21} (x_2 - x_1)$$

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
x = (X_0 +y_0 /2) \cos(\omega_1 t + \alpha_1) + (x_0 -y_0 /2) \cos(\omega_2 t + \alpha_2)
$$

$$
y = (X_0 +y_0 /2) \cos(\omega_1 t + \alpha_1) - (x_0 -y_0 /2) \cos(\omega_2 t + \alpha_2)
$$


$$
x' = -(X_0 +y_0 /2) \sin(\omega_1 t + \alpha_1) - (x_0 -y_0 /2) \sin(\omega_2 t + \alpha_2)
$$


$$
y' = -(X_0 +y_0 /2) \cos(\omega_1 t + \alpha_1) + (x_0 -y_0 /2) \cos(\omega_2 t + \alpha_2)
$$


















Solución analítica: https://phys.libretexts.org/Bookshelves/Classical_Mechanics/Classical_Mechanics_(Tatum)/17%3A_Vibrating_Systems/17.07%3A_Two_Masses%2C_Three_Springs%2C_Two_brick_Walls
