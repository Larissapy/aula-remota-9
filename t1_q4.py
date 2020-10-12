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

def main():
    pop = int(input())

    informacoes = carrega_cidades()

    print(f'CIDADES COM MAIS DE {pop} HABITANTES:')
    for dado in informacoes:
        if dado[5] > pop:
            ibge = dado[1]
            nome = dado[2]
            uf = dado[0]
            print(f'IBGE: {ibge} - {nome}({uf}) - POPULAÇÃO: {dado[5]}')

if __name__ == '__main__':
    main()