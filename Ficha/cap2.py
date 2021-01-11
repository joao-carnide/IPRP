# Capitulo 2 - Visões I (Turtle)
import turtle
import random
import math


def quadrado(lado):
    for i in range(4):
        turtle.forward(lado)
        turtle.left(90)
    turtle.hideturtle()
    turtle.exitonclick()


# Exercicio 2.1
def estrela(uni, ang):
    for i in range(5):
        turtle.forward(uni)
        turtle.right(ang)
    turtle.hideturtle()
    turtle.exitonclick()


# Exercicio 2.2
def estrela_espiral(lado, ang, stop):
    for i in range(stop):
        turtle.forward(lado)
        turtle.right(ang)
        lado += 10
    turtle.hideturtle()
    turtle.exitonclick()


# Exercicio 2.3
def random_walk(vezes):
    for i in range(vezes):
        lado = random.randint(10, 100)
        angulo = random.randint(1, 360)
        cor_r = random.random()
        cor_g = random.random()
        cor_b = random.random()
        turtle.pendown()
        turtle.pencolor(cor_r, cor_g, cor_b)
        turtle.forward(lado)
        turtle.left(angulo)
        turtle.penup()
    turtle.hideturtle()
    turtle.exitonclick()


# Exercicio 2.4
def poligono_regular(comp, n_lados):
    ang = 360 / n_lados
    for i in range(n_lados):
        turtle.forward(comp)
        turtle.right(ang)
    turtle.hideturtle()
    turtle.exitonclick()

def circunferencia(raio):
    perimetro = 2 * math.pi * raio
    comp = perimetro / 360
    poligono_regular(comp, 360)


# Exercicio 2.7
def smile():
    cara_olhos(100, 0, 0, 'yellow')  # cara
    cara_olhos(15, -40, 125, 'black')  # olho
    cara_olhos(15, 40, 125, 'black')  # olho
    turtle.right(30)
    boca(100, -55, 50, 65)  # boca
    turtle.hideturtle()
    turtle.exitonclick()

def cara_olhos(raio, pos_x, pos_y, cor):
    turtle.penup()
    turtle.goto(pos_x, pos_y)
    turtle.fillcolor(cor)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(raio, 360)
    turtle.end_fill()

def boca(raio, pos_x, pos_y, ang):
    turtle.penup()
    turtle.goto(pos_x, pos_y)
    turtle.pendown()
    turtle.circle(raio, ang)


# Exercicio 2.9
def rasto(tam, passo, ang, vezes):
    turtle.penup()
    for i in range(vezes):
        turtle.stamp()
        tam += passo
        turtle.forward(tam)
        turtle.right(ang)
    turtle.hideturtle()
    turtle.exitonclick()


# Exercicio 2.10
def relogio(lado):
    for i in range(12):
        turtle.forward(lado)
        turtle.stamp()
        turtle.goto(0, 0)
        turtle.left(30)
    turtle.hideturtle()
    turtle.exitonclick()


# Exercicio 2.11
def hexagono(lado):
    for i in range(6):
        triangulo(lado)
        turtle.left(60)
    turtle.hideturtle()
    turtle.exitonclick()

def triangulo(lado):
    for i in range(3):
        turtle.forward(lado)
        turtle.left(120)
    turtle.hideturtle()
    turtle.exitonclick()


# Exercicio 2.14
def quadrados(lado_i, posx_i, posy_i, n_quads):
    for i in range(n_quads):
        turtle.penup()
        turtle.goto(posx_i, posy_i)
        turtle.pendown()
        for j in range(4):
            turtle.forward(lado_i)
            turtle.left(90)
        posx_i -= 5
        posy_i -= 5
        lado_i += 10
    turtle.hideturtle()
    turtle.exitonclick()


# Exercicio 2.15
def nautilus(lado_i, n_quads, rot):
    for i in range(n_quads):
        for j in range(4):
            turtle.forward(lado_i)
            turtle.left(90)
        turtle.left(rot)
        lado_i += 5
    turtle.hideturtle()
    turtle.exitonclick()


# Exercicio 2.12
def casa(lado, posx_c, posy_c, lado_c, altura_c, casa_cor, chamine_cor, telhado_cor):
    # casa
    turtle.fillcolor(casa_cor)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(lado)
        turtle.right(90)
    turtle.end_fill()
    # chamine
    turtle.penup()
    turtle.goto(posx_c, posy_c)
    turtle.pendown()
    turtle.fillcolor(chamine_cor)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(lado_c)
        turtle.left(90)
        turtle.forward(altura_c)
        turtle.left(90)
    turtle.end_fill()
    # telhado
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.fillcolor(telhado_cor)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(lado)
        turtle.left(120)
    turtle.end_fill()
    turtle.hideturtle()
    turtle.exitonclick()


# Exercicio 2.16
def jogos_olimpicos(cima_i, baixo_i, raio, cor1, cor2, cor3, cor4, cor5):
    turtle.pensize(3)
    # aneis cima
    lista_cima = [cor1, cor2, cor3]
    for i in range(3):
        turtle.penup()
        turtle.goto(cima_i, 0)
        turtle.pendown()
        turtle.pencolor(lista_cima[i])
        turtle.circle(raio)
        cima_i += raio*2 + 5
    # aneis baixo
    lista_baixo = [cor4, cor5]
    for i in range(2):
        turtle.penup()
        turtle.goto(baixo_i, -raio)
        turtle.pendown()
        turtle.pencolor(lista_baixo[i])
        turtle.circle(raio)
        baixo_i += raio*2 + 5
    turtle.hideturtle()
    turtle.exitonclick()


