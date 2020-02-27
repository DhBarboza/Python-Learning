print ('Digite os três lados do triângulo')
a = int(input('Digite o primeiro lado: '))
b = int(input('Digite o segundo lado: '))
c = int(input('Digite o terceiro lado: '))
if (a + b) > c:
    print ('é um triângulo')
    if a == b == c:
        print ('equilátero')
    elif a == b != c or a != b == c or a == c != b:
        print ('isóceles')
    elif a != b != c:
        print ('escaleno')
    else:
        print ('Valores inválidos')
else:
    print ('Não é um Triângulo')
