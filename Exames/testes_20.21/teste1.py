import turtle

# Exercicio 2 - 100%
# Trocar dois caracteres de posição
# Exemplo: cadeia = 'abcdef' -> trocaxy(cadeia, 0, 2) -> 'cbadf
def trocaxy(cadeia, x, y):
    n_cadeia = ''
    for i in range(len(cadeia)):
        if x == i:
            n_cadeia += cadeia[y]
        elif y == i:
            n_cadeia += cadeia[x]
        else:
            n_cadeia += cadeia[i]
    print(n_cadeia)


# Exercicio 3 - 100%
# Fazer um quadrado branco em que existe um quadrado preto nos cantos deste
def goto(posx, posy):
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()

def quadrado(lado, cor):
    turtle.fillcolor(cor)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(lado)
        turtle.right(90)
    turtle.end_fill()

def squaredcorners(grande, pequeno):
    quadrado(grande, 'white')
    posx = -pequeno/2
    posy = pequeno/2
    for i in range(2):
        goto(posx, posy)
        quadrado(pequeno, 'black')
        posx += grande
    posx = -pequeno/2
    for i in range(2):
        goto(posx, posy - grande)
        quadrado(pequeno, 'black')
        posx += grande
    turtle.hideturtle()
    turtle.exitonclick()


trocaxy('abcdef', 0, 2)
trocaxy('teste', 4, 2)
squaredcorners(200, 50)
