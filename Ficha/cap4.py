# Capitulo 4 - Instruções Destrutivas
import math


# Exercicio 4.12
def potencia2_var(ni, nf):
    print("Número\tQuadrado")
    for i in range(ni, nf):
        print(str(i) + "\t\t" + str(i**2))


# Exercicio 4.14
def tabuada(num):
    print("Tabuada do número", num)
    print("--------------------")
    for i in range(1, 11):
        print(str(num) + "\tx\t" + str(i) + "\t=\t" + str(num*i))


# Exercicio 4.15
def acronimo(cadeia):
    lista_cadeia = cadeia.split()
    n_cadeia = ''
    for i in range(len(lista_cadeia)):
        n_cadeia += lista_cadeia[i][0]
    print(n_cadeia)


# Exercicio 4.19
def pos_matriz(lista):
    n_cadeia = ''
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            n_cadeia += "(" + str(i) + "," + str(j) + "): " + str(lista[i][j]) + "\t"
        n_cadeia += '\n'
    print(n_cadeia)


# Exercicio 4.20
def populacao_ano(p_inicial, n_anos):
    nasc = int(input("Frequência de nascimentos (minutos): "))
    morte = int(input("Frequência de falecimentos (minutos): "))
    emigracao = int(input("Frequencia de emigração (minutos): "))
    print("Resumo dos dados:")
    print("-----------------")
    print("Frequência de nascimentos:", nasc)
    print("Frequência de mortes:", morte)
    print("Frequência de emigrantes:", emigracao)
    print("População Inicial:", p_inicial)
    print("Estimativa:")
    print("-----------")
    ano_min = n_anos * 365 * 1440
    nasc_ano = ano_min / nasc
    morte_ano = ano_min / morte
    emigracao_ano = ano_min / emigracao
    p_final = p_inicial + nasc_ano - morte_ano - emigracao_ano
    print("A população ao fim de um ano:", int(p_final))


# Exercicio 4.13
def mile2km(v_i, v_f):
    print("Milhas\tQuilómetros")
    print("---------------------------")
    for i in range(v_i, v_f+1):
        i = float(i)
        km = float(format(i * 1.609, '.2f'))
        print(str("{:.2f}".format(i)) + "\t" + str("{:.2f}".format(km)))


# Exercicio 4.16
def descolagem():
    v = float(input("Velocidade de descolagem (m/s): "))
    a = float(input("Aceleração para descolagem (m/s): "))
    c = (v**2) / (2*a)
    print("Para a velocidade " + "{:.2f}".format(v) + " e aceleração " + "{:.2f}".format(a) + " o comprimento minimo da pista é: " + "{:.2f}".format(c))


# Exercicio 4.17
def energia():
    ti = float(input("Temperatura inicial (Celsius): "))
    tf = float(input("Temperatura final (Celcius): "))
    m = float(input("Quantidade de água (Quilogramas): "))
    E = math.fabs(m * (ti - tf) * 4184)
    print("Para a massa de água " + "{:.2f}".format(m) + ", temperatura inicial " + "{:.2f}".format(ti) + " e temperatura final " + "{:.2f}".format(tf) + " a energia necessária é: " + "{:.2f}".format(E) + " Joules.")


# Exercicio 4.18
def temperatura():
    v = float(input("Velocidade do vento (milhas/hora): "))
    t = float(input("Temperatura (Fahrenheit [-58, 41]): "))
    if t > 41 or t < -58:
        print("Erro: temperatura tem de estar entre -58 e 41")
    tv = 35.4 + 0.6215 * t - 35.75 * math.pow(v, 0.16) + 0.4275 * t * math.pow(v, 0.16)
    print("Para a velocidade do vento " + "{:.2f}".format(v) + " e temperatura exterior " + "{:.2f}".format(t) + " a temperatura é sentida como: " + "{:.2f}".format(tv))


if __name__ == '__main__':
    # potencia2_var(1, 5)
    # tabuada(7)
    # acronimo('Random Access Memory')
    # pos_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    # populacao_ano(10000000, 1)
    # mile2km(10, 20)
    # descolagem()
    energia()
    # temperatura()
