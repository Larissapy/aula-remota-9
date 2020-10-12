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
    mes = int(input())
    pop = int(input())

    informacoes = carrega_cidades()

    m_e = mes_extenso(mes)
    print(f'CIDADES COM MAIS DE {pop} HABITANTES E ANIVERSÁRIO EM {m_e}:')
    for dado in informacoes:
        if dado[5] > pop and dado[4] == mes:
            nome = dado[2]
            uf = dado[0]
            dia = dado[3]
            print(f'{nome}({uf}) tem {dado[5]} habitantes e faz aniversário em {dia} de {m_e.lower()}.')

if __name__ == '__main__':
    main()

