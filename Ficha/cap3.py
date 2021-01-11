# Capítulo 3 - Objetos (I)
import math
import random
import turtle


# Exercicio 3.2
def heron(a, b, c):
    if a < 1 or b < 1 or c < 1:
        print("não possivel calcular a area")
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print("area =", round(area, 2))


# Exercicio 3.3
def escada(alt, ang_graus):
    ang_rad = (math.pi/180) * ang_graus
    comp = alt/math.sin(ang_rad)
    print("comp =", round(comp, 2))


# Exercicio 3.4
def batimento(idade):
    if idade <= 0:
        print("Idade inválida")
    bat = 163 + 1.16 * idade - 0.018 * math.pow(idade, 2)
    print("batimento =", round(bat, 2))


# Exercicio 3.5
def render(v, t_perc, a):
    t_dec = t_perc / 100
    valor = v * math.pow(1 + t_dec, a)
    print("valor =", round(valor, 2))


# Exercicio 3.7
def objetos(n, m):
    if n == 0 or m == 0:
        return 0
    p1 = n / (n + m)
    p2 = m / (n + m)
    soma = 0
    p = [p1, p2]
    for i in range(len(p)):
        soma += p[i] * math.log2(p[i])
    H = -soma
    print("H(p1,p2) =", H)


# Exercicio 3.11
def dna(cadeia):
    complementar = ''
    for i in range(len(cadeia)):
        if cadeia[i] == 'A':
            complementar += 'T'
        elif cadeia[i] == 'T':
            complementar += 'A'
        elif cadeia[i] == 'C':
            complementar += 'G'
        elif cadeia[i] == 'G':
            complementar += 'C'
        else:
            print("Cadeia Inválida")
    print(complementar)


# Exercicio 3.12
def gerar_cadeia(comp):
    cadeia = ''
    for i in range(comp):
        cadeia += random.choice('ACGT')
    print(cadeia)


# Exercicio 3.13
def subs_vogais(cadeia):
    vogais = 'aeiou'
    n_cadeia = ''
    for i in range(len(cadeia)):
        if cadeia[i] in vogais:
            n_cadeia += ' '
        else:
            n_cadeia += cadeia[i]
    print(n_cadeia)


# Exercicio 3.14
def subcadeia(cadeia, comp):
    for i in range(len(cadeia)-comp+1):
        print(cadeia[i:i+comp])


# Exercicio 3.15
def prefixo(cadeia):
    for i in range(len(cadeia)):
        print(cadeia[:i+1])


# Exercicio 3.16
def sufixo(cadeia):
    for i in range(len(cadeia), -1, -1):
        print(cadeia[i:])


# Exercicio 3.17
def simulador(cadeia, lado, ang):
    for i in range(len(cadeia)):
        if cadeia[i] == 'f':
            turtle.forward(lado)
        elif cadeia[i] == 'e':
            turtle.left(ang)
        elif cadeia[i] == 't':
            turtle.back(lado)
        elif cadeia[i] == 'd':
            turtle.right(ang)
        else:
            print("Cadeia inválida")
    turtle.hideturtle()
    turtle.exitonclick()


# Exercicio 3.18
def simulador_random(cadeia):
    for i in range(len(cadeia)):
        lado = random.randint(0, 200)
        ang = random.randint(0, 180)
        if cadeia[i] == 'f':
            turtle.forward(lado)
        elif cadeia[i] == 'e':
            turtle.left(ang)
        elif cadeia[i] == 't':
            turtle.back(lado)
        elif cadeia[i] == 'd':
            turtle.right(ang)
        else:
            print("Cadeia inválida")
    turtle.hideturtle()
    turtle.exitonclick()


# Exercicio 3.19
def sim_cad_random(comp):
    cadeia = ''
    for i in range(comp):
        cadeia += random.choice('fetd')
    print("Cadeia gerada: ", cadeia)
    simulador_random(cadeia)


# Exercicio 3.20
def codificar(cadeia, valor):
    n_cadeia = ''
    alfabeto_min = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_mai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for car in cadeia:
        if car in alfabeto_min:
            nova_pos = (alfabeto_min.index(car) + valor) % len(alfabeto_min)
            n_car = alfabeto_min[nova_pos]
        elif car in alfabeto_mai:
            nova_pos = (alfabeto_mai.index(car) + valor) % len(alfabeto_mai)
            n_car = alfabeto_mai[nova_pos]
        else:
            print("caracter '" + car + "' não existe, será transformado em '-'")
            n_car = '-'
        n_cadeia += n_car
    print("Cadeia codificada:", n_cadeia)

def descodificar(cadeia, valor):
    n_cadeia = ''
    alfabeto_min = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_mai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for car in cadeia:
        if car in alfabeto_min:
            nova_pos = (alfabeto_min.index(car) - valor) % len(alfabeto_min)
            n_car = alfabeto_min[nova_pos]
        elif car in alfabeto_mai:
            nova_pos = (alfabeto_mai.index(car) - valor) % len(alfabeto_mai)
            n_car = alfabeto_mai[nova_pos]
        else:
            print("caracter '" + car + "' não existe, será transformado em '-'")
            n_car = '-'
        n_cadeia += n_car
    print("Cadeia descodificada: ", n_cadeia)


if __name__ == '__main__':
    # heron(10, 5, 7.5)
    # escada(10, 60)
    # batimento(22)
    # render(300, 15, 2)
    # objetos(20, 80)
    # dna('AAGCTAGCTGACGTTAC')
    # gerar_cadeia(10)
    # subs_vogais('nao gosto de sopa')
    # subcadeia('Monty Python', 3)
    # prefixo('Monty_Python')
    # sufixo('Monty_Python')
    # simulador('feftd', 100, 60)
    # simulador_random('feftd')
    # sim_cad_random(10)
    codificar('Bom dia colega!', 5)
    descodificar('Gtr inf htqjlf', 5)
