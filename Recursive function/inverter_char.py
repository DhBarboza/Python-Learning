#Faça uma Função recursiva que inverta uma string s.

def  inverter(tex):
    if len(tex) == 0: return tex
    return inverter(tex[1:]) + s[0]
