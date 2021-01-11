# Exercicios de Preparação para o Teste 2


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
# inverte as colunas da matriz - resultado do print: [[0, -10, -1], [10, -1, 8]]

# Exercicio 2
def remove_elementos(lista_int, lista_bin):
    lista_res = []
    if len(lista_int) != len(lista_bin):
        return "Erro, listas de tamanho diferente"
    for i in range(len(lista_int)):
        if lista_bin[i] == 1:
            lista_res.append(lista_int[i])
    return lista_res

# Exercicio 3
def histograma(fname_in, fname_out):
    fich_in = open(fname_in, 'r')
    fich_out = open(fname_out, 'w')
    lista_car = fich_in.readlines()
    texto = ''
    for i in range(len(lista_car)):
        texto += lista_car[i]
    lista_dif = list(set(texto))
    lista_dif.remove("\n")
    final = ''
    for i in range(len(lista_dif)):
        aux = ''
        conta = texto.count(lista_dif[i])
        aux += str(lista_dif[i]) + " | " + '*'*conta + "\n"
        fich_out.write(aux)
        final += aux
    print(final)
    fich_in.close()
    fich_out.close()


# Teste 2 2018 TP4-TP2
# Exercicio 1
def mais_primeiros(lista_corridas):
    lista_vencedores = []
    for i in range(len(lista_corridas)):
        for j in range(len(lista_corridas[i])):
            if lista_corridas[i][j] == 1:
                lista_vencedores.append(j)
    primeiros = 0
    numero = 0
    for i in range(len(lista_vencedores)):
        conta = lista_vencedores.count(lista_vencedores[i])
        if conta > primeiros:
            primeiros = conta
            numero = lista_vencedores[i]
    print("O piloto com mais primeiros lugares (" + str(primeiros) + ") foi o numero " + str(numero))

# Exercicio 2
def reciprocas(dicio):
    dar = list(dicio.keys())
    lista = []
    for i in range(len(dar)):
        recebe = recebe_de(dicio, dar[i])
        dador = da_a(dicio, dar[i])
        for j in range(len(recebe)):
            if recebe[j] in dador:
                lista.append([dar[i], recebe[j]])
    for i in range(len(lista)):
        lista[i].sort()
    recip = []
    for i in lista:
        if i not in recip:
            recip.append(i)
    recip = [tuple(i) for i in recip]
    print(recip)

def recebe_de(dicio, pessoa):
    pes = []
    for chave, valor in dicio.items():
        if pessoa in valor:
            pes.append(chave)
    return pes

def da_a(dicio, pessoa):
    pessoas = dicio.get(pessoa)
    return pessoas

# Exercicio 3
def hifen(fname_in, fname_out):
    fich_in = open(fname_in, 'r')
    fich_out = open(fname_out, 'w')
    n_linhas = []
    linhas = fich_in.readlines()
    for i in range(len(linhas)):
        linhas[i] = linhas[i].replace('\n', '')
        n_linhas.append(len(linhas[i]))
    maior = max(n_linhas)
    for i in range(len(linhas)):
        texto = ''
        texto += linhas[i] + '-'*(maior-len(linhas[i])) + '\n'
        fich_out.write(texto)
    fich_in.close()
    fich_out.close()


# Teste 2 2019 TP2-TP5-TP9
# Exercicio 1
# a = 5 // l1 = l2 = l3 = [3, [1, 5, 3], [5, 2]]

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
def imagem(fname_in, fname_out):
    fich_in = open(fname_in, 'r')
    fich_out = open(fname_out, 'w')
    linhas = fich_in.readlines()
    lista_num = []
    for i in range(len(linhas)):
        lista_num.append(linhas[i].split())
    soma = 0
    for i in range(len(lista_num)):
        for j in range(len(lista_num[i])):
            lista_num[i][j] = int(lista_num[i][j])
            soma += lista_num[i][j]
    nl = len(lista_num)
    nc = len(lista_num[0])
    mean = soma/(nl * nc)
    stats = 'nl = ' + str(nl) + '\nnc = ' + str(nc) + '\nmean = ' + str(mean)
    fich_out.write(stats)
    fich_in.close()
    fich_out.close()


