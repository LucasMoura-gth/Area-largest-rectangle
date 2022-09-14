#Nome: Lucas Moura de Almeida | E-mail: lucas.moura020@gmail.com

#Bibliotecas
import numpy as n
import math as m
import random

#Gerador da Matriz Binária 2D
lines = random.randint(1,20) #Quantidade de Linhas
col = random.randint(1,20) #Quantidade de Colunas

#Condicional Matriz MxN (M != N)
#if lines == col:
    #col = random.randint(1,20)

#Declaração da variável - Matriz Inicial
matrix = n.zeros((lines,col))

#Geração aleatória de 0 e 1's para os elementos de uma matriz
for i in range(0,col,1):
    for j in range(0,lines,1):
        matrix[j,i] = random.randint(0,1)


#Processo de análise da matriz
print("\nMatriz Inicial:\n" "\n{}".format(matrix))

count = 0 #contador
line_aux = lines #parâmetro auxiliar da quantidade de linhas
aux = n.zeros((lines,col)) #Declaração da matriz auxiliar para dados do Histograma

#Gerador de Histograma
for l in range(0, line_aux, 1):
    for j in range(0, col, 1):
        for i in range(lines-1,-1,-1):
            if matrix[i,j] == 1:
                count = count + 1
            else:
                break
        aux[l,j] = count
        count = 0
    lines = lines - 1


#Declaração da variáveis área e de uma lista (st)
area = 0
st = [-1]

#Método para determinar maior área em um histograma
for m in range(0, line_aux, 1):
    for k in range(0, col,1):
        #Caso1: Lista possui elemento e o módulo do próximo elemento é maior
        while st[-1] != -1 and aux[m, st[-1]] >= aux[m, k]:
            H = aux[m, st.pop()]
            W = k - st[-1] -1
            area = max(area, H*W)
        #Inserir índice de elemento na lista
        st.append(k)
    #Caso2: Lista possui elemento e seu módulo é menor que o anteriormente analisado
    while st[-1] != -1:
        H = aux[m, st.pop()]
        W = col - st[-1] -1
        area = max(area, H*W)

print("\n Área máxima encontrada: {}". format(area))

