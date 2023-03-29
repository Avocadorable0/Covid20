import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Créer les données à tracer
x = [1.2, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
z = [3, 6, 9, 12, 15]

# Créer une figure et un axe 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Tracer les points en 3D
ax.scatter(x, y, z, marker='o')

# Relier les points avec une ligne
ax.plot(x, y, z, linestyle='-')

# Afficher la figure
plt.show()
