# Capítulo 6 - Objetos (II)
import random
import turtle
import math

# Exercicio 6.2
def pares_impares(lista):
    par = 0
    impar = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            par += lista[i]
        else:
            impar += lista[i]
    print((par, impar))


# Exercicio 6.4
def conta_menores(num, lista):
    n_menores = 0
    for i in range(len(lista)):
        if lista[i] < num:
            n_menores += 1
    print(n_menores)


# Exercicio 6.6
def soma_comulativa(lista):
    soma = 0
    lista_soma = []
    for i in range(len(lista)):
        soma += lista[i]
        lista_soma.append(soma)
    print(lista_soma)


# Exercicio 6.7
def imagem(lista):
    lista_negativo = []
    for i in range(len(lista)):
        aux = []
        for j in range(len(lista[i])):
            if lista[i][j] < 0 or lista[i][j] > 1:
                print("lista inválida")
            else:
                if lista[i][j] == 0:
                    aux.append(1)
                else:
                    aux.append(0)
        lista_negativo.append(aux)
    print(lista_negativo)


# Exercicio 6.8
def imagem_90(lista):
    # passa elementos para a linha correta
    lista_linha = []
    for col in range(len(lista[0])):
        n_linha = []
        for linha in lista:
            n_linha.append(linha[col])
        lista_linha.append(n_linha)
    # troca elemento final com inicial
    lista_final = []
    for linha in range(len(lista_linha)):
        lista_final.append(lista_linha[linha][::-1])
    print(lista_final)


# Exercicio 6.3
def alterna(lista1, lista2):
    lista = []
    for i in range(len(lista1)):
        lista.append(lista1[i])
        lista.append(lista2[i])
    print(lista)


# Exercicio 6.5
def lancamentos_pares(n_lancamentos):
    lista_somas = []
    for i in range(n_lancamentos):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        lista_somas.append(dado1 + dado2)
    pares = 0
    for i in range(len(lista_somas)):
        if lista_somas[i] % 2 == 0:
            pares += 1
    prob_par = pares / n_lancamentos
    print("Probabilidade de sair número par =", prob_par)


# Exercicio 6.9
def gera_comandos(n):
    direcoes = 'ADER'
    lista_comandos = []
    for i in range(n):
        lista_comandos.append(random.choice(direcoes))
    return lista_comandos

def navega(comandos, tartaruga):
    tartaruga.shape('circle')
    tartaruga.color('lime')
    tartaruga.stamp()
    tartaruga.color('black')
    andar = 50
    for i in range(len(comandos)):
        if comandos[i] == 'A':
            tartaruga.forward(andar)
        elif comandos[i] == 'D':
            tartaruga.right(90)
        elif comandos[i] == 'E':
            tartaruga.left(90)
        elif comandos[i] == 'R':
            tartaruga.backward(andar)
    tartaruga.color('red')
    tartaruga.stamp()
    tartaruga.hideturtle()

def main_tarta(n):
    tartaruga = turtle.Turtle()
    comandos = gera_comandos(n)
    navega(comandos, tartaruga)
    turtle.exitonclick()


# Exercicio 6.10
def existe_chave(dicio, chave):
    if chave in dicio.keys():
        print(chave + " existe no dicionário")
    else:
        print(chave + " não existe no dicionário")


# Exercicio 6.11
def dicio_fruta(lista_fruta, lista_stock):
    dicio = {}
    for i in range(len(lista_fruta)):
        dicio[lista_fruta[i]] = lista_stock[i]
    print(dicio)


# Exercicio 6.12
# dicio = {fruta: {compra: c, venda: v, peso: p, stock: s}}
def lucro(dicio):
    lucro = 0
    for val in dicio.values():
        lucro += (val['peso'] - val['stock']) * (val['venda'] - val['compra'])
    print(lucro)

def mais_cara(dicio):
    lista = []
    for fruta, info in dicio.items():
        lista.append([info['venda'], fruta])
    cara = max(lista)
    print("Fruta mais cara da loja:", cara[-1])


# Exercicio 6.13
def converter_data(data):
    dias_semana = {1: 'Domingo', 2: 'Segunda-feira', 3: 'Terça-feira', 4: 'Quarta-feira', 5: 'Quinta-feira', 6: 'Sexta-feira', 7: 'Sábado'}
    meses_ano = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
    lista = data.split('/')
    print(dias_semana[int(lista[0])] + ", " + lista[1] + " de " + meses_ano[int(lista[2])] + " de " + lista[3])


# Exercicio 6.14
def metabolismo(dicio):
    n_dicio = dicio
    for chave, valor in dicio.items():
        if valor['genero'] == 'Masculino':
            meta = 66 + (6.3 * valor['peso']) + (12.9 * valor['altura']) - (6.8 * valor['idade'])
        else:
            meta = 65.5 + (4.3 * valor['peso']) + (4.7 * valor['altura']) - (4.7 * valor['idade'])
        valor['metabolismo'] = round(meta, 2)
        n_dicio[chave] = valor
    print(n_dicio)


# Exercicio 6.15
def imc_bi(dicio):
    n_dicio = dicio
    for chave, valor in dicio.items():
        imc = valor['peso'] / math.pow(valor['altura'], 2)
        valor['imc'] = round(imc, 2)
        n_dicio[chave] = valor
    print(n_dicio)


