def celsius(t):
    C = (t - 32) * (5/9)
    return C

def fahrenheit(t):
    F = (t * (9/5)) + 32
    return F

def soma(primeira_t, segunda_t):
    s = primeira_t + segunda_t
    return round(s, 4)

def identicandor(t1, e1, t2, e2):
    if e1 == 'C':
        if e2 == 'C':
            e = 'C'
        elif e2 == 'F':
            t1 = fahrenheit(t1)
            e = 'F'
    elif e1 == 'F':
        if e2 == 'F':
            e = 'F'
        elif e2 == 'C':
            t1 = celsius(t1)
            e = 'C'

    s = soma(t1, t2)

    return s, e

def main():
    temperatura_1 = float(input())
    escala_1 = input().upper()[0]
    tupla_1 = (temperatura_1, escala_1)
    temperatura_2 = float(input())
    escala_2 = input().upper()[0]
    tupla_2 = (temperatura_2, escala_2)

    r1, r2 = identicandor(temperatura_1, escala_1, temperatura_2, escala_2)
    temperatura_s = (r1, r2)

    print(temperatura_s)

if __name__ == '__main__':
    main()