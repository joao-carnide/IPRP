# Capitulo 1 - Introdução
import math


def peso_ideal():
    genero = input("Qual o seu género (m/f)?\n>>> ")
    if genero == 'm':
        altura = float(input("Qual a sua altura (em metros)?\n>>> "))
        peso = (72.7 * altura) - 58
        print("O seu peso ideal é", peso)
    elif genero == 'f':
        altura = float(input("Qual a sua altura (em metros)?\n>>> "))
        peso = (62.1 * altura) - 44.7
        print("O seu peso ideal é", peso)
    else:
        peso_ideal()


# Exercicio 1.3
def anoluz_km():
    dist_al = float(input("Qual a distancia em ano-luz?\n>>> "))
    dist_km = dist_al * (9.459*(10**12))
    print("Valor em kilometros = ", dist_km)


# Exercicio 1.4
def segs():
    anos = float(input("Quantos anos?\n>>> "))
    segundos = anos * 365 * 24 * 60 * 60
    print("Equivalente a:", segundos)


# Exercicio 1.7
def area_triangulo():
    base = float(input("base = "))
    altura = float(input("altura = "))
    area = (base * altura)/2
    print("Area do triangulo = ", area)


# Exercicio 1.8
def hamburger():
    tam_novo = float(input("Qual o tamanho novo do hamburger?\n>>> "))
    tam_velho = float(input("Qual o tamanho velho do hamburger?\n>>> "))
    area_novo = tam_novo * 2
    area_velho = math.pi * (tam_velho**2)
    if area_novo < area_velho:
        print("Deve reclamar")
    else:
        print("Não é necessário reclamar")


# Exercicio 1.9
def imc():
    peso = float(input("Introduza o seu peso (em kg)\n>>> "))
    altura = float(input("Introduza a sua altura (em m)\n>>> "))
    imc = peso / (altura**2)
    print("O seu Indice de Mssa Corporal é: ", imc)


# Exercicio 1.10
def celsius_fahrenheit():
    temp_c = float(input("Introduza uma temperatura em Celsius\n>>> "))
    temp_f = (9/5) * temp_c + 32
    print("Temperatura em Fahrenheit: ", temp_f)


# Exercicio 1.11
def volume_cone():
    r = float(input("Raio = "))
    h = float(input("Altura = "))
    v = (math.pi * r**2 * h)/3
    print("Volume = ", v)


# Exercicio 1.12
def polinomio():
    print("Equação: x^4 + x^3 + 2x^2 - x")
    x = float(input("x = "))
    eq = x**4 + x**3 + 2*x**2 - x
    print("Resultado: ", eq)


# Exercicio 1.14
def euro2dollar():
    guito = float(input("Qual o valor (em euros) que prentende converter para dolares?\n>>> "))
    dollar = guito * 1.17581
    print("Irá obter aproximadamente (em dolares): ", dollar)


# Exercicio 1.15
def garrafas():
    agua = float(input("Qual a quantidade de agua que pretende?\n>>> "))
    garrafa5 = int(agua // 5)
    agua = garrafa5 % 5
    garrafa1_5 = int(agua // 1.5)
    agua = garrafa1_5 % 1.5
    garrafa0_5 = int(agua // 0.5)
    agua = garrafa0_5 % 0.5
    garrafa0_25 = math.ceil(agua / 0.25)
    return garrafa5 + garrafa1_5 + garrafa0_5 + garrafa0_25


# Exercicio 1.17
def pol2cart():
    r = float(input("Coordenadas polares\nr = "))
    teta = float(input("teta = "))
    x = r * math.cos(teta)
    y = r * math.sin(teta)
    print("Coordenadas cartesianas:\n", (x, y))


def cart2pol():
    x = float(input("Coordenadas cartesianas\nx = "))
    y = float(input("y = "))
    r = math.sqrt(x**2 + y**2)
    teta = math.asin(y/x)
    print("Coordenadas polares:\n", (r, teta))


# Exercicio 1.18
def orbita():
    distancia = float(input("distancia = "))
    p = math.sqrt(distancia**3)
    print(p)


# Exercicio 1.19
def kepler(m1, m2, a):
    G = 6.67e-11
    p = math.sqrt((4 * math.pow(math.pi, 2) / (G * (m1 + m2)) * math.pow(a, 3)))
    print(p)


if __name__ == '__main__':
    # peso_ideal()
    # anoluz_km()
    # segs()
    # area_triangulo()
    # imc()
    hamburger()
    # celsius_fahrenheit()
    # volume_cone()
    # polinomio()
    # euro2dollar()
    # print(garrafas())
    # pol2cart()
    # cart2pol()
    # orbita()
    # kepler(1.2e30, 2.2e21, 400)
