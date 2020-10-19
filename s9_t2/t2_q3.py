from random import *

def criar_matriz(linhas, colunas):
    matriz = []

    for c in range(colunas):
        coluna = []

        for l in range(linhas):
            num = int(input())
            coluna.append(num)
        matriz.append(coluna)
    return matriz


def elementos(matriz):
    todos_elementos = []

    for linha in matriz:
        for elemento in linha:
            todos_elementos.append(elemento)
    return todos_elementos

def soma_primeira_linha(matriz, linhas):
    todos_elementos = elementos(matriz)

    soma_linha = 0
    for c in range(linhas):
        soma_linha += todos_elementos[c]
    return soma_linha

def soma_ultima_coluna(matriz, colunas, linhas):
    todos_elementos = elementos(matriz)

    soma_coluna = 0

    for c in range(colunas - 1, linhas * colunas, colunas):
        soma_coluna += todos_elementos[c]
    return soma_coluna


def menor_elemento(matriz):
    todos_elementos = elementos(matriz)
    men = 1000000

    for elemento in todos_elementos:
        if elemento < men:
            men = elemento
    return men

def maior_elemento(matriz):
    todos_elementos = elementos(matriz)
    mai = 0

    for elemento in todos_elementos:
        if elemento > mai:
            mai = elemento
    return mai

def media_matriz(matriz, colunas, linhas):
    todos_elementos = elementos(matriz)
    soma = 0

    for e in todos_elementos:
        soma += e

    media = soma / (colunas * linhas)

    return round(media, 2)

def main():
    c = int(input())
    l = int(input())

    m = criar_matriz(l, c)
    soma_linha = soma_primeira_linha(m, l)
    soma_coluna = soma_ultima_coluna(m, l, c)
    media = media_matriz(m, l, c)
    menor = menor_elemento(m)
    maior = maior_elemento(m)


    tupla = soma_linha, soma_coluna, media, menor, maior
    print(tuple(tupla))

if __name__ == "__main__":
    main()