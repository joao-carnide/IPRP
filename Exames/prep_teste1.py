# Exercicios de Preparação para o Teste 1
import turtle
import random
import math


# Teste 1 2015 TP4
# Exercicio 2
def divisores(numero):
    print("Divisores de " + str(numero) + ":")
    for i in range(1, numero):
        if numero % i == 0:
            print(i)

# Exercicio 3
def mickey(posx, posy, tam, cor_r, cor_g, cor_b):
    circulo(posx, posy, tam, cor_r, cor_g, cor_b)
    circulo(posx - (2 * tam / 2), posy + 1.5 * tam, tam / 2, cor_r, cor_g, cor_b)
    circulo(posx + (2 * tam / 2), posy + 1.5 * tam, tam / 2, cor_r, cor_g, cor_b)

def circulo(posx, posy, tam, cor_r, cor_g, cor_b):
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()
    turtle.pencolor(cor_r, cor_g, cor_b)
    turtle.fillcolor(cor_r, cor_g, cor_b)
    turtle.begin_fill()
    turtle.circle(tam)
    turtle.end_fill()

def random_mickey(numero):
    for i in range(numero):
        posx = random.randint(-300, 300)
        posy = random.randint(-300, 300)
        tam = random.randint(5, 50)
        cor_r = random.random()
        cor_g = random.random()
        cor_b = random.random()
        mickey(posx, posy, tam, cor_r, cor_g, cor_b)
    turtle.hideturtle()
    turtle.exitonclick()


# Teste 1 2015 TP6-TP8
# Exercicio 2
def maiores_90_circulo(ni, nf):
    r = 1
    area_circulo = math.pi * r**2
    print("Poligonos com area maior do que 90% da area do circulo:")
    for n in range(ni, nf+1):
        area_poligono = n * math.pow(r, 2) * math.cos(math.pi/n) * math.sin(math.pi/n)
        if area_poligono > area_circulo * 0.9:
            print("Poligono com " + str(n) + " lados")

# Exercicio 3
def prateleira(livros, posx, posy):
    grossura = 20
    estante(livros * grossura, 50, posx, posy)
    for i in range(livros):
        turtle.penup()
        turtle.goto(posx + i * grossura, posy)
        turtle.pendown()
        altura = random.randint(10, 50)
        livro(grossura, altura)
    turtle.hideturtle()
    turtle.exitonclick()

def estante(comp, altura, posx, posy):
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()
    for i in range(2):
        turtle.forward(comp)
        turtle.left(90)
        turtle.forward(altura)
        turtle.left(90)

def livro(comp, altura):
    for i in range(2):
        turtle.forward(comp)
        turtle.left(90)
        turtle.forward(altura)
        turtle.left(90)


# Teste 1 2015 TP7
def dados():
    n_dados = int(input("Quantos dados deseja jogar? "))
    soma = 0
    seis = 0
    for i in range(n_dados):
        jogada = random.randint(1, 6)
        if jogada == 6:
            seis += 1
        soma += jogada
    print("A soma foi de >> " + str(soma) + " e o numero seis saiu " + str(seis) + " vezes")

# Exercicio 3
def cortina(ondas, altura, largura):
    topo(altura, largura)
    for i in range(ondas):
        onda((largura/ondas)/4)
    turtle.hideturtle()
    turtle.exitonclick()

def topo(altura, largura):
    turtle.setheading(90)
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(largura)
    turtle.left(90)
    turtle.forward(altura)

def onda(raio):
    turtle.setheading(-90)
    turtle.circle(raio, 180)
    turtle.setheading(270)
    turtle.circle(raio, -180)


# Teste 1 2013 TP2-TP8
# Exercicio 2
def domino(posx, posy, comp, larg, espaco):
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()
    peca(comp, larg)
    traco(posx + comp/2, posy + larg/8, larg - larg/4)
    pontos(posx + comp/8, posy + espaco, larg/5, 'black')
    pontos(posx + comp / 8 + 2*larg/5 + espaco, posy + espaco, larg / 5, 'black')
    pontos(posx + comp / 8, posy + (larg / 8) + 2 * larg / 5 + espaco, larg / 5, 'black')
    pontos(posx + comp / 8 + 2*larg/5 + espaco, posy + (larg / 8) + 2*larg/5 + espaco, larg / 5, 'black')
    turtle.hideturtle()
    turtle.exitonclick()

