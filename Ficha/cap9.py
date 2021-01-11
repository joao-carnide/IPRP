# Capítulo 9 - Recursividade
import math


# Somatorio de numeros inteiros positivos até N
# sem recursividade
def somatorio_srec(N):
    soma = 0
    for i in range(1, N+1):
        soma += i
    return soma

# com recursividade
def somatorio_crec(N):
    if N == 1:
        return 1
    else:
        return N + somatorio_crec(N-1)


# Exercicio 9.2
def produto_escalar(V, W):
    if len(V) == 0:
        return 0
    else:
        return (V[0] * W[0]) + produto_escalar(V[1:], W[1:])


# Exercicio 9.3
def exponencial(x, n):
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            return exponencial(x, n//2) * exponencial(x, n//2)
        else:
            return exponencial(x, n//2) * exponencial(x, n//2) * x


# Exercicio 9.5
def incluido(conj_p, conj_g):
    # caso base: se conjunto pequeno for vazio
    if not conj_p:
        return True
    else:
        if conj_p[0] not in conj_g:
            return False
        else:
            return incluido(conj_p[1:], conj_g)


# Exercicio 9.6
def intersecao(conj_p, conj_g):
    if not conj_p:
        return []
    elif conj_p[0] in conj_g:
        return [conj_p[0]] + intersecao(conj_p[1:], conj_g)
    else:
        return intersecao(conj_p[1:], conj_g)


if __name__ == '__main__':
    # print(somatorio_srec(3))
    # print(somatorio_crec(3))
    # print(produto_escalar([1, 2, 3], [4, 5, 6]))
    # print(exponencial(2, 6))
    # print(incluido([2, 4], [1, 2, 3, 4]))
    print(intersecao([2, 4, 20], [1, 2, 3, 4]))
