#Faça uma Função Recursiva que calcule o mdc de dois inteiros a e b.

def mdc(a, b):
    if b == 0: return a
    return mdc(b, a % b)