def peca(comp, larg):
    for i in range(2):
        turtle.forward(comp)
        turtle.left(90)
        turtle.forward(larg)
        turtle.left(90)

def ponto(raio, cor):
    turtle.fillcolor(cor)
    turtle.begin_fill()
    turtle.circle(raio)
    turtle.end_fill()

def traco(posx, posy, traco):
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(traco)
    turtle.setheading(0)

def pontos(posx, posy, raio, cor):
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()
    ponto(raio, cor)

# Exercicio 3
def bola_cair(altura, n_saltos):
    distancia = altura
    print("Bola desce " + str(altura) + " metros")
    for i in range(n_saltos-1):
        altura /= 2
        print("Bola sobe " + str(altura) + " metros\nBola desce " + str(altura) + " metros")
        distancia += altura * 2
    print("Distancia percorrida final =", distancia)


# Teste 1 2013 TP3
# Exercicio 2
def flor_geometrica(petalas, cor):
    comp = 100
    larg = 50
    for i in range(petalas):
        retangulo(comp, larg, cor)
        turtle.right(360/petalas)
    turtle.hideturtle()
    turtle.exitonclick()

def retangulo(comp, larg, cor):
    turtle.fillcolor(cor)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(larg)
        turtle.left(90)
        turtle.forward(comp)
        turtle.left(90)
    turtle.end_fill()

# Exercicio 3
def n_abs(cadeia):
    valida = 'abc'
    n_a = 0
    n_b = 0
    for i in range(len(cadeia)):
        if cadeia[i] not in valida:
            print("Cadeia inválida")
            return
    for i in range(len(cadeia)):
        if cadeia[i] == 'a':
            n_a += 1
        elif cadeia[i] == 'b':
            n_b += 1
    if n_a == n_b:
        print("numero de a's é igual ao numero de b's, ambos", n_a)
    else:
        print("o numero de a's e b's é diferente")


# Teste 1 2013 TP4-TP6
# Exercicio 2
def num_nao_vogais_min(cadeia):
    vogais = 'aeiou'
    soma = 0
    for i in range(len(cadeia)):
        if cadeia[i] not in vogais:
            soma += 1
    print(soma)

# Exercicio 3
def floco_neve(comp, posx, posy):
    for i in range(6):
        turtle.setheading(i*60)
        turtle.forward(comp)
        mini_floco(comp/4)
        turtle.goto(posx, posy)
    turtle.hideturtle()
    turtle.exitonclick()

def mini_floco(comp):
    turtle.setheading(90)
    for i in range(6):
        turtle.forward(comp)
        turtle.backward(comp)
        turtle.right(60)
    turtle.setheading(0)


# Teste 1 2013 TP7-TP9
# Exercicio 2
def cara_geometrica(comp_c, comp_ol, cor1, comp_or, larg_or, comp_n, larg_n, cor2, comp_b, larg_b, cor3, posx, posy):
    goto(posx, posy)
    ret(comp_c, comp_c, cor='white')
    # Olhos
    goto(posx + comp_c/5, posy + 3 * comp_c/4)
    ret(comp_ol, comp_ol, cor1)
    goto(posx + 3 * comp_c / 5, posy + 3 * comp_c / 4)
    ret(comp_ol, comp_ol, cor1)
    # Orelhas
    goto(posx - comp_or, posy + comp_c/2)
    ret(comp_or, larg_or, cor2)
    goto(posx + comp_c, posy + comp_c/2)
    ret(comp_or, larg_or, cor2)
    # Nariz
    goto(posx + comp_c/2 - comp_n/2, posy + comp_c/3)
    ret(comp_n, larg_n, cor2)
    # Boca
    goto(posx + comp_c/2 - comp_b/2, posy + comp_c/5)
    ret(comp_b, larg_b, cor3)
    turtle.hideturtle()
    turtle.exitonclick()

def goto(posx, posy):
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()

def ret(comp, larg, cor):
    turtle.fillcolor(cor)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(comp)
        turtle.left(90)
        turtle.forward(larg)
        turtle.left(90)
    turtle.end_fill()

