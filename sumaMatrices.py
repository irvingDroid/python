import numpy as np

def tamanio():
    fil = int(input("Filas: "))
    col = int(input("Columnas: "))
    return fil, col

def tamanio2():
    fil = int(input("Filas: "))
    col = int(input("Columnas: "))
    return fil, col

def validacion(colA, filA, colB, filB):
    aux = int()
    if colA == colB and filA == filB:
        aux = 1
    else:
        aux = 0
    return aux

def matriz(filA, colA):
    for i in range(0,filA):
        for j in range(0,colA):
            aux[i][j] = int(input("Elemento" + str([i]) + str([j]) + ":" + " "))
    return aux
            
def suma(matrixA, matrixB, filA, colA):
    for i in range(0,filA):
        for j in range(0,colA):
            matrixC[i][j] = matrixA[i][j] + matrixB[i][j]
    return matrixC

def resta(matrixA, matrixB, filA, colA):
    for i in range(0,filA):
        for j in range(0,colA):
            matrixC[i][j] = matrixA[i][j] - matrixB[i][j]
    return matrixC
    

print("Suma/Resta matrices")
print("[1] Suma\n[2] Resta")
opcion = input("Opcion: ")
print("Matriz A:")
filA, colA = tamanio() 
print("Matriz B:")
filB, colB = tamanio2()
aux = np.eye(filA, colA)
valido = int()
valido = validacion(colA, filA, colB, filB)
if valido == 1:
    print("Valido")
    matrixA = np.eye(filA, colA)
    matrixB = np.eye(filA, colB)
    matrixC = np.eye(filA, colB)
    print("Matriz A: ")
    matrixA = matriz(filA, colB)
    print("Matriz B: ")
    matrixB = matriz(filB, colB)
    if opcion == '1':
        aux = suma(matrixA, matrixB, filA, colA)
        print("La suma es: ")
    elif opcion == '2':
        aux = resta(matrixA, matrixB, filA, colA)
        print("La resta es: ")
    print(aux)
else:
    print("Error")