# Teste 2 2019 TP3-TP6
# Exercicio 1
# chave - numero de estudante
# valor - dicionario com chaves nome (valor nome do aluno) e disciplinas concluidas (valor de dicionario com chave disciplina e valor nota)
# {2017247442: {'nome': 'João Nunes', 'concluidas/nota': {'COMP': 14, 'CG': 11, 'IIA': 15, 'LPA': 13, 'SI': 16}}}

# Exercicio 2
def find(file, cad):
    fich_in = open(file, 'r')
    fich_out = open("teste2_2019/output_find.txt", 'w')
    fich_linhas = fich_in.readlines()
    linhas = ''
    for i in range(len(fich_linhas)):
        if cad in fich_linhas[i]:
            linhas += str(i+1) + ' '
    fich_out.write(linhas)
    fich_in.close()
    fich_out.close()

# Exercicio 3
def cria_dicionario(dic):
    ano = 2019
    dicio_maes = {}
    for chave, valor in dic.items():
        dicio_maes[valor[0]] = dicio_maes.get(valor[0], ()) + (chave, valor[1])
    filhos = []
    for valor in dicio_maes.values():
        aux = []
        for i in range(len(valor)):
            if i % 2 != 0:
                aux.append(ano - valor[i])
        filhos.append(aux)
    dicio = {}
    pos = 0
    for chave in dicio_maes.keys():
        dicio[chave] = (len(filhos[pos]), max(filhos[pos]))
        pos += 1
    print(dicio)


# Teste 2 2019 TP7
# Exercicio 1
# Listas são coleções odenadas, heterogeneas e mutaveis
# Dicionários são coleção sem ordem, heterogeneas e mutaveis

# Exercicio 2
def extrai_info(lista_pontos):
    soma_x = 0
    soma_y = 0
    soma_z = 0
    dicio = {}
    for i in range(len(lista_pontos)):
        soma_x += lista_pontos[i][0]
        soma_y += lista_pontos[i][1]
        soma_z += lista_pontos[i][2]
        dicio[lista_pontos[i]] = lista_pontos.count(lista_pontos[i])
    media_x = soma_x/len(lista_pontos)
    media_y = soma_y/len(lista_pontos)
    media_z = soma_z/len(lista_pontos)
    return media_x, media_y, media_z, dicio

# Exercicio 3
def n_vezes(fname):
    fich_in = open(fname, 'r')
    fich_out = open('teste2_2019/output_vezes.txt', 'w')
    linhas = fich_in.readlines()
    for i in range(len(linhas)):
        linhas[i] = linhas[i].replace('\n', '')
        linhas[i] = linhas[i].split("-")
        linhas[i][0] = int(linhas[i][0])
    out = ''
    for i in range(len(linhas)):
        out += linhas[i][1] * int(linhas[i][0])
    fich_out.write(out)
    fich_in.close()
    fich_out.close()


# Teste Final 2016
# Exercicio 4
def soma_vetores(dicio_x1, dicio_x2):
    x1 = cria_lista0(dicio_x1)
    x2 = cria_lista0(dicio_x2)
    x1 = give_vals(dicio_x1, x1)
    x2 = give_vals(dicio_x2, x2)
    vet_soma = []
    for i in range(len(x1)):
        vet_soma.append(x1[i] + x2[i])
    dicio_soma = get_dicio(vet_soma)
    print(dicio_soma)

def get_dicio(vet_soma):
    dicio_soma = {}
    for i in range(len(vet_soma)):
        if vet_soma[i] != 0:
            dicio_soma[i] = vet_soma[i]
    dicio_soma['len'] = len(vet_soma)
    return dicio_soma

def cria_lista0(dicio):
    x = []
    for chave, valor in dicio.items():
        if chave == 'len':
            x = [0, ] * valor
    return x

def give_vals(dicio, x):
    for chave, valor in dicio.items():
        if chave != 'len':
            x[chave] = valor
    return x

