# Capitulo 5 - Instruções de Controlo
import random
import turtle

# Exercicio 5.7
def amigas(pal1, pal2):
    conta = 0
    for i in range(len(pal1)):
        if pal1[i] != pal2[i]:
            conta += 1
    if len(pal1) * 0.1 > conta:
        print("As palavras são amigas")
    else:
        print("As palavars não são amigas")


# Exercicio 5.9
def numero_par(lancamentos):
    n_par = 0
    for i in range(lancamentos):
        dado = random.randint(1, 6)
        if dado % 2 == 0:
            n_par += 1
    perc = n_par / lancamentos
    print("Percentagem de vezes que saiu numero par:", perc)


# Exercicio 5.10
def monte_carlo(n_dardos):
    conta = 0
    for i in range(n_dardos):
        x = random.uniform(0, 2)
        y = random.uniform(0, 2)
        if x <= 1 and y >= 1 or x > 1 and y <= 1 or x > 1 and y >= 1 and y < x:
            conta += 1
    print(100*conta/n_dardos)


# Exercicio 5.15
def fatorial(n):
    fact = 1
    if n == 0:
        return fact
    else:
        for i in range(n):
            fact *= n - i
    return fact

def logaritmo(precisao):
    ordem = 0
    res = 0
    dif = 1
    while dif > precisao:
        termo = 1 / fatorial(ordem)
        res, ant = res + termo, res
        dif = abs(res - ant)
        ordem += 1
    print(res)


# Exercicio 5.17
def padrao_a(n_max):
    comp = len(str(n_max))
    for i in range(1, n_max+1):
        for j in range(1, i+1):
            print(j, end=comp*' ')
        print()

def padrao_b(n_max):
    for i in range(n_max, 0, -1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()

def padrao_c(n_max):
    for i in range(1, n_max+1):
        print(end=2*((n_max-i)*' '))
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()


# Exercicio 5.19
def caminho_random(lado, posx, posy, quadriculas, viagem):
    pos_max = lado * quadriculas
    turtle.color('grey')
    grelha(lado, posx, posy, quadriculas)
    turtle.color('red')
    x = posx + lado * quadriculas/2
    y = posy + lado * quadriculas/2
    turtle.penup()
    turtle.goto(posx + lado*(quadriculas/2), posy + lado*(quadriculas/2))
    turtle.pendown()
    turtle.dot()
    lista_viragens = [0, 90, 180, 270]
    for i in range(viagem):
        viragem = random.choice(lista_viragens)
        if viragem == 90 and y < pos_max:
            y += lado
            turtle.setheading(viragem)
            turtle.forward(lado)
        elif viragem == 270 and y > -pos_max:
            y -= lado
            turtle.setheading(viragem)
            turtle.forward(lado)
        elif viragem == 0 and x < pos_max:
            x += lado
            turtle.setheading(viragem)
            turtle.forward(lado)
        elif viragem == 180 and x > -pos_max:
            x -= lado
            turtle.setheading(viragem)
            turtle.forward(lado)
    turtle.exitonclick()

def grelha(lado, posx, posy, quadriculas):
    turtle.speed(0)
    for i in range(quadriculas):
        linha_grelha(lado, posx, posy, quadriculas)
        posy += lado

def linha_grelha(lado, posx, posy, quadriculas):
    for i in range(quadriculas):
        turtle.penup()
        turtle.goto(posx, posy)
        turtle.pendown()
        quadrado(lado)
        posx += lado

def quadrado(lado):
    for i in range(4):
        turtle.forward(lado)
        turtle.left(90)


# Exercicio 5.21
def excecao_index(cadeia, subcad):
    try:
        pos = cadeia.index(subcad)
        return pos
    except ValueError:
        return -1


# Exercicio 5.20
def fibonacci(num):
    lista = [1, 1]
    for i in range(num+1):
        if i == lista[len(lista)-1] + lista[len(lista)-2]:
            lista.append(i)
    if num in lista:
        print(str(num) + " pertence à sequência de Fibonacci")
    else:
        print(str(num) + " não pertence à sequência de Fibonacci")


# Exercicio 5.16
def perfeitos(num):
    divisores = []
    for i in range(1, num):
        if num % i == 0:
            divisores.append(i)
    if sum(divisores) == num:
        print(str(num) + " é um número perfeito")
    else:
        print(str(num) + " não é um número perfeito\nA sua soma dá", sum(divisores))


if __name__ == '__main__':
    # amigas('bom dia amigos', 'boa dia amigos')
    # numero_par(5)
    # monte_carlo(1000000)
    # logaritmo(5)
    # padrao_a(5)
    # padrao_b(5)
    # padrao_c(5)
    caminho_random(20, -80, -80, 8, 10)
    # print(excecao_index('ola', 'q'))
    # fibonacci(21)
    # perfeitos(22)
