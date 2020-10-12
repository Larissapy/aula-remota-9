def celsius(t1):
    C = (t1 - 32) * (5 / 9)
    return C

def identicandor(t1, e1, t2, e2):
        if e1 == 'C':
            x = t1
            if e2 == 'F':
                y = celsius(t2)
            elif e2 == 'C':
                y = t2
        elif e1 == 'F':
            x = celsius(t1)
            if e2 == 'F':
                y = celsius(t2)
            elif e2 == 'C':
                y = t2
        return x, y

def main():
    temperatura_1 = float(input())
    escala_1 = input().upper()[0]
    tupla_1 = (temperatura_1, escala_1)
    temperatura_2 = float(input())
    escala_2 = input().upper()[0]
    tupla_2 = (temperatura_2, escala_2)

    r1, r2 = identicandor(temperatura_1, escala_1, temperatura_2, escala_2)

    if r1 > r2:
        maior_t1 = tupla_1
        print(maior_t1)
    elif r2 > r1:
        maior_t2= tupla_2
        print(maior_t2)

if __name__ == "__main__":
    main()