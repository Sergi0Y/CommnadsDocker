import matplotlib.pyplot as plt
import numpy as np
 
""" # Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Crear el gráfico de línea
plt.plot(x, y)

# Etiquetas y título
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de ejemplo con plot()')

# Mostrar el gráfico
plt.show()
 """

# ##############

# VECTORES
a = np.array([-1, 1])
b = np.array([1, 1])
dot = np.dot(a, b)
def Plotvec2(a, b, dot):
    ax = plt.axes()  # to generate the full window axes

    ax.arrow(0, 0, *a, head_width=0.05, color='r', head_length=0.1)  # Add an arrow to the  a Axes
    plt.text(*(a + 0.1), 'a')

    ax.arrow(0, 0, *b, head_width=0.05, color='b', head_length=0.1)  # Add an arrow to the  b Axes
    plt.text(*(b + 0.1), 'b')
    # muestra la variable en el gráfico
    plt.text(-1.5, 1.5, f'Valor externo: {dot}', fontsize=12, color='purple')
    # muestra la variable en el título
    plt.title(f'Gráfico de vectores (Valor externo: {dot})')

    plt.ylim(-2, 2)  # set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)  # set the xlim to left(-2), right(2)
        
    plt.show()

Plotvec2(a, b, dot)

