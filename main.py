import numpy as np

def solver(A, B, C):
    delta = B**2 - 4*A*C

    if delta > 0:
        root1 = (-B + np.sqrt(delta)) / (2*A)
        root2 = (-B - np.sqrt(delta)) / (2*A)
        return root1, root2
    elif delta == 0:
        root = -B / (2*A)
        return root,
    else:
        print("Il n'existe aucune solution pour cette equation")

# Get user input for coefficients
A = float(input("Entrer la valeur de A: "))
B = float(input("Entrer la valeur de B: "))
C = float(input("Entrer la valeur de C: "))

roots = solver(A, B, C)
print("Solutions:", roots)
