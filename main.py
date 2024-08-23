#Felipe Trezub Bueno

from webbrowser import open_new

def uniao(conj1, conj2):
    resultado = conj1.union(conj2)
    print(f'União:\n conjunto 1 {conj1},\n conjunto 2 {conj2}.\n Resultado: {resultado}')

def interseccao(conj1, conj2):
    resultado = conj1.intersection(conj2)
    print(f'Intersecção:\n conjunto 1 {conj1},\n conjunto 2 {conj2}.\n Resultado: {resultado}')

def diferenca(conj1, conj2):
    resultado = conj1.difference(conj2)
    print(f'Diferença:\n conjunto 1 {conj1}, \n conjunto 2 {conj2}.\n Resultado: {resultado}')

def produto_cartesiano(conj1, conj2):
    resultado = {(x, y) for x in conj1 for y in conj2}
    print(f'Produto Cartesiano:\n conjunto 1 {conj1},\n conjunto 2 {conj2}.\n Resultado: {resultado}')


with open('Discreto1.txt', 'r') as arquivo:
    linhas = [linha.strip() for linha in arquivo]

num_operacoes = int(linhas[0])
indice = 1

for _ in range(num_operacoes):
    operacao = linhas[indice]
    conjunto1 = set(linhas[indice + 1].split(','))
    conjunto2 = set(linhas[indice + 2].split(','))
    indice += 3

    if operacao == 'I':
        interseccao(conjunto1, conjunto2)
    elif operacao == 'U':
        uniao(conjunto1, conjunto2)
    elif operacao == 'D':
        diferenca(conjunto1, conjunto2)
    elif operacao == 'C':
        produto_cartesiano(conjunto1, conjunto2)

