def criar_matriz(n):
    matriz = []

    for l in range(n):
        linha = []
        for c in range(n):
            num = int(input())
            linha.append(num)
        matriz.append(linha)
    return matriz

def maior_elemento(matriz, n):
    maior = matriz[0][0]
    linha = 0
    coluna = 0

    for l in range(n):
        for c in range(n):
            if matriz[l][c] > maior:
                maior = matriz[l][c]
                linha = l
                coluna = c
    return maior, linha, coluna

def menor_elemento(matriz, n):
    menor = matriz[0][0]
    linha = 0
    coluna = 0
    for l in range(n):
        for c in range(n):
            if matriz[l][c] < menor:
                menor = matriz[l][c]
                linha = l
                coluna = c
    return menor, linha, coluna

def main():
    n = int(input())

    matriz = criar_matriz(n)

    maior, l_maior, c_maior = maior_elemento(matriz, n)
    tupla_maior = l_maior, c_maior

    print(tuple(tupla_maior))

    menor, l_menor, c_menor = menor_elemento(matriz, n)
    tupla_menor = l_menor, c_menor

    print(tuple(tupla_menor))

if __name__ == "__main__":
    main()