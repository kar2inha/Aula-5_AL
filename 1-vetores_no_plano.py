import numpy as np
import matplotlib.pyplot as plt

# Captura dos valores do vetor u
print("Digite os valores do vetor u:")
u1 = float(input("u1 = "))
u2 = float(input("u2 = "))

# Captura dos valores do vetor v
print("Digite os valores do vetor v:")
v1 = float(input("v1 = "))
v2 = float(input("v2 = "))

# Criação dos vetores u e v
u = np.array([u1, u2])
v = np.array([v1, v2])

# Produto escalar
produto = np.dot(u, v)

print(f"\nProduto escalar de u e v: {produto}")

# Verificação de ortogonalidade
if produto == 0:
    print("Movimento seguro: vetores ortogonais.")

    plt.figure()

    # Vetor u
    plt.quiver(0, 0, u[0], u[1], angles='xy', scale_units='xy', scale=1)

    # Vetor v
    plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1)    

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Vetores u e v - Verificando Ortogonalidade')

    plt.show()
else:
    print("Movimento não seguro: vetores não ortogonais.")