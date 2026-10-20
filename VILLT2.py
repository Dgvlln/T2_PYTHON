def imprime(mat):
    for x in mat:
        print(x)
    print()

def valido(lab, res, f, c):
    if f >= len(lab):
        return False
    if f < 0:
        return False
    if c >= len(lab[0]):
        return False
    if c < 0:
        return False
    if res[f][c] == 1:
        return False
    if lab[f][c] == 0:
        return False
    return True

def laberB(lab, res, f, c, puntos):
    if f == 0 and c == 0:
        if valido(lab, res, f, c):
            res[f][c] = 1
            print("Puntos acumulados al llegar a F:", puntos)
            imprime(res)
            
            if puntos >= 23:
                return True
            else:
                res[f][c] = 0
                return False
        else:
            return False
    else:
        if valido(lab, res, f, c):
            ganancia = 0
            if lab[f][c] == 3 or lab[f][c] == 4:
                ganancia = lab[f][c]
            
            puntos += ganancia
            res[f][c] = 1
            print("Puntos actuales:", puntos)
            imprime(res)
            
            if laberB(lab, res, f-1, c, puntos):
                return True
            elif laberB(lab, res, f, c+1, puntos):
                return True
            elif laberB(lab, res, f+1, c, puntos):
                return True
            elif laberB(lab, res, f, c-1, puntos):
                return True
            else:
                puntos -= ganancia
                res[f][c] = 0
                return False
        else:
            return False

lab = [
    [1, 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    [1, 1, 3, 1, 0, 1, 1, 1, 1]  
]

res = [[0 for _ in range(9)] for _ in range(9)]

print("- LABERINTO ORIGINAL -")
imprime(lab)

print("- PROCESO DE BÚSQUEDA BACKTRACKING -")
if laberB(lab, res, 8, 0, 0):
    print("Salimos sumando los puntos que se necesitan")
    print("-MATRIZ DE SOLUCIÓN -")
    imprime(res)
else:
    print("Quedamos atrapados o no se alcanzaron los 23 puntos mínimos")
    print("-MATRIZ FINAL INTENTADA -")
    imprime(res)