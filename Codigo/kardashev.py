import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Datos
e_z = 6.48148e-4
m_z = 12062      # toneladas
e_c = 1.25e-4
m_c = 86.3

# Cono (r = k * z)
k = m_z / e_z   # pendiente de coherencia
z = np.linspace(0, 0.001, 50)
r = k * z
theta = np.linspace(0, 2*np.pi, 30)
Z, Theta = np.meshgrid(z, theta)
R = k * Z
X = R * np.cos(Theta)
Y = R * np.sin(Theta)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Superficie del cono
ax.plot_surface(X, Y, Z, alpha=0.3, color='blue')

# Eje del cono (recta crítica)
z_axis = np.linspace(0, 0.001, 100)
ax.plot([0]*100, [0]*100, z_axis, color='cyan', linewidth=2, label='Tensor Z (recta crítica)')

# Esfera de Hawking (centro en z=0.001, radio pequeño para visualizar)
u = np.linspace(0, 2*np.pi, 20)
v = np.linspace(0, np.pi, 20)
sphere_x = 0.0002 * np.outer(np.cos(u), np.sin(v))
sphere_y = 0.0002 * np.outer(np.sin(u), np.sin(v))
sphere_z = 0.001 + 0.0002 * np.outer(np.ones_like(u), np.cos(v))
ax.plot_surface(sphere_x, sphere_y, sphere_z, color='gold', alpha=0.6)

# Punto ZAGGI (dentro del cono, sobre el eje, en z=e_z)
ax.scatter(0, 0, e_z, color='blue', s=100, label='ZAGGI (estado SINTRE)')
ax.text(0, 0, e_z, '  ZAGGI\nCivilización tipo 2', color='blue', fontsize=8)

# Punto CERN (fuera del cono, en z=e_c, pero con radio > k*e_c)
r_c_cone = k * e_c   # radio del cono a esa altura
r_c = 0.001          # lo situamos muy lejos del eje para mostrar que está fuera
ax.scatter(r_c, 0, e_c, color='red', s=100, label='CERN (perforando)')
ax.text(r_c, 0, e_c, '  CERN\ntaladro', color='red', fontsize=8)

# Línea que muestra la perforación (desde el punto CERN hasta la superficie del cono)
ax.plot([r_c, r_c_cone], [0,0], [e_c, e_c], color='orange', linestyle='--', linewidth=2)

# Configuración de ejes
ax.set_xlabel('Masa / fase (escala arbitraria)')
ax.set_ylabel('')
ax.set_zlabel('ε (constante de soldadura)')
ax.set_title('Puerta de Kardashev: Dominio ZAGGI (cono de coherencia)\ny taladro del CERN perforando desde fuera')
ax.legend()
plt.show()