# Exercicio 5
def soma_vet_fich(fname):
    fich = open(fname, 'r')
    lista = fich.readlines()
    for i in range(len(lista)):
        lista[i] = lista[i].strip().split(',')
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            lista[i][j] = int(lista[i][j])
    vet_soma = []
    for i in range(len(lista[0])):
        aux = 0
        for j in range(len(lista)):
            aux += lista[j][i]
        vet_soma.append(aux)
    dicio_soma = get_dicio(vet_soma)
    print(dicio_soma)


# Teste Final 2015
def melhor_filme(dicio_films, lista):
    # adiciona valores da lista ao dicionario
    for chave, valor in dicio_films.items():
        for i in range(1, len(lista)):
            if chave == lista[0]:
                valor.append(lista[i])
    if lista[0] not in dicio_films.keys():
        dicio_films[lista[0]] = lista[1:len(lista)]
    # fazer dicionario auxiliar com médias
    dicio_medias = {}
    for chave, valor in dicio_films.items():
        if len(valor) >= 3:
            dicio_medias[chave] = round(sum(valor)/len(valor), 1)
    # saber a média mais alta e a qual filme pertence
    media = max(dicio_medias.values())
    chave = list(dicio_medias.keys())
    valor = list(dicio_medias.values())
    filme = chave[valor.index(media)]
    return filme, media

# Exercicio 4
def pessoas_soma(fname):
    fich_in = open(fname, 'r')
    fich_out = open("pessoas_soma.txt", 'w')
    linhas = fich_in.readlines()
    for i in range(len(linhas)):
        linhas[i] = linhas[i].split()
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


# Exercicio de ver quantos digitos e letras existem numa string
def conta_digitos_letras(cadeia):
    digitos = 0
    letras = 0
    for i in range(len(cadeia)):
        if cadeia[i].isdigit():
            digitos += 1
        elif cadeia[i].isalnum():
            letras += 1
    print("DIGITOS: " + str(digitos) + "\nLETRAS: " + str(letras))


# Exame Normal 2016
# Exercicio 2
def processa(cadeia):
    lista = []
    seguidos = 0
    for i in range(1, len(cadeia)):
        info_car = ()
        pos = i-1
        if cadeia[i-1] == cadeia[i]:
            seguidos += 1
        else:
            info_car += (cadeia[i-1], pos-seguidos, seguidos)
            seguidos = 0
            lista.append(info_car)
    print(lista)

# Exercicio 3
def mais_seguido(dicio):
    popular = ''
    maior = 0
    for chave, valor in dicio.items():
        if maior < len(valor):
            maior = len(valor)
            popular = chave
    print("O utilizador com mais seguidores é: @" + popular)


# Exercicio de passar uma linha para maiuscula
def maiusculas(fname, n):
    fich = open(fname, 'r+')
    linhas = fich.readlines()
    if n > len(linhas):
        return "Faltam linhas"
    else:
        linhas[n] = linhas[n].upper()
        fich.seek(0)
        for i in range(len(linhas)):
            fich.write(linhas[i])
    fich.close()


# Teste 2 3013 TP2-TP8
# Exercicio 2
def cadeia_listas(lista_cad, lista_pos):
    for i in range(len(lista_cad)):
        lista_cad[i] = lista_cad[i].split()
    texto = ''
    for i in range(len(lista_cad)):
        if i != len(lista_cad)-1:
            texto += lista_cad[i][lista_pos[i]] + ' '
        else:
            texto += lista_cad[i][lista_pos[i]]
    texto += '.'
    return texto

# Exercicio 3
def domino():
    dicio = {}
    for i in range(1, 7):
        aux = []
        for j in range(i, 7):
            aux.append(j)
        dicio[i] = aux
    lista_comb = []
    for chave, valor in dicio.items():
        for i in range(len(valor)):
            lista_comb.append(chave + valor[i])
    comb = list(set(lista_comb))
    return "Pontos possiveis: " + str(comb)