# Exercicio 3
def hamming(cad1, cad2):
    dist = 0
    cad_menor = ''
    cad_maior = ''
    if len(cad1) < len(cad2):
        dist += math.fabs(len(cad1) - len(cad2))
        print("cadeia 1 é menor")
        cad_menor = cad1
        cad_maior = cad2
    elif len(cad1) > len(cad2):
        dist += math.fabs(len(cad1) - len(cad2))
        print("cadeia 2 é menor")
        cad_menor = cad2
        cad_maior = cad1
    for i in range(len(cad_menor)):
        if cad_menor[i] != cad_maior[i]:
            dist += 1
    print("Distancia de Hamming =", dist)


# Testes 1 2012
# Exercicio 1
def lado_pentagono(raio):
    lado = math.tan(math.pi/5) * raio * 2
    print(lado)

# Exercicio 2
def valor_ph(ph):
    if ph < 0 or ph > 14:
        print("Valor de pH invalido")
    elif ph < 7:
        print("Solucao Acida")
    elif ph > 7:
        print("Solucao Basica")
    else:
        print("Solucao Neutra")

# Exercicio 3
def remove_car(cadeia, caracter):
    n_cadeia = ''
    for i in range(len(cadeia)):
        if cadeia[i] != caracter:
            n_cadeia += cadeia[i]
    print(n_cadeia)


# Outro Teste 1 2012
def inicio(cadeia, percentagem):
    p = percentagem/100
    n_tam = int(len(cadeia) * p)
    print(cadeia[:n_tam])


# Exame Normal 2016
# Exercicio 2
def caminho_ferro(comp_lado, comp_base, travessas):
    comp_lado /= travessas
    comp_base /= travessas
    x = - comp_base/2
    y = - math.sqrt((comp_base/2)**2 + comp_lado**2)
    for i in range(travessas):
        turtle.setheading(turtle.towards(x, y))
        turtle.forward((i+1) * comp_lado)
        turtle.goto(-turtle.position()[0], turtle.position()[1])
        turtle.goto(0, 0)
    turtle.hideturtle()
    turtle.exitonclick()

# Exercicio 3
def ocorrencias(cadeia, subcadeia):
    conta = 0
    for i in range(len(cadeia)-len(subcadeia)+1):
        if cadeia[i:i+len(subcadeia)] == subcadeia:
            conta += 1
    print(conta)


# Exercicio Balão
def balao(raio1, raio2, orient, fio, tracos):
    turtle.setheading(orient)
    for i in range(tracos):
        fio_tam(fio)
    turtle.circle(raio1)
    turtle.circle(raio1, -180)
    turtle.setheading(90)
    turtle.circle(raio2)
    turtle.exitonclick()

def fio_tam(comp):
    turtle.forward(comp)
    turtle.left(60)
    turtle.forward(comp)
    turtle.right(60)


# Exame Recurso 2019
# Exercicio 2
def tracejado(posx, posy, comp, larg, espaco):
    goto(posx, posy)
    aux = 0
    for i in range(4):
        if i % 2 == 0:
            tracos(aux, comp, espaco)
        else:
            tracos(aux, larg, espaco)
        aux = 0
        turtle.right(90)
    turtle.hideturtle()
    turtle.exitonclick()

def tracos(aux, dist, espaco):
    while aux <= dist:
        turtle.forward(espaco)
        turtle.penup()
        turtle.forward(espaco)
        turtle.pendown()
        aux += (espaco * 2)


# Exame Recurso 2018
# Exercicio 2
def bolachas(n, raio, posx, posy, cor):
    goto(posx, posy)
    angulo = 180 - (360 / n)
    turtle.pencolor(cor)
    turtle.fillcolor(cor)
    turtle.begin_fill()
    for i in range(n):
        turtle.circle(raio, 180)
        turtle.right(angulo)
    turtle.end_fill()
    turtle.hideturtle()
    turtle.exitonclick()


# Teste 1 2ª e 3ª fase
# Exercicio 2
def troca_pos(cadeia):
    n_cadeia = ''
    if len(cadeia) % 2 != 0:
        for i in range(len(cadeia)-1):
            if i % 2 == 0:
                n_cadeia += cadeia[i+1]
            else:
                n_cadeia += cadeia[i-1]
        n_cadeia += cadeia[-1]
    else:
        for i in range(len(cadeia)):
            if i % 2 == 0:
                n_cadeia += cadeia[i+1]
            else:
                n_cadeia += cadeia[i-1]
    print(n_cadeia)

