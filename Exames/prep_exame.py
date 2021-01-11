# Exercicios de preparação para o exame

import turtle
import random 
import math

'''
Definições Teóricas
Cadeias - coleções ordenadas, homogéneas e imutáveis
Tuplos - coleções ordenadas, heterogéneas e imutáveis
Listas - coleções ordenadas, heterogéneas e mutáveis
Dicionários - coleções sem ordem, heterogéneas e mutáveis
Ficheiros - coleções ordenas, homogéneas sem mutabilidadas
'''

# Exame Normal 2017
# Exercicio 1
'''
a = 2
t = (1, 2, 3)
l = list(t)
def xpto(x, y):
    y = x * y
    return y
print(xpto(a, t))
??? -> (1, 2, 3, 1, 2, 3)
t
??? -> (1, 2, 3)
'''

# Exercicio 2
def processa(cadeia):
    lista = []
    ocorrencias = 0
    for i in range(1, len(cadeia)):
        if cadeia[i] == cadeia[i-1]:
            ocorrencias += 1
        else:
            lista.append((cadeia[i-1], (i-1) - ocorrencias, ocorrencias))
            ocorrencias = 0
            if i == len(cadeia) - 1:
                lista.append((cadeia[i], i - ocorrencias, ocorrencias))
    print(lista)

# Exercicio 3
def mais_seguidores(dicio):
    pessoa = ''
    n_seguidores = 0
    for chave, valor in dicio.items():
        if len(valor) > n_seguidores:
            pessoa = chave
            n_seguidores = len(valor)
    print("O utilizador com mais seguidores é", pessoa)


# Exame Recurso 2016
# Exercicio 1
def xpto(lista):
    for i in range(len(lista)):
        m = max(lista[i:])
        ind = lista.index(m)
        lista[i], lista[ind] = lista[ind], lista[i]
    return lista
# O programa não tem erros e permite inverter a lista de input, ou seja, se o input for [1, 2, 3] o output após a execução da função será [3, 2, 1]

# Exercicio 2
def triangulos_volta(n_triangulos, lado):
    for i in range(n_triangulos):
        triangulo(lado)
        turtle.forward(lado)
        turtle.right(360/n_triangulos)
    turtle.hideturtle()
    turtle.exitonclick()

def triangulo(lado):
    for i in range(3):
        turtle.forward(lado)
        turtle.left(120)

# Exercicio 3
def gera_cadeia(lista):
    cadeia = ''
    lista = sorted(lista, key=lambda x: x[1])
    for i in range(len(lista)):
        cadeia += lista[i][0] * (lista[i][2] + 1)
    print(cadeia)

# Exercicio 4
def sugestoes(pessoa, rede, n):
    lista_sug = []
    seguidores = rede.get(pessoa)
    for chave, valor in rede.items():
        for i in seguidores:
            if i in valor and chave != pessoa and chave not in lista_sug:
                lista_sug.append(chave)
    print(lista_sug)

# Exercicio 5
def triatlo(f_name):
    fich_in = open(f_name, 'r')
    fich_out = open("provas_tabela.txt", 'w')
    linhas = fich_in.readlines()
    for i in range(len(linhas)):
        linhas[i] = linhas[i].strip().split()
    for i in range(len(linhas)):
        linhas[i][2] = linhas[i][2].split(':')
        for j in range(len(linhas[i])):
            linhas[i][2][j] = int(linhas[i][2][j])
    lista_rank = []
    for i in range(len(linhas)):
        aux = []
        for j in range(len(linhas[i])):
            if j == 2:
                tempo = linhas[i][j][0] * 60 + linhas[i][j][1] * 60 + linhas[i][j][2]
                aux.append(tempo)
            else:
                aux.append(linhas[i][j])
        lista_rank.append(aux)
    lista_rank = sorted(lista_rank, key=lambda x: x[2])
    menos_tempo = lista_rank[0][2]
    for i in range(5):
        texto = ''
        if i + 1 == 1:
            texto += str(i+1) + '. ' + lista_rank[i][0] + '\n'
            fich_out.write(texto)
        else:
            texto += str(i+1) + '. ' + lista_rank[i][0] + ' +' + str(lista_rank[i][2] - menos_tempo) + 's' + '\n'
            fich_out.write(texto)
    fich_in.close()
    fich_out.close()


# Exame Recurso 2015
# Exercicio 1a
# variaveis locais são variaveis que são definidas e utilizadas unica e exclusivamente da função onde são definidas
# variaveis globais são variaveis que são definidas no codigo sem restrições e podem ser utilizadas em todas as funções
''' Exemplo
a = 10 -> variavel global
def teste():
    b = 2 -> variavel local da função teste
    return b + a
'''