# Teste 2 2013 TP4-TP6
# Exercicio 2
def moda(lista):
    dicio = {}
    for i in range(len(lista)):
        dicio[lista[i]] = lista.count(lista[i])
    max_valor = max(dicio.values())
    lista_aux = []
    for chave, valor in dicio.items():
        if valor == max_valor:
            lista_aux.append(chave)
    print((min(lista_aux), max_valor))


# Teste 2 2013 TP7
# Exercicio 2
def medias(lista):
    soma_min = 0
    soma_max = 0
    for i in range(len(lista)):
        soma_min += lista[i][0]
        soma_max += lista[i][1]
    media_min = soma_min/len(lista)
    media_max = soma_max/len(lista)
    print((media_min, media_max))

# Exercicio 3
def temperaturas(lista):
    maior = 0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if maior < lista[i][j]:
                maior = lista[i][j]
    conta = 0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] == maior:
                conta += 1
    print("Maior temperatura: " + str(maior) + "\nNúmero de vezes registada: " + str(conta))


# Exame Recurso 2017
# Exercicio 3
def gera_cadeia(lista):
    cadeia = ''
    lista = sorted(lista, key=lambda x: x[1])
    for i in range(len(lista)):
        cadeia += lista[i][0] * (lista[i][2] + 1)
    print(cadeia)

# Exercicio 5
def prova_classificacao(fname):
    fich_in = open(fname, 'r')
    fich_out = open("provas_tabela.txt", 'w')
    linhas = fich_in.readlines()
    for i in range(len(linhas)):
        linhas[i] = linhas[i].strip().split()
    for i in range(len(linhas)):
        linhas[i][2] = linhas[i][2].split(':')
        for j in range(len(linhas[i][2])):
            linhas[i][2][j] = int(linhas[i][2][j])
    n_lista = []
    for i in range(len(linhas)):
        tempo = 0
        aux = []
        for j in range(len(linhas[i])):
            if j == 2:
                tempo = linhas[i][j][0] * 60 + linhas[i][j][1] * 60 + linhas[i][j][2]
                aux.append(tempo)
            else:
                aux.append(linhas[i][j])
        n_lista.append(aux)
    n_lista = sorted(n_lista, key=lambda x: x[2])
    menos_tempo = n_lista[0][2]
    for i in range(5):
        texto = ''
        texto += str(i+1) + '. ' + n_lista[i][0] + ' +' + str(n_lista[i][2] - menos_tempo) + 's\n'
        fich_out.write(texto)
    fich_in.close()
    fich_out.close()


# Exercicios Complementares
# Exercicio 2.1
def ultima(lista, n):
    ocorrencias = []
    if n not in lista:
        return -1
    else:
        for i in range(len(lista)):
            if lista[i] == n:
                ocorrencias.append(i)
    return ocorrencias[-1]

# Exercicio 2.2
def desliza_dir(lista):
    desliza = []
    for i in range(len(lista)):
        desliza.append(lista[i-1])
    return desliza

# Exercicio 2.3
def desliza_esq(lista):
    desliza = []
    for i in range(len(lista)):
        if i+1 >= len(lista):
            desliza.append(lista[0])
        else:
            desliza.append(lista[i+1])
    return desliza


# Teste 2 2020 das 9h
# Exercicio 1 - Pq é que uma lista pode ser fatiada e um dicionário não?
# As listas apresentam ordem (base do fatiamento nas listas) e os dicionários não têm qualquer ordem

# Exercicio 2
def localizacoes(fname):
    fich = open(fname, 'r')
    linhas = fich.readlines()
    nomes = []
    for i in range(len(linhas)):
        linhas[i] = linhas[i].strip().split(',')
        for j in range(1, len(linhas[i])):
            linhas[i][j] = int(linhas[i][j])
        if linhas[i][0] not in nomes:
            nomes.append(linhas[i][0])
    dicio = {}
    for nome in nomes:
        aux = []
        for i in range(len(linhas)):
            if nome == linhas[i][0]:
                aux.append((linhas[i][1], linhas[i][2], linhas[i][3]))
                dicio[nome] = aux
    return dicio