# Exercicio 3
def sobrepostos(n_triangulos, lado, posx, posy, cor1, cor2):
    for i in range(n_triangulos):
        turtle.penup()
        turtle.goto(posx, posy)
        turtle.pendown()
        if i % 2 == 0:
            tri_equilatero(lado, cor1)
        else:
            tri_equilatero(lado, cor2)
        posx += 10
        posy -= 10
        lado -= 20
    turtle.hideturtle()
    turtle.exitonclick()

def tri_equilatero(lado, cor):
    turtle.color(cor)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(lado)
        turtle.right(120)
    turtle.end_fill()


# Teste 1 2019 TP1-TP4-TP8
# Exercicio 1
def raizes(a, b, c):
    discriminante = b**2 - 4 * a * c
    if a == 0 or discriminante < 0:
        print("Erro")
    else:
        raiz_disc = math.sqrt(discriminante)  # ERRO: Falta import math no inicio do programa
        raiz1 = float((-b + raiz_disc))/(2*a)
        raiz2 = float((-b - raiz_disc))/(2*a)
        if raiz1 == raiz2:
            print("Solucao:", raiz1)
        else:
            print("Solucoes:", raiz1, raiz2)  # ERRO: print("Solucoes:", raizes) não existe numa variavel raizes,
            # tem de se chamar as 2 individualmente

# Exercicio 2
def palavra_aleatoria(palavra_original):
    n_palavra = ''
    for i in range(len(palavra_original)):
        n_palavra += random.choice(palavra_original)
    print(n_palavra)

# Exercicio 3
def piano(posx, posy, comp, larg):
    for i in range(6):
        seccao(posx, posy, comp, larg)
        posx += larg*4
    turtle.hideturtle()
    turtle.exitonclick()

def seccao(posx, posy, comp, larg):
    aux_posx = posx
    for i in range(4):
        turtle.penup()
        turtle.goto(posx, posy)
        turtle.pendown()
        retang(comp, larg)
        posx += larg
    posx = aux_posx
    turtle.fillcolor('black')
    turtle.begin_fill()
    for i in range(3):
        turtle.penup()
        turtle.goto(posx + (2/3)*larg, posy)
        turtle.pendown()
        retang(comp/2, (3/4)*larg)
        posx += larg
    turtle.end_fill()

def retang(comp, larg):
    for i in range(2):
        turtle.forward(larg)
        turtle.right(90)
        turtle.forward(comp)
        turtle.right(90)


# Teste 1 2019 TP2-TP5-TP9
# Exercicio 1
# Cadeias de caracteres são coleções ordenadas, homogeneas e imutaveis
# Tuplos são coleções ordenadas, heterogéneas e imutaveis
# Em mémoria estará a = '555' e b = ('5', '5', '5')

# Exercicio 2
def cadeia_comp(cadeia, car_a, car_b):
    n_cadeia = ''
    for i in range(len(cadeia)):
        if car_a <= cadeia[i] <= car_b:
            n_cadeia += cadeia[i]
    print(n_cadeia)

# Exercicio 3
def teias(posx, posy, orient, fios, shape, lado):
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.setheading(orient)
    turtle.pendown()
    lado_n = lado / fios
    lado /= fios
    for i in range(fios):
        hexagon(lado)
        lado += lado_n
    turtle.goto(posx, posy)
    turtle.shape(shape)
    turtle.exitonclick()

def hexagon(lado):
    for i in range(6):
        triangulo(lado)
        turtle.left(60)

def triangulo(lado):
    for i in range(3):
        turtle.forward(lado)
        turtle.left(120)


# Teste 1 2019 TP7
# Exercicio 1
def mostra(i):
    # print(a_str[-1])   ERRO: não existe numa variavel a_str definida no espaço de nomes da função mostra
    a_str = i[0]
    print(a_str[-1])
def func():
    a_str = 'ola'
    mostra(a_str)

# Exercicio 2
def acumula_letras(cadeia, letras):
    n_cadeia = ''
    for i in range(len(cadeia)):
        if cadeia[i] in letras:
            n_cadeia += cadeia[i]
    print(n_cadeia)

# Exercicio 3
def grafico(linhas, pontos, lim_x, lim_y):
    eixos(lim_x, lim_y)
    for i in range(linhas):
        cor_r = random.random()
        cor_g = random.random()
        cor_b = random.random()
        turtle.pencolor(cor_r, cor_g, cor_b)
        soma_x = 0
        soma_y = 0
        x = 0
        y = 0
        for j in range(pontos):
            while x <= soma_x < lim_x:
                x = random.randint(1, lim_x)
            while y <= soma_y < lim_y:
                y = random.randint(1, lim_y)
            turtle.goto(x, y)
            soma_x += x
            soma_y += y
        turtle.penup()
        turtle.home()
        turtle.pendown()
    turtle.hideturtle()
    turtle.exitonclick()

