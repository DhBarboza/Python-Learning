#Faça uma função pot(x, n) que faz x elevando a n, onde x é float e n um inteiro positivo
#Faça recursivamente não usando **

def pot(x, n):
    if n == 0: return 1
    return x * pot(x, n-1)