# Exercicio 6.16
def posicoes(cadeia):
    dicio = {}
    vogais = 'aAeEiIoOuU'
    for i in range(len(cadeia)):
        if cadeia[i] in vogais:
            dicio[cadeia[i]] = dicio.get(cadeia[i], []) + [i]
    return dict(sorted(dicio.items()))


# Exercicio 6.17
def inverte_dicio(dicio):
    inv_dicio = {}
    for chave, valor in dicio.items():
        inv_dicio[valor] = inv_dicio.get(valor, []) + [chave]
    print(inv_dicio)


# Exercicio 6.18
# arvore = { pai: [pessoa1, pessoa2]}
def irmaos(dicio, nome1, nome2):
    prog1 = progenitor(dicio, nome1)
    prog2 = progenitor(dicio, nome2)
    if prog1 == prog2:
        print(nome1 + " e " + nome2 + " são irmãos")
    else:
        print(nome1 + " e " + nome2 + " não são irmãos")

# função para ver o progenitor de uma pessoa
def progenitor(dicio, pessoa):
    prog = ''
    for pai, filho in dicio.items():
        if pessoa in filho:
            prog += pai
    return prog


# Exercicio 6.19
def netos(dicio, pessoa):
    filhos = filho(dicio, pessoa)
    if filhos:
        netos = []
        for pes in filhos:
            neto = filho(dicio, pes)
            if neto:
                netos.append(neto)
        if netos:
            print("Netos de " + pessoa + ": " + str(netos))
        else:
            print(pessoa + " não tem netos")
    else:
        print(pessoa + " não tem filhos, logo também não tem netos")

# função para ver os filhos de uma pessoa
def filho(dicio, pessoa):
    filhos = dicio.get(pessoa)
    return filhos


# Exercicio 6.20
def avos(dicio, pessoa):
    prog = progenitor(dicio, pessoa)
    if prog:
        avo = progenitor(dicio, prog)
        if avo:
            print(avo + " é avo de " + pessoa)
        else:
            print(pessoa + " não tem avos")
    else:
        print(pessoa + " não tem pais, logo também não tem avos")


# Exercicio 6.21
def iguais(conj1, conj2):
    if len(conj1) != len(conj2):
        return False
    for i in range(len(conj1)):
        if conj1[i] != conj2[i]:
            return False
    return True


# Exercicio 6.23
def reflexiva(c1, c2):
    relacao = cria_lista(c1, c2)
    for x in relacao:
        if [x, x] not in relacao:
            return False
    return True


# Exercicio 6.24
def simetrica(c1, c2):
    relacao = cria_lista(c1, c2)
    for [x, y] in relacao:
        if [y, x] not in relacao:
            return False
    return True

def cria_lista(c1, c2):
    lista = []
    if len(c1) != len(c2):
        print("conjuntos de tamanho diferente")
        return 0
    for x in c1:
        for y in c2:
            lista.append([x, y])
    return lista


if __name__ == '__main__':
    # pares_impares([1, 4, 7, 9, 3, 2, 8, 5, 6])
    # conta_menores(5, [2, 8, 6, 5, 3, 2])
    # soma_comulativa([1, 2, 3])
    # imagem([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
    # imagem_90([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
    # imagem_90([[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1]])
    # alterna([1, 2, 3], ['a', 'b', 'c'])
    # lancamentos_pares(5)
    # main_tarta(10)
    # existe_chave({"php": "Rasmus Lerdorf", "perl": "Larry Wall", "tcl": "John Ousterhout", "awk": "Brian Kernighan", "java": "James Gosling", "parrot": "Simon Cozens", "python": "GuidovanRossum", "xpto": "zxcv"}, "c++")
    # dicio_fruta(['maçã', 'banana'], [10, 4])
    # lucro({'maçã': {'compra': 0.5, 'venda': 1.5, 'peso': 2, 'stock': 10}, 'banana': {'compra': 1, 'venda': 1.75, 'peso': 3, 'stock': 4}})
    # mais_cara({'maçã': {'compra': 0.5, 'venda': 1.5, 'peso': 2, 'stock': 10}, 'banana': {'compra': 1, 'venda': 1.75, 'peso': 3, 'stock': 4}})
    # converter_data("4/5/6/2006")
    # metabolismo({123456789: {'genero': 'Masculino', 'idade': 22, 'altura': 1.75, 'peso': 65}})
    # imc_bi({123456789: {'genero': 'Masculino', 'idade': 22, 'altura': 1.75, 'peso': 65}})
    # print(posicoes('agora e que vao ser elas, Ai, Ai!'))
    # inverte_dicio({'joao': 10, 'pedro': 18, 'tiago': 13, 'luis': 18})
    # irmaos({'João': ['Filipe', 'José'], 'Joana': ['Filipa', 'Mariana']}, 'Filipe', 'José')
    # irmaos({'João': ['Filipe', 'José'], 'Joana': ['Filipa', 'Mariana']}, 'José', 'Mariana')
    # netos({'João': ['Filipe', 'José'], 'Filipe': ['Vasco', 'António'], 'Afonso': ['André', 'Pedro']}, 'João')
    # avos({'João': ['Filipe', 'José'], 'Filipe': ['Vasco', 'António']}, 'Vasco')
    # print(iguais([1, 2, 3], [1, 2, 3]))
    # print(reflexiva([0, 1], [1, 0]))
    print(simetrica([0, 1], [0, 1]))
