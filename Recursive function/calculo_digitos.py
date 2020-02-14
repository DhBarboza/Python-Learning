#Faça uma Função recursiva que calcule a soma dos digitos de um inteiro positivo n

def sd(n):
    if n <= 9: return n
    return n % 10 + sd(n//10)
