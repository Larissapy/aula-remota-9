def fahrenheit_kelvin(t):
    F_K = round((t - 32) * (5 / 9) + 273.15, 2)
    return F_K

def celsius_kelvin(t):
    C_K = round(t + 273.15, 2)
    return C_K

def conversao(matriz):
    convertidos = []

    for l in range(12):
        t = matriz[l][0]
        g = matriz[l][1]

        if g == 'F':
            t = fahrenheit_kelvin(t)
        elif g == 'C':
            t = celsius_kelvin(t)
        elif g == 'K':
            t = t
        convertidos.append(t)
    return convertidos

def media_temperatura(convertidos):
    soma = 0
    for i in convertidos:
        soma += i

    media = soma / 12
    media = round(media, 2)

    return media

def maiores(convertidos):
    media = media_temperatura(convertidos)
    maior = []
    i = 1
    for m in convertidos:
        if m > media:
            maior.append(m)
        i += 1
    return maior

def mes_extenso(i):
    if i == 1:
        return 'Janeiro'
    if i == 2:
        return 'Fevereiro'
    if i == 3:
        return 'Março'
    if i == 4:
        return 'Abril'
    if i == 5:
        return 'Maio'
    if i == 6:
        return 'Junho'
    if i == 7:
        return 'Julho'
    if i == 8:
        return 'Agosto'
    if i == 9:
        return 'Setembro'
    if i == 10:
        return 'Outubro'
    if i == 11:
        return 'Novembro'
    if i == 12:
        return 'Dezembro'
def main():
    matriz = []

    for l in range(12):
        linha = []

        for c in range(1):
            temp = float(input())
            grau = input().strip().upper()
            linha.append(temp)
            linha.append(grau)

        matriz.append(linha)

    convertidos = conversao(matriz)

    print('TEMPERATURA MÉDIA ANUAL')
    media = media_temperatura(convertidos)
    print('{}K'.format(media))

    print('TEMPERATURAS ACIMA DA MÉDIA ANUAL:')
    i = 1
    for m in convertidos:
        if m > media:
            print(f'{mes_extenso(i)}: {m}K')

        i += 1
if __name__ == '__main__':
    main()
