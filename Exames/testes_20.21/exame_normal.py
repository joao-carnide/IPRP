# Exercicio 1
def misterio(nome):
    l = []
    with open(nome) as f:
        for s in f.readlines():
            t = []
            for x in s.split():
                if x.isdigit():
                    t.append(int(x))
            l.append(t)
    return l

# Exercicio 2
def entrelaca(cadeia1, cadeia2):
    n_cadeia = ''
    if len(cadeia1) > len(cadeia2):
        for i in range(len(cadeia2)):
            n_cadeia += cadeia1[i] + cadeia2[i]
        n_cadeia += cadeia1[len(cadeia2):]
    elif len(cadeia1) < len(cadeia2):
        for i in range(len(cadeia1)):
            n_cadeia += cadeia1[i] + cadeia2[i]
        n_cadeia += cadeia2[len(cadeia1):]
    else:
        for i in range(len(cadeia1)):
            n_cadeia += cadeia1[i] + cadeia2[i]
    print((n_cadeia, len(n_cadeia)))

# Exercicio 3
def processa_dados(lista):
    lista_somas = []
    somas_dif = []
    for dados in lista:
        if dados[0] + dados[1] not in somas_dif:
            somas_dif.append(dados[0] + dados[1])
        lista_somas.append(dados[0] + dados[1])
    valor = []
    for soma in somas_dif:
        aux = []
        for dados in lista:
            if dados[0] + dados[1] == soma:
                aux.append(dados)
        conta = lista_somas.count(soma)
        valor.append([conta, aux])
    dicio = {}
    for i in range(len(somas_dif)):
        dicio[somas_dif[i]] = valor[i]
    print(dicio)

# Exercicio 4
def export_friends(t, fname):
    fich = open(fname, 'w')
    lista_pessoas = []
    for i in t:
        for pessoa in i:
            if pessoa not in lista_pessoas:
                lista_pessoas.append(pessoa)
    dicio_amigos = {}
    for pessoa in lista_pessoas:
        lista_amigos = []
        for amizade in t:
            for amigo in amizade:
                if pessoa in amizade and pessoa != amigo:
                    lista_amigos.append(amigo)
        dicio_amigos[pessoa] = lista_amigos
    texto = ''
    for pessoa in lista_pessoas:
        texto += pessoa + ';'
    texto += '\n'
    for chave, valor in dicio_amigos.items():
        for pessoa in lista_pessoas:
            if chave == pessoa:  # condição desnecessária
                texto += '0'
            elif pessoa in valor:
                texto += 'X'
            else:
                texto += '0'
        texto += '\n'
    fich.write(texto)
    fich.close()


if __name__ == '__main__':
    print(misterio("iva.txt"))
    entrelaca('acegikmoqsuwy', 'bdfhjlnprtvxz')
    entrelaca('acegikmoqsuvwxyz', 'bdfhjlnprt')
    entrelaca('acegikmoqs', 'bdfhjlnprtuvwxyz')
    processa_dados([(2, 2), (4, 2), (5, 1), (4, 4), (5, 2), (5, 2)])
    processa_dados([(2, 2), (2, 2), (3, 1)])
    export_friends([('joao', 'maria'), ('maria', 'sofia'), ('sofia', 'catia')], "fich.txt")
