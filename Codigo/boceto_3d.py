import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Datos
e_z = 6.48148e-4
m_z = 12062
e_c = 1.25e-4
m_c = 86.3
delta_e = e_z - e_c
k_z = m_z / e_z   # pendiente ZAGGI

# Cono ZAGGI (base en +X, punta en 0)
z_cone = np.linspace(0, e_z, 50)
r_z = k_z * z_cone
theta = np.linspace(0, 2*np.pi, 30)
Z_z, Theta_z = np.meshgrid(z_cone, theta)
R_z = k_z * Z_z
X_z = R_z * np.cos(Theta_z)
Y_z = R_z * np.sin(Theta_z)

# Cono CERN (base en -X, punta en 0) – reflejado
z_c_neg = np.linspace(0, e_c, 50)
r_c = k_z * z_c_neg   # usamos misma pendiente para visualizar, aunque la real es menor
X_c = -r_c * np.cos(Theta_z)
Y_c = r_c * np.sin(Theta_z)
Z_c = Z_z   # mismo rango en z

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Superficies
ax.plot_surface(X_z, Y_z, Z_z, alpha=0.4, color='blue', label='Cono ZAGGI (5D)')
ax.plot_surface(X_c, Y_c, Z_c, alpha=0.4, color='red', label='Cono CERN (4D)')

# Tubería cilíndrica entre las bases (simplificada como línea)
# Coordenadas de las bases: (m_z,0,e_z) y (-m_c,0,e_c)
ax.plot([-m_c/1000, m_z/1000], [0,0], [e_c, e_z], color='gold', linewidth=4, label='Tubería de carbón fotónico')

# Puntos de las bases
ax.scatter(-m_c/1000, 0, e_c, color='red', s=100, label='Base CERN (86,3 t)')
ax.scatter(m_z/1000, 0, e_z, color='blue', s=100, label='Base ZAGGI (12.062 t)')

# Esfera de la rendija (en el centro)
ax.scatter(0, 0, (e_z+e_c)/2, color='orange', s=200, label='Rendija Δε (9.735 t)')

# Ejes y etiquetas
ax.set_xlabel('Masa (×1000 t) / Fase')
ax.set_ylabel('')
ax.set_zlabel('ε')
ax.set_title('Puerta de la 5D – Conos enfrentados y tubería de carbón fotónico')
ax.legend()
plt.show()
