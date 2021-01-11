# Capitulo 7 - Ficheiros
import random
import turtle

# Exercicio 7.1
def primeiro():
    fich = open('ficheiros_aula/primeiro.txt', 'w')
    conteudo = "Acabei de criar o meu primeiro ficheiro em Python\n"
    fich.write(conteudo)
    print("ficheiro primeiro.txt criado com sucesso")
    fich.close()


# Exercicio 7.2
def seq_ficheiro(car_i, car_f):
    fich = open("ficheiros_aula/primeiro.txt", 'r')
    conteudo = fich.readline()
    print(conteudo[car_i:car_f])
    fich.close()


# Exercicio 7.3
def linha_data(data_hoje):
    fich = open('ficheiros_aula/primeiro.txt', 'a')
    fich.writelines(data_hoje)
    fich.close()


# Exercicio 7.4
def numeros(fname):
    lista_num = []
    fich = open(fname, 'r')
    linhas = fich.readlines()
    for i in range(len(linhas)):
        linha = linhas[i].split()
        for j in range(len(linha)):
            if linha[j].isdigit():
                lista_num.append(int(linha[j]))
    print("Números encontrados no ficheiro:", lista_num)
    fich.close()


# Exercicio 7.6
def copia_fich(fname1, fname2):
    fich1 = open(fname1, 'r')
    fich2 = open(fname2, 'w')
    conteudo = fich1.read()
    fich2.write(conteudo)
    fich1.close()
    fich2.close()


# Exercicio 7.7
def gerar_numeros(fname, n_pares):
    fich = open(fname, 'w')
    for i in range(n_pares):
        aux = ''
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        aux += str(dado1) + ' ' + str(dado2) + '\n'
        fich.writelines(aux)
    fich.close()

def desenha_coord(fname, n_pares):
    gerar_numeros(fname, n_pares)
    fich = open(fname, 'r')
    lista_pares = []
    for i in range(n_pares):
        lista_pares.append(fich.readline().split())
    print(lista_pares)
    x_origin = float(lista_pares[0][0]) * 20
    y_origin = float(lista_pares[0][1]) * 20
    turtle.penup()
    turtle.goto(x_origin, y_origin)
    turtle.pendown()
    for i in range(1, len(lista_pares)):
        turtle.goto(float(lista_pares[i][0]) * 20, float(lista_pares[i][1]) * 20)
    turtle.goto(x_origin, y_origin)
    turtle.hideturtle()
    turtle.exitonclick()
    fich.close()


# Exercicio 7.11
def gerir_vendas(fname_base, fname_gestor):
    fich_base = open(fname_base, 'r')
    fich_gestor = open(fname_gestor, 'w')
    lista_info = fich_base.readlines()
    lista_gestao = []
    for i in range(len(lista_info)):
        lista_gestao.append(lista_info[i].split())
    for i in range(len(lista_gestao)):
        texto = ''
        vendedor = input("Vendedor da venda " + lista_gestao[i][0] + ": ")
        texto += "Venda a Dinheiro No " + lista_gestao[i][0] + "\n-----------------------\nEmpresa: " + lista_gestao[i][1] + "\nN.C.: " + lista_gestao[i][2] + "\nData: " + lista_gestao[i][3] + "\nValor: " + lista_gestao[i][4] + "\nVendedor: " + vendedor + '\n\n'
        fich_gestor.write(texto)
    fich_base.close()
    fich_gestor.close()


# Exercicio 7.12
def int_repetidos(fname):
    fich = open(fname, 'r')
    dicio = {}
    lista = fich.readlines()
    lista_num = []
    for i in range(len(lista)):
        aux = [lista[i].split()]
        for j in range(len(aux[0])):
            lista_num.append(int(aux[0][j]))
    lista_num.sort()
    for i in range(1, len(lista_num)):
        if lista_num[i-1] != lista_num[i]:
            dicio[lista_num[i-1]] = lista_num.count(lista_num[i-1])
    fich.close()
    print(dicio)


# Exercicio 7.13
def dados_pessoais(fname1, fname2):
    dicio_prof = {102: "Professor", 411: "Advogado", 203: "Estudante"}
    dicio_estado = {1: "Casado", 2: "Solteiro", 3: "Viuvo", 4: "Separado"}
    fich_base = open(fname1, 'r')
    fich_trans = open(fname2, 'w')
    lista = fich_base.readlines()
    lista_pessoas = []
    for i in range(len(lista)):
        aux = lista[i].split()
        lista_pessoas.append(aux)
    for i in range(len(lista_pessoas)):
        info = ''
        info += lista_pessoas[i][0][0] + lista_pessoas[i][1][0] + ' ' + lista_pessoas[i][2] + ' ' + dicio_prof.get(int(lista_pessoas[i][3])) + ' ' + dicio_estado.get(int(lista_pessoas[i][4])) + '\n'
        fich_trans.write(info)
    fich_base.close()
    fich_trans.close()


if __name__ == '__main__':
    # primeiro()
    # seq_ficheiro(0, 15)
    # linha_data('2 de dezembro de 2020\n')
    # numeros('ficheiros_aula/primeiro.txt')
    # copia_fich('ficheiros_aula/primeiro.txt', 'ficheiros_aula/primeiro_copia.txt')
    # desenha_coord("ficheiros_aula/exercicio7.txt", 4)
    # gerir_vendas("ficheiros_aula/exercicio11_base.txt", "ficheiros_aula/exercicio11_gestor.txt")
    # int_repetidos("ficheiros_aula/exercicio12.txt")
    dados_pessoais("ficheiros_aula/exercicio13_base.txt", "ficheiros_aula/exercicio13_trans")
