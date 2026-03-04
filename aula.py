import numpy as np
import matplotlib.pyplot as plt

# Definir pontos A, B, e C
A = np.array([0, 0])
B = np.array([5, 10])
C = np.array([10, 5])

# Calcular vetores de deslocamento
AB = B - A
BC = C - B# Com NumPy, você pode facilmente calcular:
# Vetores de deslocamento:
# Calcular ditâncias
dist_AB = np.linalg.norm(AB)
dist_BC = np.linalg.norm(BC)

#Ângulo entre vetores:
# Calcular ângulo entre os vetores
cos_theta = np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC))

# Converte de graus p/ radianos
angle_rad = np.arccos(cos_theta)
angle_deg = np.degrees(angle_rad)

# Criar gráfico
plt.figure(figsize=(8, 6))