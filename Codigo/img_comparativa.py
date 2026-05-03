import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Datos
e_z = 6.48148e-4
m_z = 12.06
e_c = 1.25e-4
m_c = 86.3

# Crear figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Cono: radio = k * z, con z = epsilon, k = pendiente
z = np.linspace(0, 1e-3, 50)
r = z * 1000  # factor de escala para visualización
theta = np.linspace(0, 2*np.pi, 50)
Z, Theta = np.meshgrid(z, theta)
R = Z * 1000
X = R * np.cos(Theta)
Y = R * np.sin(Theta)
ax.plot_surface(X, Y, Z, alpha=0.3, color='gray')

# Puntos
ax.scatter(0, 0, 0, color='black', s=50, label='Tensor Hubble (fulcro)')
ax.scatter(e_z*1000, 0, m_z/100, color='blue', s=100, label='ZAGGI (SINTRE)')
ax.scatter(e_c*1000, 0, m_c/100, color='red', s=100, label='CERN (taladrando)')

ax.set_xlabel('ε (×1000)')
ax.set_ylabel('Fase')
ax.set_zlabel('Masa (×100 t)')
ax.legend()
plt.show()