# Exercicio 2.13
def esse(raio):
    turtle.penup()
    turtle.goto(-raio*2, 0)
    turtle.pendown()
    turtle.setheading(270)
    turtle.circle(raio, -180)
    turtle.setheading(270)
    turtle.circle(raio, 180)


# Exercicio 2.18
def ying_yang(raio_g, raio_p):
    turtle.fillcolor('black')
    turtle.begin_fill()
    esse(raio_g)
    turtle.setheading(90)
    turtle.circle(raio_g*2, -180)
    turtle.end_fill()
    turtle.setheading(270)
    turtle.circle(raio_g*2, -180)
    turtle.penup()
    turtle.goto(-(raio_g-raio_p), 0)
    turtle.pendown()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.circle(raio_p, 360)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(raio_g + raio_p, 0)
    turtle.pendown()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.circle(raio_p, 360)
    turtle.end_fill()
    turtle.hideturtle()
    turtle.exitonclick()


# Exercicio 2.17
def radioatividade(lado_quad, lado_tri, orient, raio, cor1, cor2):
    turtle.penup()
    turtle.goto(-lado_quad/2, lado_quad/2)
    turtle.pendown()
    quadrado_cor(lado_quad, cor1, cor2)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    for i in range(3):
        turtle.setheading(orient)
        parte(lado_tri, cor1)
        orient -= 120
    turtle.penup()
    turtle.goto(0, -raio)
    turtle.pendown()
    circulo(raio, cor1, cor2)
    turtle.hideturtle()
    turtle.exitonclick()

def quadrado_cor(lado, cor1, cor2):
    turtle.pencolor(cor1)
    turtle.fillcolor(cor2)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(lado)
        turtle.right(90)
    turtle.end_fill()

def parte(lado, cor):
    turtle.fillcolor(cor)
    turtle.begin_fill()
    turtle.forward(lado)
    turtle.left(90)
    turtle.circle(lado, 60)
    turtle.left(90)
    turtle.forward(lado)
    turtle.end_fill()

def circulo(raio, cor1, cor2):
    turtle.pencolor(cor2)
    turtle.fillcolor(cor1)
    turtle.begin_fill()
    turtle.circle(raio)
    turtle.end_fill()


# Xadrez cause bored
def xadrez(lado, cor1, cor2, posx, posy):
    aux_posx = posx
    aux_posy = posy
    turtle.speed(9)
    # linhas impares
    for i in range(4):
        turtle.penup()
        turtle.goto(posx, posy)
        turtle.pendown()
        for j in range(4):
            quads_cor(lado, cor1, cor2, posx, posy)
            posx += lado * 2
        posx = aux_posx
        posy -= lado * 2
    posx = aux_posx
    posy = aux_posy - lado
    # linhas pares
    for i in range(4):
        turtle.penup()
        turtle.goto(posx, posy)
        turtle.pendown()
        for j in range(4):
            quads_cor(lado, cor2, cor1, posx, posy)
            posx += lado * 2
        posx = aux_posx
        posy -= lado * 2
    turtle.hideturtle()
    turtle.exitonclick()

def quads_cor(lado, cor1, cor2, posx, posy):
    lista_cor = [cor1, cor2]
    for i in range(2):
        turtle.penup()
        turtle.goto(posx, posy)
        turtle.pendown()
        turtle.fillcolor(lista_cor[i])
        turtle.begin_fill()
        quad(lado)
        turtle.end_fill()
        posx += lado

def quad(lado):
    for i in range(4):
        turtle.forward(lado)
        turtle.right(90)


# Colmeia
def colmeia(lado, linha, coluna, posx, posy):
    turtle.speed(8)
    for i in range(coluna):
        coluna_hex(lado, posx, posy, linha)
        if i % 2 == 0:
            posx += lado*2
            posy += lado
        else:
            posx += lado*2
            posy -= lado
    turtle.hideturtle()
    turtle.exitonclick()

def coluna_hex(lado, posx, posy, linha):
    for i in range(linha):
        turtle.penup()
        turtle.goto(posx, posy)
        turtle.pendown()
        if i % 2 == 0:
            turtle.fillcolor('white')
        else:
            turtle.fillcolor('black')
        turtle.begin_fill()
        hexagon(lado)
        turtle.end_fill()
        posy -= lado*2

def hexagon(lado):
    for i in range(6):
        turtle.forward(lado)
        turtle.right(60)


if __name__ == '__main__':
    # quadrado(50)
    # estrela(100, 144)
    # estrela_espiral(5, 144, 20)
    # random_walk(50)
    # poligono_regular(1, 360)
    # circunferencia(50)
    # smile()
    # rasto(10, 10, 30, 10)
    # relogio(100)
    # hexagono(100)
    # quadrados(30, 5, 5, 30)
    # nautilus(10, 100, 10)
    # casa(100, 75, 0, 5, 75, 'lime', 'black', 'red')
    # jogos_olimpicos(-55, -5, 50, 'blue', 'black', 'red', 'orange', 'lightgreen')
    # esse(50)
    # ying_yang(100, 20)
    # radioatividade(440, 200, 0, 50, 'black', 'yellow')
    # xadrez(25, 'white', 'black', -100, 100)
    colmeia(25, 6, 6, -200, 200)
