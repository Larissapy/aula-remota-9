def criar_matriz():
    matriz = []

    for a in range(4):
        ano = []
        for l in range(12):
            linha = []
            for c in range(3):
                num = int(input())
                linha.append(num)
            ano.append(linha)
        matriz.append(ano)
    return matriz

def mes():
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
             'Novembro', 'Dezembro']
    return meses

def total_ano_2014_por_filial(matriz):
    filial_1 = []

    for l in range(12):
        filial_1.append(matriz[0][l][0])
    total_filial_1_2014 = 0
    for num in filial_1:
        total_filial_1_2014 += num
    filial_2 = []

    for l in range(12):
        filial_2.append(matriz[0][l][1])
    total_filial_2_2014 = 0
    for num in filial_2:
        total_filial_2_2014 += num
    filial_3 = []

    for l in range(12):
        filial_3.append(matriz[0][l][2])
    total_filial_3_2014 = 0
    for num in filial_3:
        total_filial_3_2014 += num

    return total_filial_1_2014, total_filial_2_2014, total_filial_3_2014

def total_ano_2015_por_filial(matriz):
    filial_1 = []

    for l in range(12):
        filial_1.append(matriz[1][l][0])
    total_filial_1_2015 = 0
    for num in filial_1:
        total_filial_1_2015 += num
    filial_2 = []

    for l in range(12):
        filial_2.append(matriz[1][l][1])
    total_filial_2_2015 = 0
    for num in filial_2:
        total_filial_2_2015 += num
    filial_3 = []

    for l in range(12):
        filial_3.append(matriz[1][l][2])
    total_filial_3_2015 = 0
    for num in filial_3:
        total_filial_3_2015 += num

    return total_filial_1_2015, total_filial_2_2015, total_filial_3_2015


def total_ano_2016_por_filial(matriz):
    filial_1 = []

    for l in range(12):
        filial_1.append(matriz[2][l][0])
    total_filial_1_2016 = 0
    for num in filial_1:
        total_filial_1_2016 += num
    filial_2 = []

    for l in range(12):
        filial_2.append(matriz[2][l][1])
    total_filial_2_2016 = 0
    for num in filial_2:
        total_filial_2_2016 += num
    filial_3 = []

    for l in range(12):
        filial_3.append(matriz[2][l][2])
    total_filial_3_2016 = 0
    for num in filial_3:
        total_filial_3_2016 += num

    return total_filial_1_2016, total_filial_2_2016, total_filial_3_2016


def total_ano_2017_por_filial(matriz):
    filial_1 = []

    for l in range(12):
        filial_1.append(matriz[3][l][0])
    total_filial_1_2017 = 0
    for num in filial_1:
        total_filial_1_2017 += num
    filial_2 = []

    for l in range(12):
        filial_2.append(matriz[3][l][1])
    total_filial_2_2017 = 0
    for num in filial_2:
        total_filial_2_2017 += num
    filial_3 = []

    for l in range(12):
        filial_3.append(matriz[3][l][2])
    total_filial_3_2017 = 0
    for num in filial_3:
        total_filial_3_2017 += num

    return total_filial_1_2017, total_filial_2_2017, total_filial_3_2017


def total_ano_2014_todas_filiais(matriz):
    total_filial_1_2014, total_filial_2_2014, total_filial_3_2014 = total_ano_2014_por_filial(matriz)

    total_2014 = total_filial_1_2014 + total_filial_2_2014 + total_filial_3_2014

    return total_2014

def total_ano_2015_todas_filiais(matriz):
    total_filial_1_2015, total_filial_2_2015, total_filial_3_2015 = total_ano_2015_por_filial(matriz)

    total_2015 = total_filial_1_2015 + total_filial_2_2015 + total_filial_3_2015

    return total_2015

def total_ano_2016_todas_filiais(matriz):
    total_filial_1_2016, total_filial_2_2016, total_filial_3_2016 = total_ano_2016_por_filial(matriz)

    total_2016 = total_filial_1_2016 + total_filial_2_2016 + total_filial_3_2016

    return total_2016

def total_ano_2017_todas_filiais(matriz):
    total_filial_1_2017, total_filial_2_2017, total_filial_3_2017 = total_ano_2017_por_filial(matriz)

    total_2017 = total_filial_1_2017 + total_filial_2_2017 + total_filial_3_2017

    return total_2017

def total_todos_anos(matriz):
    total_2014 = total_ano_2014_todas_filiais(matriz)
    total_2015 = total_ano_2015_todas_filiais(matriz)
    total_2016 = total_ano_2016_todas_filiais(matriz)
    total_2017 = total_ano_2017_todas_filiais(matriz)
    total = total_2014 + total_2015 + total_2016 + total_2017

    return total