# Exercicio 3
def encontro(dicio, pessoa):
    lista_pos = dicio.get(pessoa)
    for chave, valor in dicio.items():
        if chave != pessoa:
            for i in range(len(lista_pos)):
                for j in range(len(valor)):
                    if lista_pos[i] == valor[j]:
                        posicao = (lista_pos[i][1], lista_pos[i][2])
                        print("Às " + str(lista_pos[i][0]) + ", " + chave + " esteve em contacto com " + pessoa + " em " + str(posicao))


if __name__ == '__main__':
    # print(misterio([[-1, -10, 0], [8, -1, 10]]))
    # print(remove_elementos([1, 2, 3, 4, 5], [0, 1, 0, 1, 0]))
    # histograma("teste2_2019/texto.txt", "teste2_2019/histograma.txt")
    # mais_primeiros([(1, 3, 2, 4), (2, 3, 1, 4), (1, 2, 3, 4), (2, 1, 4, 3)])
    # reciprocas({'Joana': ['Pedro', 'Tania', 'Joao'], 'Joao': ['Pedro', 'Joana', 'Sofia', 'Tania'], 'Tania': ['Pedro', 'Ines', 'Joao']})
    # hifen("teste2_2019/linhas.txt", "teste2_2019/linhas_hifen.txt")
    # print(removeElementos({1: [1, 5, 2], 2: [3, 1, 4], 3: [9, 3, 5]}, 5))
    # imagem("teste2_2019/imagem.txt", "teste2_2019/imagem_stats.txt")
    # find("teste2_2019/texto.txt", 'wet')
    # cria_dicionario({10: (3, 2000), 20: (4, 1998), 21: (4, 1987), 11: (3, 1990)})
    # print(extrai_info([(1, 1, 1), (1, 2, 3), (1, 2, 3), (1, 5, 2)]))
    # n_vezes("teste2_2019/input.txt")
    # soma_vetores({3: 5, 6: 2, 'len': 7}, {1: 2, 3: 4, 5: 3, 'len': 7})
    # soma_vet_fich("vetores.txt")
    # print(melhor_filme({'X': [3, 2, 5], 'Y': [1, 3], 'Z': [2, 2, 4, 1]}, ['Y', 5, 5, 4]))
    # print(melhor_filme({'X': [3, 2, 5], 'Y': [1, 3], 'Z': [2, 2, 4, 1]}, ['W', 5, 5, 4]))
    # pessoas_soma("pessoas.txt")
    # conta_digitos_letras("hello world! 123")
    # processa('x22ddd cbba ')
    # mais_seguido({'cristiano': ['joao', 'antonio', 'filipe', 'pedro'], 'twitter': ['cristiano', 'maria'], })
    # maiusculas("lyrics_upper.txt", 1)
    # print(cadeia_listas(["isto e um teste!!", "nao e facil ser informatico.", "realmente custa programar...", "mas... nada e facil hoje em dia."], [0, 0, 1, 1]))
    # print(domino())
    # moda([96, 79, 79, 96, 63, 96, 45, 89, 45, 79])
    # medias([(10, 25), (12, 27), (14, 29), (16, 30)])
    # temperaturas([(10, 25), (12, 27), (25, 30), (30, 30)])
    # gera_cadeia([('2', 1, 1), ('a', 10, 0), ('x', 0, 0), ('d', 3, 2), (' ',6, 0), ('c', 7, 0), ('b', 8, 1)])
    # prova_classificacao("provas.txt")
    # print(ultima([2, 4, 1, 2, 4, 5, 5, 2], 2))
    # print(desliza_dir([1, 2, 3, 4]))
    # print(desliza_esq([1, 2, 3, 4]))
    print(localizacoes("localizacao.txt"))
    encontro({'joao': [(100, 4, 5), (200, 3, 4)], 'carlos': [(200, 3, 4)], 'maria': [(100, 4, 5)], 'sara': [(200, 3, 4)]}, 'joao')
