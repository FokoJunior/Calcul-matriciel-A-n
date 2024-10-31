import numpy as np

A = np.array([
    [0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
])

def calculer_puissances(matrice, puissances):
    
       for p in puissances:
        resultat = np.linalg.matrix_power(matrice, p)
        print(f"A^{p}:\n{resultat}\n")


puissances_a_calculer = [2, 3, 4, 5, 6]


calculer_puissances(A, puissances_a_calculer)