# Exercicio 1b
def mist(seq):
    lista = []
    for i in range(len(seq), 0, -1):
        lista.append(sum(seq[len(seq) - i:]))
    return lista
# valor retornado será [15, 14, 12, 9, 5] com input [1, 2, 3, 4, 5]
# a função faz uma lista que representa a soma dos valores de seq do fim ao inicio

# Exercicio 2
def relogio(horas):
    circulo(100)
    h_min = horas.split(':')
    analog = []
    for i in h_min:
        analog.append(int(i)//12)
    for i in range(len(analog)):
        turtle.setheading(90)
        turtle.right(30 * analog[i])
        if i == 0:
            turtle.forward(50)
        elif i == 1:
            turtle.forward(80)
        goto(0, 0)
    turtle.hideturtle()
    turtle.exitonclick()

def circulo(raio):
    goto(0, -raio)
    turtle.circle(raio)
    goto(0, 0)

# Exercicio 3
def comprar_vender(lista):
    lista_dias = []
    for i in range(len(lista)):
        media = sum(lista[:i+1]) / (i + 1)
        if lista[i] < media:
            lista_dias.append('c')
        else:
            lista_dias.append('v')
    print(lista_dias)

# Exercicio 4
def consistente(base_dados):
    dicio_base = {}
    for valor in base_dados.values():
        dicio_base = valor
    consiste = []
    for valor in base_dados.values():
        if valor.keys() == dicio_base.keys():
            consiste.append(True)
        else:
            consiste.append(False)
    if False in consiste:
        return False
    else:
        return True

# Exercicio 5
def frequencia(cadeia):
    fich_out = open("palavras.txt", 'w')
    cadeia = cadeia.lower()
    palavras = []
    for pal in cadeia.split():
        if pal not in palavras:
            palavras.append(pal)
    for i in range(len(palavras)):
        texto = ''
        conta = cadeia.split().count(palavras[i])
        texto += palavras[i] + ',' + str(conta) + '\n'
        fich_out.write(texto)
    fich_out.close()


# Teste Final 2015
# Exercicio 2
def dardos(raio, cor1, cor2, cor_dardo):
    alvo(raio, cor1, cor2)
    dardo_x = random.randint(-raio, raio)
    dardo_y = random.randint(-raio, raio)
    goto(dardo_x, dardo_y)
    circulo_cor(raio/20, cor_dardo)
    turtle.hideturtle()
    turtle.exitonclick()

def alvo(raio, cor1, cor2):
    for i in range(4):
        goto(0, -raio)
        if i % 2 == 0:
            circulo_cor(raio, cor1)
        else:
            circulo_cor(raio, cor2)
        raio *= (2/3)

def circulo_cor(raio, cor):
    turtle.color(cor)
    turtle.begin_fill()
    turtle.circle(raio)
    turtle.end_fill()

# Exercicio 3
def melhor_filme(dicio_films, lista):
    for chave, valor in dicio_films.items():
        for i in range(1, len(lista)):
            if chave == lista[0]:
                valor.append(lista[i])
    if lista[0] not in dicio_films.keys():
        dicio_films[lista[0]] = lista[1:len(lista)]
    dicio_medias = {}
    for chave, valor in dicio_films.items():
        dicio_medias[chave] = round(sum(valor) / len(valor), 1)
    melhor_media = max(dicio_medias.values())
    melhor_filme = ''
    for chave, valor in dicio_medias.items():
        if valor == melhor_media:
            melhor_filme = chave
    return melhor_filme, melhor_media

# Exercicio 4
def pessoas_soma(fname):
    fich_in = open(fname, 'r')
    fich_out = open("pessoas_soma.txt", 'w')
    linhas = fich_in.readlines()
    linhas = [i.strip().split() for i in linhas]
    for i in range(len(linhas)):
        soma = 0
        for j in range(1, len(linhas[i])):
            linhas[i][j] = int(linhas[i][j])
            soma += linhas[i][j]
        linhas[i].insert(0, soma)
    linhas.sort()
    for i in range(len(linhas)):
        texto = ''
        for j in range(1, len(linhas[i])):
            texto += str(linhas[i][j]) + ' '
        texto += str(linhas[i][0]) + '\n'
        fich_out.write(texto)
    fich_in.close()
    fich_out.close()


# Teste Final 2014
# Exercicio 1b
def palavras(w1, w2):
    dif = len(w1) - len(w2)
    if dif > 0:
        w2 = w2 + dif * " "
    else:
        w1 = w1 + (-dif) * " "
    for i in range(len(w1)):
        print(w1[i], w2[i])

# Exercicio 2
def jaccard(a, b):
    inter = []
    uniao = []
    for i in range(len(a)):
        if a[i] in b:
            inter.append(a[i])
        uniao.append(a[i])
    for i in b:
        if i not in uniao:
            uniao.append(i)
    return len(inter)/len(uniao)

# Exercicio 3
def ingredientes_mais_usados(receitas):
    dicio_ingredientes = {}
    for chave, valor in receitas.items():
        for ing in valor:
            dicio_ingredientes[ing] = dicio_ingredientes.get(ing, []) + [chave]
    mais_usados = []
    usado = 0
    for chave, valor in dicio_ingredientes.items():
        if len(valor) > usado:
            usado = len(valor)
            mais_usados.clear()
            mais_usados.append(chave)
        elif len(valor) == usado:
            mais_usados.append(chave)
    dicio_mais_usados = {}
    for chave, valor in dicio_ingredientes.items():
        for ingrediente in mais_usados:
            if chave == ingrediente:
                dicio_mais_usados[ingrediente] = valor
    print(dicio_mais_usados)

# Exercicio 4
def horarios_salas(fname):
    fich_in = open(fname, 'r')
    fich_out = open("horario_salas.txt", 'w')
    linhas = fich_in.readlines()
    linhas = [linha.strip().split() for linha in linhas]
    dicio_salas = {}
    # criar dicionário com informação de cada sala
    for i in range(len(linhas)):
        dicio_salas[linhas[i][-1]] = dicio_salas.get(linhas[i][-1], []) + [linhas[i][:len(linhas[i])-1]]
    # ordenar por dia da semana e por hora de começo cada sala (valor de cada dicionário)
    for chave, valor in dicio_salas.items():
        valor = sorted(valor, key=lambda x: x[0])
        valor = sorted(valor, key=lambda x: x[1])
        dicio_salas[chave] = valor
    # escrever para o ficheiro
    for chave, valor in dicio_salas.items():
        texto = 'Horario da Sala ' + chave + '\n'
        for i in range(len(valor)):
            for j in range(len(valor[i])):
                texto += valor[i][j] + ' '
            texto += '\n'
        fich_out.write(texto)
    fich_in.close()
    fich_out.close()


# Teste 1 2019 2ª e 3ª fase
# Exercicio 2
def troca_indices(cadeia):
    n_cadeia = ''
    if len(cadeia) % 2 == 0:
        n_cadeia += troca(cadeia, n_cadeia, len(cadeia))
    else:
        n_cadeia += troca(cadeia, n_cadeia, len(cadeia)-1)
        n_cadeia += cadeia[-1]
    print(n_cadeia)

def troca(cadeia, n_cadeia, tam):
    for i in range(tam):
        if i % 2 == 0:
            n_cadeia += cadeia[i + 1]
        else:
            n_cadeia += cadeia[i - 1]
    return n_cadeia

# Exercicio 3
def triangulos(n, lado, cor1, cor2):
    x = y = 0
    for i in range(n):
        goto(x, y)
        if i % 2 == 0:
            equilatero(lado, cor1)
        else:
            equilatero(lado, cor2)
        x += 10
        y -= 10
        lado -= 20
    turtle.hideturtle()
    turtle.exitonclick()

def equilatero(lado, cor):
    turtle.color(cor)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(lado)
        turtle.right(120)
    turtle.end_fill()


# Teste 1 2019 TP1-TP4-TP8
# Exercicio 2
def palavra_aleatoria(palavra_original):
    n_cadeia = ''
    for i in range(len(palavra_original)):
        n_cadeia += random.choice(palavra_original)
    print(n_cadeia)

# Exercicio 3
def piano(comp, larg, cor1, cor2, posx, posy):
    for i in range(5):
        seccao(comp, larg, cor1, cor2, posx, posy)
        posx += larg*4
    turtle.hideturtle()
    turtle.exitonclick()

def seccao(comp, larg, cor1, cor2, posx, posy):
    aux_posx = posx
    for i in range(4):
        goto(posx, posy)
        retangulo(comp, larg, cor1)
        posx += larg
    posx = aux_posx
    for i in range(3):
        goto(posx + (2/3)*larg, posy)
        retangulo(comp/2, (3/4)*larg, cor2)
        posx += larg

def retangulo(comp, larg, cor):
    turtle.fillcolor(cor)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(larg)
        turtle.right(90)
        turtle.forward(comp)
        turtle.right(90)
    turtle.end_fill()


# Teste 2 2019 TP4-TP8-TP9
# Exercicio 1
def auxiliar(lista):
    temp = []
    for i in range(len(lista)-1, -1, -1):
        temp.append(lista[i])
    return temp
def misterio(matriz):
    for i in range(len(matriz)):
        matriz[i] = auxiliar(matriz[i])
    return matriz
# a função inverte as colunas da matriz, ou seja, com um input de [[-1, -10, 0], [8, -1, 10]] o output será de [[0, -10, -1], [10, -1, 8]]

# Exercicio 2
def remove_elementos(lista_int, lista_bin):
    lista = []
    for i in range(len(lista_int)):
        if lista_bin[i] == 1:
            lista.append(lista_int[i])
    return lista

# Exercicio 3
def histograma(fname_in, fname_out):
    fich_in = open(fname_in, 'r')
    fich_out = open(fname_out, 'w')
    linhas = fich_in.readlines()
    texto = ''
    for i in range(len(linhas)):
        linhas[i] = linhas[i].strip()
        texto += linhas[i]
    lista_dif = []
    for i in range(len(texto)):
        if texto[i] not in lista_dif:
            lista_dif.append(texto[i])
    for letra in lista_dif:
        aux = ''
        conta = texto.count(letra)
        aux += letra + ' | ' + '*'*conta + '\n'
        fich_out.write(aux)
    fich_in.close()
    fich_out.close()


# Teste 1 2015 TP6-TP8
# Exercicio 2
def maiores_90_circulo(n_min, n_max):
    r = 1  # raio default do enunciado
    area_circulo = math.pi * math.pow(r, 2)
    poligono_90 = []
    for i in range(n_min, n_max+1):
        area = area_poligono(i, r)
        if area > area_circulo * 0.9:
            poligono_90.append(i)
    print("Poligonos com area maior do que 90% da area do circulo:")
    for pol in poligono_90:
        print("Poligono com " + str(pol) + " lados")

def area_poligono(n, r):
    return n * math.pow(r, 2) * math.cos(math.pi/n) * math.sin(math.pi/n)

# Exercicio 3
def prateleira(n_livros, alt_max, larg_livro):
    posx = posy = 0
    retang(n_livros*larg_livro, alt_max)
    alt_min = 5  # altura minima de um livro
    for i in range(n_livros):
        goto(posx, posy)
        altura = random.randint(alt_min, alt_max)
        retang(larg_livro, altura)
        posx += larg_livro
    turtle.hideturtle()
    turtle.exitonclick()

def retang(base, alt):
    for i in range(2):
        turtle.forward(base)
        turtle.left(90)
        turtle.forward(alt)
        turtle.left(90)


# Teste 2 2019 TP2-TP5-TP9
# Exercicio 2
def removeElementos(d, n):
    newd = {}
    delKeys = []
    for chave, valor in d.items():
        if n not in valor:
            newd[chave] = valor
        else:
            delKeys.append(chave)
    return newd, delKeys

# Exercicio 3
def imagem(fname):
    fich_in = open(fname, 'r')
    fich_out = open("imagem_info.txt", 'w')
    linhas = fich_in.readlines()
    linhas = [linha.strip().split() for linha in linhas]
    nl = len(linhas)
    nc = len(linhas[0])
    soma = 0
    for i in range(len(linhas)):
        for j in range(len(linhas[i])):
            soma += int(linhas[i][j])
    mean = soma / (nl * nc)
    info = 'nl = ' + str(nl) + '\nnc = ' + str(nc) + '\nmean = ' + str(mean)
    fich_out.write(info)
    fich_in.close()
    fich_out.close()


# Exame Recurso 2012
# Exercicio 3
def conta_seguidos(cadeia):
    caracteres = []
    for car in cadeia:
        if car not in caracteres:
            caracteres.append(car)
    lista_seguidos = []
    for i in caracteres:
        conta = cadeia.count(i)
        lista_seguidos.append((conta, i))
    print(lista_seguidos)

# Exercicio 4
def acronimos(fname):
    fich_in = open(fname, 'r')
    fich_out = open("acronimo_res.txt", 'w')
    linhas = fich_in.readlines()
    linhas = [pal.strip().split() for pal in linhas]
    lista_siglas = []
    for i in range(len(linhas)):
        sigla = ''
        for j in range(len(linhas[i])):
            sigla += linhas[i][j][0].upper()
        lista_siglas.append(sigla + '\n')
    for acro in lista_siglas:
        fich_out.write(acro)
    fich_in.close()
    fich_out.close()

# Exercicio 5
def maisSeguidores(dicio):
    n_seguidores = 0
    pessoa = []
    for chave, valor in dicio.items():
        if len(valor) >= n_seguidores:
            n_seguidores = len(valor)
            pessoa.append([chave, valor])
    p_rand = random.randint(0, len(pessoa)-1)
    print(tuple(pessoa[p_rand]))


# Exame Recurso 2019
# Exercicio 1
def mst(l_lista):
    aux_1 = list()
    for i in range(len(l_lista)):
        aux_2 = list()
        for j in range(len(l_lista[i])):
            aux_2 += [l_lista[i][j]]
        aux_1 += [aux_2]
    return aux_1

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

def goto(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


# Exercicio 4
def coautor_todos(dicio):
    coautores = ''
    dicio_coautor = {}
    for chave, valor in dicio.items():
        for coautor in valor:
            dicio_coautor[coautor] = dicio_coautor.get(coautor, []) + [chave]
    autor_aux = len(list(dicio.keys())) - 1  # maximo que os autores podem ser coautores, excluido eles mesmos
    for chave, valor in dicio_coautor.items():
        if len(valor) == autor_aux and chave in dicio.keys():
            coautores += chave + ' '
    print(coautores)

# Exercicio 5
def publicacoes_conjuntas(fname, autor):
    fich = open(fname, 'r')
    linhas = fich.readlines()
    linhas = [linha.strip().split("|") for linha in linhas]
    dicio_pubs = {}
    for i in range(len(linhas)):
        linhas[i][2] = linhas[i][2].split(",")
        dicio_pubs[linhas[i][0] + '-' + linhas[i][1]] = linhas[i][2]
    lista_pubs = []
    for chave, valor in dicio_pubs.items():
        if autor in valor:
            lista_pubs.append(chave)
    print(lista_pubs)
    fich.close()


# Teste 1 2020 TP7
# Exercicio 2 - trocar dois caracteres de posição
# Exemplo: cadeia = 'abcdef' -> trocaxy(cadeia, 0, 2) -> 'cbadf
def trocaxy(cadeia, x, y):
    n_cadeia = ''
    for i in range(len(cadeia)):
        if i == x:
            n_cadeia += cadeia[y]
        elif i == y:
            n_cadeia += cadeia[x]
        else:
            n_cadeia += cadeia[i]
    print(n_cadeia)

# Exercicio 3 - fazer um quadrado branco em que existe um quadrado preto nos cantos deste
def squaredcorners(grande, pequeno):
    quadrado(grande, 'white')
    posx = - pequeno / 2
    posy = pequeno / 2
    for i in range(2):
        goto(posx, posy)
        quadrado(pequeno, 'black')
        posx += grande
    posx = - pequeno / 2
    for i in range(2):
        goto(posx, posy - grande)
        quadrado(pequeno, 'black')
        posx += grande
    turtle.hideturtle()
    turtle.exitonclick()

def quadrado(lado, cor):
    turtle.fillcolor(cor)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(lado)
        turtle.right(90)
    turtle.end_fill()


# Teste 2 2020 TP7
# Exercicio 2 - dado um dicionário de briquendos como chave e valor lista de pessoas que os pediu determinar o mais pedido, em caso de empate, retornar o ultimo
def calcula_mais_pedido(dicio):
    mais_pedidos = ''
    pedido = 0
    for chave, valor in dicio.items():
        if len(valor) >= pedido:
            mais_pedidos = chave
    print(mais_pedidos)

# Exercicio 3 - dado um dicionario organizar cada brinquedo num ficheiro (com nº de pessoas que pediu e nome das pessoas) e ter um ficheiro brinquedos_pedidos com a lista de todos os brinquedos no dicionario
def organiza_pedido(dicio):
    brinquedos_pedidos(dicio, 'brinquedos_pedidos.txt')
    info_brinquedos(dicio, 'brinquedos_pedidos.txt')

def brinquedos_pedidos(dicio, fname):
    fich = open(fname, 'w')
    for chave in dicio.keys():
        texto = ''
        texto += chave + '.txt\n'
        fich.write(texto)
    fich.close()

def info_brinquedos(dicio, fname):
    fich_in = open(fname, 'r')
    linhas = fich_in.readlines()
    linhas = [linha.strip() for linha in linhas]
    for brinquedo in linhas:
        fich_out = open(brinquedo, 'w')
        info_brinquedo = ''
        for chave, valor in dicio.items():
            if chave in brinquedo:
                info_brinquedo += str(len(valor)) + '\n'
                for pessoa in valor:
                    info_brinquedo += pessoa + '\n'
        fich_out.write(info_brinquedo)
        fich_out.close()
    fich_in.close()


# Fazer um count apenas usando as operações básicas sobre cadeias de caracteres
def conta(cadeia, caracter):
    soma = 0
    for i in range(len(cadeia)):
        if cadeia[i] == caracter:
            soma += 1
    return soma


# Escrever um programa que pergunte ao utilizador quantos dados quer jogar e apresente no ecrã o número total de pontos e quantas vezes saiu o numero 6
def lanca_dados():
    n_dados = int(input("Quantos dados deseja jogar? "))
    soma = 0
    n_seis = 0
    for i in range(n_dados):
        lancamento = random.randint(1, 6)
        if lancamento == 6:
            n_seis += 1
        soma += lancamento
    print("A soma foi de >> " + str(soma) + " e o numero seis saiu >> " + str(n_seis) + " vezes")


# Exercicio 3.4 - Exercicios Complementares 3
def erros_ortograficos(fname, english):
    fich = open(fname, 'r+')
    linha = fich.readline()
    linha = linha.split()
    fich.seek(0)
    texto = ''
    for i in range(len(linha)):
        if linha[i] not in english:
            texto += '*' + str(linha[i]) + '* '
        else:
            texto += linha[i] + ' '
    fich.write(texto)
    fich.close()

# Exercicio 3.2 - Exercicios Complementares 3
def highscores(fname):
    fich = open(fname, 'r')
    linhas = fich.readlines()
    linhas = [linha.strip().split(',') for linha in linhas]
    linhas = sorted(linhas, key=lambda x: int(x[0]), reverse=True)
    dicio_top3 = {}
    for pessoa in range(3):
        dicio_top3[linhas[pessoa][1]] = linhas[pessoa][0]
    fich.close()
    return dicio_top3

# Exercicio 3.3 - Exercicios Complementares 3
def sort_highscores(fname):
    fich = open(fname, 'r+')
    linhas = fich.readlines()
    linhas = [linha.strip().split(',') for linha in linhas]
    linhas = sorted(linhas, key=lambda x: int(x[0]), reverse=True)
    fich.seek(0)
    texto = ''
    for pessoa in linhas:
        texto += pessoa[0] + ',' + pessoa[1] + '\n'
    fich.write(texto)
    fich.close()


# Exercicio de Turtle do Teste 2 2013 TP9
def figura_quadrados(lado, posx, posy):
    for i in range(1, 5):
        goto(posx, posy)
        quadrados(lado, i, posx, posy)
        posx += lado
        posy -= lado / 2
    turtle.hideturtle()
    turtle.exitonclick()

def quadrados(lado, n_quadrados, posx, posy):
    for i in range(n_quadrados):
        goto(posx, posy)
        quad(lado)
        posy += lado

def quad(lado):
    for i in range(4):
        turtle.forward(lado)
        turtle.right(90)


# Exercicio de listas e strings do Teste 2 2013 TP2-TP8
def cadeia_posicoes(lista, posicoes):
    n_cadeia = ''
    lista = [frase.split() for frase in lista]
    for i in range(len(lista)):
        n_cadeia += lista[i][posicoes[i]] + ' '
    return n_cadeia


# Exercicio turtle Exame Recurso 2013
def quads_coloridos(n_quads, lado, afastamento):
    posx = posy = 0
    for i in range(n_quads):
        cor_r = random.random()
        cor_g = random.random()
        cor_b = random.random()
        goto(posx, posy)
        quad_cor(lado, (cor_r, cor_g, cor_b))
        posx += afastamento
        posy -= afastamento
        lado -= afastamento * 2
    turtle.hideturtle()
    turtle.exitonclick()

def quad_cor(lado, cor):
    turtle.fillcolor(cor)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(lado)
        turtle.right(90)
    turtle.end_fill()


# Teste 3 2012 TP1-TP6
# Exercicio 2
def quantidade(produto, dicio):
    soma = 0
    for chave, valor in dicio.items():
        if produto in dicio.keys() and chave[0:2] == produto[0:2]:
            soma += valor
    print(soma)

# Exercicio 3
def conta_ditado(fname):
    fich = open(fname, 'r')
    linhas = fich.readlines()
    linhas = [linha.strip().split() for linha in linhas]
    palavras = []
    texto = ''
    for i in range(len(linhas)):
        for pal in linhas[i]:
            texto += pal + ' '
            if pal not in palavras:
                palavras.append(pal)
    diferentes = texto.split()
    dicio_palavras = {}
    for pal in palavras:
        conta = 0
        for i in diferentes:
            if pal == i:
                conta += 1
        dicio_palavras[pal] = conta
    fich.close()
    print(dicio_palavras)


# Teste 3 2012 TP2-TP3
# Exercicio 2
def conta_nums(lista):
    dicio_nums = {}
    diferentes = []
    for num in lista:
        if num not in diferentes:
            diferentes.append(num)
    for num in diferentes:
        conta = lista.count(num)
        dicio_nums[num] = conta
    return dicio_nums

# Exercicio 3
def palavra_ficheiro(fname, pos):
    fich = open(fname)
    linhas = fich.readlines()
    linhas = [linha.strip().split() for linha in linhas]
    lista_ficheiro = []
    for i in range(len(linhas)):
        for palavra in linhas[i]:
            lista_ficheiro.append(palavra)
    if pos <= len(lista_ficheiro):
        return lista_ficheiro[pos]
    else:
        return ''


# Exercicio 2 Teste 3 2012 TP7
def ocorrencias(texto):
    palavras = texto.lower().split()
    diferentes = []
    for palavra in palavras:
        if palavra not in diferentes:
            diferentes.append(palavra)
    for i in sorted(diferentes):
        conta = palavras.count(i)
        print(i + " aparece " + str(conta) + " vezes no texto")


# Exercicio 2 Teste 1 2015 TP4
def divisores(numero):
    lista = []
    for i in range(1, numero+1):
        if numero % i == 0:
            lista.append(i)
    return lista


# Exercicio de Turtle onde os circulos em posição random se estiverem dentro de um quadrado são preto e fora brancos
def circulos_quadrado(quad_x, quad_y, lado, raio, n_circulos):
    square(quad_x, quad_y, lado)
    for i in range(n_circulos):
        posx = random.randint(-300, 300)
        posy = random.randint(-300, 300)
        if quad_x < posx < quad_x + lado and quad_y - lado < posy < quad_y:
            circle(raio, 'black', posx, posy)
        else:
            circle(raio, 'white', posx, posy)
    turtle.hideturtle()
    turtle.exitonclick()

def circle(raio, cor, posx, posy):
    goto(posx, posy)
    turtle.fillcolor(cor)
    turtle.begin_fill()
    turtle.circle(raio)
    turtle.end_fill()

def square(posx, posy, lado):
    goto(posx, posy)
    for i in range(4):
        turtle.forward(lado)
        turtle.right(90)


if __name__ == '__main__':
    # processa('x22ddd cbba')
    # mais_seguidores({'cristiano': ['joao', 'antonio', 'filipe', 'pedro'], 'twitter': ['cristiano', 'maria']})
    # triangulos_volta(4, 100)
    # gera_cadeia([('2', 1, 1), ('a', 10, 0), ('x', 0, 0), ('d', 3, 2), (' ', 6, 0), ('c', 7, 0), ('b', 8, 1)])
    # sugestoes('joao', {'tiago': ['rita', 'francisco', 'joao', 'filipa'], 'joao': ['tiago', 'ricardo'], 'ricardo':['rita', 'francisco'], 'rita': ['tiago', 'filipa', 'ricardo'], 'filipa':[], 'francisco': ['tiago']}, 2)
    # triatlo("provas.txt")
    # print(mist([1, 2, 3, 4, 5]))
    # relogio("15:00")
    # comprar_vender([3, 4, 5, 7, 3, 5, 10, 13, 5, 7])
    # print(consistente({'ecosta': {'nome': 'Ernesto', 'apelido': 'Costa', 'nascimento': 1953, 'titulo': 'Catedratico', 'cadeiras': {'LEI': ['IPRP'], 'MEI': ['CE', 'SC']}}, 'pato': {'nome': 'Luis', 'apelido': 'Pato', 'nascimento': 1985, 'titulo': 'Auxiliar', 'cadeiras': {'LEI': ['PPP', 'AED', 'SO'], 'MEI': ['AC', 'RP']}}, 'aneves': {'nome': 'Artur', 'apelido': 'Neves', 'nascimento': 1981, 'titulo': 'Auxiliar', 'cadeiras': {'LEI': ['SD', 'LPA', 'PPP'], 'MEI': ['ES', 'SU', 'VC'], 'LDM': ['PPP']}}}))
    # frequencia("O Tempo perguntou ao tempo quanto tempo o tempo tem o Tempo respondeu ao tempo que o tempo tem tanto tempo quanto tempo tempo tem")
    # dardos(100, 'black', 'white', 'red')
    # print(melhor_filme({'X': [3, 2, 5], 'Y': [1, 3], 'Z': [2, 2, 4, 1]}, ['Y', 5, 5, 4]))
    # print(melhor_filme({'X': [3, 2, 5], 'Y': [1, 3], 'Z': [2, 2, 4, 1]}, ['W', 5, 5, 4]))
    # pessoas_soma("pessoas.txt")
    # palavras("Epoca", "Normal")
    # print(jaccard([1, 2, 3, 4], [2, 3, 5]))
    # ingredientes_mais_usados({'sonhos': ['agua', 'farinha', 'manteiga', 'ovos', 'acucar'], 'rabanadas': ['pao', 'leite', 'ovos', 'manteiga', 'acucar'], 'leite creme': ['acucar', 'farinha', 'ovos', 'leite']})
    # horarios_salas("horario.txt")
    # troca_indices('poder')
    # triangulos(6, 200, 'yellow', 'blue')
    # palavra_aleatoria('domino')
    # piano(100, 20, 'white', 'black', -200, 150)
    # print(misterio([[-1, -10, 0], [8, -1, 10]]))
    # print(remove_elementos([1, 2, 3, 4, 5], [0, 1, 0, 1, 0]))
    # histograma("texto.txt", "histograma.txt")
    # maiores_90_circulo(3, 10)
    # prateleira(10, 100, 30)
    # print(removeElementos({1: [1, 5, 2], 2: [3, 1, 4], 3: [9, 3, 5]}, 5))
    # imagem("imagem.txt")
    # conta_seguidos('abbccc d22x')
    # acronimos("acronimo.txt")
    # maisSeguidores({'Ana': ['Miguel', 'Teresa'], 'Miguel': ['Teresa'], 'Teresa': ['Miguel', 'Ana']})
    # print(mst([[1, 2, 3], [3, 2, 1]]))
    # tracejado(0, 0, 200, 100, 10)
    # coautor_todos({'Gomes': ['Harrison', 'Silva', 'Vilela', 'Dinis'], 'Vilela': ['Harrison', 'Bloch', 'Dalmazo', 'Curado', 'Gomes'], 'Harrison': ['Bloch', 'Vilela']})
    # publicacoes_conjuntas("Ficheiro.txt", "Harrison")
    # trocaxy('abcdef', 0, 2)
    # trocaxy('teste', 4, 2)
    # squaredcorners(200, 50)
    # calcula_mais_pedido({'Barbie': ['Joao', 'Pedro'], 'Bola de futebol': ['Ana'], 'Nenuco': ['Goncalo', 'David']})
    # organiza_pedido({'Barbie': ['Joao', 'Pedro'], 'Bola de futebol': ['Ana'], 'Nenuco': ['Goncalo', 'David']})
    # print(conta('ola bom dia senhor policia', 'a'))
    # lanca_dados()
    # erros_ortograficos("erros.txt", ['a', 'for', 'giant', 'leap', 'man', 'mankind', 'one', 'small', 'step', 'two'])
    # print(highscores("highscores.txt"))
    # sort_highscores("highscores.txt")
    # figura_quadrados(50, -100, 25)
    # print(cadeia_posicoes(["isto e um teste!!", "nao e facil ser informatico.", "realmente custa programar...", "mas... nada e facil hoje em dia"], [0, 0, 1, 1]))
    # quads_coloridos(4, 100, 10)
    # quantidade('XY2002', {'XY2002': 10, 'AY2011': 30, 'ZX2001': 1000, 'XY2010': 400, 'XY2009': 40})
    # quantidade('XY10', {'XY2002': 10, 'AY2011': 30, 'ZX2001': 1000, 'XY2010': 400, 'XY2009': 40})
    # quantidade('XY2007', {'XY2002': 10, 'AY2011': 30, 'ZX2001': 1000, 'XY2010': 400, 'XY2009': 40})
    # conta_ditado("ditado.txt")
    # print(conta_nums(['um', 'dois', 'tres', 'dois', 'dois', 'quatro', 'um']))
    # print(palavra_ficheiro("frase.txt", 10))
    # ocorrencias("Quem parte e reparte e nao fica com a melhor parte ou e tolo ou nao tem arte")
    # print(divisores(24))
    circulos_quadrado(-100, 100, 200, 10, 20)