def imprimir_2014():
    matriz = criar_matriz()

    meses = mes()
    total_filial_1_2014, total_filial_2_2014, total_filial_3_2014 = total_ano_2014_por_filial(matriz)

    for i in range(12):
        m = meses[i]
        print(f'2014; Filial 1; {m}; {matriz[0][i][0]}')

    print(f'TOTAL 2014 FILIAL 1; {total_filial_1_2014}')
    print()

    for i in range(12):
        m = meses[i]
        print(f'2014; Filial 2; {m}; {matriz[0][i][1]}')

    print(f'TOTAL 2014 FILIAL 2; {total_filial_2_2014}')
    print()

    for i in range(12):
        m = meses[i]
        print(f'2014; Filial 3; {m}; {matriz[0][i][2]}')

    print(f'TOTAL 2014 FILIAL 3; {total_filial_3_2014}')
    print()

    total_2014 = total_ano_2014_todas_filiais(matriz)
    print(f'TOTAL 2014 TODAS FILIAIS; {total_2014}')
    print()


def imprimir_2015():
    matriz = criar_matriz()

    meses = mes()
    total_filial_1_2015, total_filial_2_2015, total_filial_3_2015 = total_ano_2015_por_filial(matriz)

    for i in range(12):
        m = meses[i]
        print(f'2015; Filial 1; {m}; {matriz[1][i][0]}')

    print(f'TOTAL 2015 FILIAL 1; {total_filial_1_2015}')
    print()

    for i in range(12):
        m = meses[i]
        print(f'2015; Filial 2; {m}; {matriz[1][i][1]}')

    print(f'TOTAL 2015 FILIAL 2; {total_filial_2_2015}')
    print()

    for i in range(12):
        m = meses[i]
        print(f'2015; Filial 3; {m}; {matriz[1][i][2]}')

    print(f'TOTAL 2015 FILIAL 3; {total_filial_3_2015}')
    print()

    total_2015 = total_ano_2015_todas_filiais(matriz)
    print(f'TOTAL 2015 TODAS FILIAIS; {total_2015}')
    print()


def imprimir_2016():
    matriz = criar_matriz()

    meses = mes()
    total_filial_1_2016, total_filial_2_2016, total_filial_3_2016 = total_ano_2016_por_filial(matriz)

    for i in range(12):
        m = meses[i]
        print(f'2016; Filial 1; {m}; {matriz[2][i][0]}')

    print(f'TOTAL 2016 FILIAL 1; {total_filial_1_2016}')
    print()

    for i in range(12):
        m = meses[i]
        print(f'2016; Filial 2; {m}; {matriz[2][i][1]}')

    print(f'TOTAL 2016 FILIAL 2; {total_filial_2_2016}')
    print()

    for i in range(12):
        m = meses[i]
        print(f'2016; Filial 3; {m}; {matriz[2][i][2]}')

    print(f'TOTAL 2016 FILIAL 3; {total_filial_3_2016}')
    print()

    total_2016 = total_ano_2016_todas_filiais(matriz)
    print(f'TOTAL 2016 TODAS FILIAIS; {total_2016}')
    print()


def imprimir_2017():
    matriz = criar_matriz()

    meses = mes()
    total_filial_1_2017, total_filial_2_2017, total_filial_3_2017 = total_ano_2017_por_filial(matriz)

    for i in range(12):
        m = meses[i]
        print(f'2017; Filial 1; {m}; {matriz[3][i][0]}')

    print(f'TOTAL 2017 FILIAL 1; {total_filial_1_2017}')
    print()

    for i in range(12):
        m = meses[i]
        print(f'2017; Filial 2; {m}; {matriz[3][i][1]}')

    print(f'TOTAL 2017 FILIAL 2; {total_filial_2_2017}')
    print()

    for i in range(12):
        m = meses[i]
        print(f'2017; Filial 3; {m}; {matriz[3][i][2]}')

    print(f'TOTAL 2017 FILIAL 3; {total_filial_3_2017}')
    print()

    total_2017 = total_ano_2017_todas_filiais(matriz)
    print(f'TOTAL 2017 TODAS FILIAIS; {total_2017}')
    print()


def main():
    matriz = criar_matriz()

    imprimir_2014()
    imprimir_2015()
    imprimir_2016()
    imprimir_2017()

    total = total_todos_anos(matriz)
    print(f'TOTAL PERÍODO TODAS FILIAIS; {total}')

if __name__ == "__main__":
    main()