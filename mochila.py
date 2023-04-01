class Object:

    def __init__(self, valor, peso):
        self.valor = valor
        self.peso = peso

objetos = [
    
    Object(1, 7),
    Object(3, 6),
    Object(6, 3),
    Object(5, 3),
    Object(4, 5),
    Object(7, 4),
    Object(8, 1),
    Object(1, 1),
    Object(5, 5)
    
]

capacidad = 10

def greedy1(objetos, capacidad):
    objetos_or = sorted(objetos, key=lambda obj: obj.peso)
    mochila = []
    peso_actual = 0
    for obj in objetos_or:
      
        if peso_actual + obj.peso <= capacidad:
            mochila.append(obj)
            peso_actual += obj.peso
    return mochila

def greedy2(objetos, capacidad):
    objetos_or = sorted(objetos, key=lambda obj: obj.valor, reverse=True)
    mochila = []
    peso_actual = 0
    for obj in objetos_or:
        if peso_actual + obj.peso <= capacidad:
            mochila.append(obj)
            peso_actual += obj.peso
    return mochila

def greedy3(objetos, capacidad):
    objetos_or = sorted(objetos, key=lambda obj: obj.valor / obj.peso, reverse=True)
    mochila = []
    peso_actual = 0
    for obj in objetos_or:
        if peso_actual + obj.peso <= capacidad:
            mochila.append(obj)
            peso_actual += obj.peso
    return mochila

def dp(objetos, capacidad):
     
    K = [[0 for _ in range(capacidad + 1)] for _ in range(len(objetos) + 1)]

    for i in range(1, len(objetos) + 1):
        for j in range(1, capacidad + 1):
            if objetos[i-1].peso > j:
                K[i][j] = K[i-1][j]
            else:
                K[i][j] = max(K[i-1][j], K[i-1][j-objetos[i-1].peso] + objetos[i-1].valor)

    seleccionados = []
    i = len(objetos)
    j = capacidad
    while i > 0 and j > 0:
        if K[i][j] != K[i-1][j]:
            seleccionados.append(objetos[i-1])
            j -= objetos[i-1].peso
        i -= 1

    return seleccionados[::-1]

mo_greedy1 = greedy1(objetos, capacidad)
mo_greedy2 = greedy2(objetos, capacidad)
mo_greedy3 = greedy3(objetos, capacidad)
mo_dp = dp(objetos, capacidad)

print("Objetos elegidos para entrar a la mochila con greedy 1: ", [(obj.valor, obj.peso) for obj in mo_greedy1])
print("Objetos elegidos para entrar a la mochila con greedy 2: ", [(obj.valor, obj.peso) for obj in mo_greedy2])
print("Objetos elegidos para entrar a la mochila con greedy 3: ", [(obj.valor, obj.peso) for obj in mo_greedy3])
print("Objetos elegidos para entrar a la mochila con DP: ", [(obj.valor, obj.peso) for obj in mo_dp])