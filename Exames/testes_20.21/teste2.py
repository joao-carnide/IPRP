# Exercicio 1
def calcula(lista_a, lista_b):
    r1 = r2 = -1
    for i in range(len(lista_a)):
        if lista_a[i] % 2 == 0 and lista_a[i] in lista_b:
            r1 = i
            r2 = lista_a[i]
    return r1, r2

# Exercicio 2
# Dado um dicionário de brinquedos como chave e valor lista de pessoas que os pediu determinar o mais pedido, em caso de empate, retornar o ultimo
def calcula_mais_pedido(d):
    mais_pedido = ''
    pedido = 0
    for chave, valor in d.items():
        if len(valor) >= pedido:
            pedido = len(valor)
            mais_pedido = chave
    print(mais_pedido)

# Exercicio 3
# Dado um dicionario organizar cada brinquedo num ficheiro (com nº de pessoas que pediu e nome das pessoas) e ter um ficheiro brinquedos_pedidos com a lista de todos os brinquedos no dicionario
def organiza_pedido(d):
    # escrever ficheiro brinquedos_pedidos.txt
    escreve_pedidos(d, "brinquedos_pedidos.txt")
    # escrever ficheiros dos brinquedos
    escreve_briquedos(d, "brinquedos_pedidos.txt")

def escreve_pedidos(d, fname):
    fich_pedidos_w = open(fname, 'w')
    lista_brinquedos = list(d.keys())
    for i in range(len(lista_brinquedos)):
        texto_pedidos = ''
        texto_pedidos += lista_brinquedos[i] + '.txt\n'
        fich_pedidos_w.write(texto_pedidos)
    fich_pedidos_w.close()

def escreve_briquedos(d, fname):
    fich_pedidos_ler = open(fname, 'r')
    linhas = fich_pedidos_ler.readlines()
    for i in range(len(linhas)):
        linhas[i] = linhas[i].strip()
    for i in range(len(linhas)):
        fich_briquedo = open(linhas[i], 'w')
        info_brinquedo = ''
        for chave, valor in d.items():
            if chave in linhas[i]:
                info_brinquedo += str(len(valor)) + '\n'
                for j in range(len(valor)):
                    info_brinquedo += valor[j] + '\n'
        fich_briquedo.write(info_brinquedo)
        fich_briquedo.close()
    fich_pedidos_ler.close()


if __name__ == '__main__':
    print(calcula([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6]))
    print(calcula([11, 12, 13, 14, 15, 16], [11, 13, 15]))
    calcula_mais_pedido({'Barbie': ['Joao', 'Pedro'], 'Bola de futebol': ['Ana'], 'Nenuco': ['Goncalo', 'David']})
    organiza_pedido({'Barbie': ['Joao', 'Pedro'], 'Bola de futebol': ['Ana'], 'Nenuco': ['Goncalo', 'David']})