def eixos(lim_x, lim_y):
    turtle.forward(lim_x)
    turtle.stamp()
    turtle.home()
    turtle.left(90)
    turtle.forward(lim_y)
    turtle.stamp()
    turtle.home()


# Teste 1 TP3-TP6
# Exercicio 1
# s = 'the brown tox jumped over the lazy dog'
# s[10] = 'f'   dá erro pois uma string é imutavel e não se pode subtituir valores desta
# print(s)      o print do s dará o mesmo que s inicial

# Exercicio 2
def obtem_sub_cadeias(cadeia, char_i, char_f):
    n_cadeia = ''
    inicio1 = cadeia.index(char_i)
    fim1 = cadeia.index(char_f, inicio1)
    inicio2 = cadeia.rindex(char_i)
    fim2 = cadeia.rindex(char_f, inicio2)
    n_cadeia += cadeia[inicio1:fim1 + 1]
    n_cadeia += '\n'
    n_cadeia += cadeia[inicio2:fim2+1]
    print(n_cadeia)

# Exercicio 3
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
        hexa(lado)
        turtle.end_fill()
        posy -= lado*2

def hexa(lado):
    for i in range(6):
        turtle.forward(lado)
        turtle.right(60)


# Flor - saiu no testes das 9h
def flor(r_caule, larg_caule, orient):
    petalas(n_petalas=5, raio=100, ang=45)
    goto(r_caule, -r_caule)
    caule(r_caule - larg_caule/2, larg_caule, orient)
    turtle.exitonclick()

def caule(r_caule, larg_caule, orient):
    turtle.setheading(orient)
    turtle.circle(r_caule, 90)
    turtle.right(90)
    turtle.forward(larg_caule)
    turtle.right(90)
    turtle.circle(-(r_caule + larg_caule), 90)
    turtle.right(90)
    turtle.forward(larg_caule)

def petalas(n_petalas, raio, ang):
    ang_rot = 180 / 5
    for i in range(n_petalas):
        turtle.circle(raio, ang)
        turtle.left(135)
        turtle.circle(raio, ang)
        turtle.left(ang_rot - ang)


if __name__ == '__main__':
    # divisores(24)
    # mickey(0, 0, 75, 0, 0, 0)
    # random_mickey(5)
    # maiores_90_circulo(3, 10)
    # prateleira(10, -100, 0)
    # dados()
    # cortina(5, 100, 200)
    # domino(-50, 0, 200, 100, 5)
    # bola_cair(10, 3)
    # flor_geometrica(16, 'red')
    # n_abs('aabc')
    # num_nao_vogais_min("Uma cadeia de caracteres!")
    # floco_neve(100, 0, 0)
    # cara_geometrica(100, 20, 'blue', 10, 20, 10, 25, 'red', 25, 10, 'yellow', 0, 0)
    # hamming('bons dias joao', 'bom dia joana')
    # lado_pentagono(50)
    # valor_ph(7)
    # remove_car('Vamos remover um caracter', 'a')
    # inicio("Programacao", 30)
    # caminho_ferro(200, 100, 20)
    # ocorrencias('olalal mundo', 'lal')
    # balao(10, 50, 60, 25, 5)
    # tracejado(-100, 50, 200, 100, 10)
    # bolachas(30, 15, 100, 100, 'blue')
    # troca_pos('amanha')
    # sobrepostos(6, 150, -100, 100, 'yellow', 'blue')
    # raizes(1, 4, 3)
    # palavra_aleatoria('domino')
    # piano(-250, 150, 100, 20)
    # cadeia_comp('bom dia', 'a', 'f')
    # teias(0, 0, 0, 10, 'turtle', 100)
    # func()
    # acumula_letras('o teste deste exercicio', 'eo')
    # acumula_letras('o teste deste exercicio', 'oi')
    # grafico(3, 5, 200, 200)
    # obtem_sub_cadeias('aaa#aeiou*aaa#abcd*', '#', '*')
    # colmeia(25, 5, 6, -200, 200)
    # caule(100, 5, 90)
    # petalas(5, 100, 45)
    flor(100, 5, 90)
