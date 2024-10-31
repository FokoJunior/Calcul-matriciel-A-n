
taille = 6

A = [
    [0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

A2 = []
for i in range(taille):
        ligne = []
        for j in range(taille):
            ligne.append(0)
        A2.append(ligne)

A3 = []
for i in range(taille):
        ligne = []
        for j in range(taille):
            ligne.append(0)
        A3.append(ligne)

A4 = []
for i in range(taille):
        ligne = []
        for j in range(taille):
            ligne.append(0)
        A4.append(ligne)

A5 = []
for i in range(taille):
        ligne = []
        for j in range(taille):
            ligne.append(0)
        A5.append(ligne)

A6 = []
for i in range(taille):
        ligne = []
        for j in range(taille):
            ligne.append(0)
        A6.append(ligne)

A7 = []
for i in range(taille):
        ligne = []
        for j in range(taille):
            ligne.append(0)
        A7.append(ligne)


#A2
for i in range(taille):
        for j in range(taille):
            for k in range(taille):
                A2[i][j] = A2[i][j] + A[i][k] * A[k][j]

#A3
for i in range(taille):
        for j in range(taille):
            for k in range(taille):
                A3[i][j] = A3[i][j] + A2[i][k] * A[k][j]


#A4
for i in range(taille):
        for j in range(taille):
            for k in range(taille):
                A4[i][j] = A4[i][j] + A3[i][k] * A[k][j]


#A5
for i in range(taille):
        for j in range(taille):
            for k in range(taille):
                A5[i][j] = A5[i][j] + A4[i][k] * A[k][j]


#A6
for i in range(taille):
        for j in range(taille):
            for k in range(taille):
                A6[i][j] = A6[i][j] + A5[i][k] * A[k][j]

#A7
for i in range(taille):
        for j in range(taille):
            for k in range(taille):
                A7[i][j] = A7[i][j] + A6[i][k] * A[k][j]




print("\nLe resultat de A est:")
for resultat in A:
    print(resultat)
    

print("\nLe resultat de A^2 est:")
for resultat in A2:
    print(resultat)


print("\nLe resultat de A^3 est:")
for resultat in A3:
    print(resultat)


print("\nLe resultat de A^4 est:")
for resultat in A4:
    print(resultat)

print("\nLe resultat de A^5 est:")
for resultat in A5:
    print(resultat)

print("\nLe resultat de A^6 est:")
for resultat in A6:
    print(resultat)

print("\nLe resultat de A^7 est:")
for resultat in A7:
    print(resultat)

