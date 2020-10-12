def carrega_cidades():
    informacoes = []

    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            informacoes.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()

    informacoes = tuple(informacoes)
    return informacoes

def mes_extenso(mes):
    if mes == 1:
        return 'JANEIRO'
    if mes == 2:
        return 'FEVEREIRO'
    if mes == 3:
        return 'MARÇO'
    if mes == 4:
        return 'ABRIL'
    if mes == 5:
        return 'MAIO'
    if mes == 6:
        return 'JUNHO'
    if mes == 7:
        return 'JULHO'
    if mes == 8:
        return 'AGOSTO'
    if mes == 9:
        return 'SETEMBRO'
    if mes == 10:
        return 'OUTUBRO'
    if mes == 11:
        return 'NOVEMBRO'
    if mes == 12:
        return 'DEZEMBRO'

def main():
    dia = int(input())
    mes = int(input())

    informacoes = carrega_cidades()

    m = mes_extenso(mes)
    print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {mes}:')
    for dado in informacoes:
        if dado[3] == dia and dado[4] == mes:
            nome = dado[2]
            uf = dado[0]
            print(f'{nome}({uf})')

if __name__ == "__main__":
    main()