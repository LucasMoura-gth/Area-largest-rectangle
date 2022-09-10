#Nome: Lucas Moura de Almeida

#Problema: Dada uma matriz binária 2D de tamanho MxN preenchida com '0' (zero) e '1' (um), 
# encontre o retângulo de maior área contendo apenas '1' e retorne o valor de sua área


#Bibliotecas

import numpy as n
import math as m
import random

#Gerador da Matriz Binária 2D

lines = random.randint(1,20)
print(lines)
columm = random.randint(1,20)
print(columm)

if lines == columm:
    columm = random.randint(1,20)


#Inicializando a matriz
matrix = n.zeros((lines,columm))

#Randomizando os valores dentro da matriz (0 e 1)
for i in range(0,columm,1):
    for j in range(0,lines,1):
        matrix[j,i] = random.randint(0,1)


#Processo de análise da matriz
#matriz exemplo cuja resposta é 6 (4x5)
#matrix = n.array([[1, 1, 0, 1, 1], [1, 1, 0, 0, 1],[1, 1, 0, 1, 1], [1, 1, 1, 1, 1]])
print(matrix)
lines = lines
col = columm
count = 0
line_2 = lines

aux = n.zeros((lines,col))

#Gerador de Histograma

for l in range(0, line_2, 1):
    for j in range(0, col, 1):
        for i in range(lines-1,-1,-1):
            if matrix[i,j] == 1:
                count = count + 1
            else:
                break
        aux[l,j] = count
        count = 0
    lines = lines - 1

print(aux)

area = 0
st = [-1]


for m in range(0, line_2, 1):
    for k in range(0, col,1):
        while st[-1] != -1 and aux[m, st[-1]] >= aux[m, k]:
            H = aux[m, st.pop()]
            W = k - st[-1] -1
            area = max(area, H*W)
        st.append(k)
    while st[-1] != -1:
        H = aux[m, st.pop()]
        W = col - st[-1] -1
        area = max(area, H*W)

print("Max area:", area)

#To-do list

#Texto
#O intuito do presente projeto é desenvolver um algoritmo capaz de obter uma matriz aleatória
#e calcular a maior área contendo apenas "1"
#Primeiramente iniciou-se o processo gerando aleatoriamente os valores da linhas e colunas da matriz MxN
#confome mostrado por meio do código abaixo, limitando o número em até 20, contudo podendo ser livremente
#modifica e a condicional foi colocada para garantir que
#M seja diferente de N, caso queira determinar uma matriz quadrada, simplesmente comentar a condicional
# se utilziando de "#" é o suficiente, de maneira a não comprometer o bom funcionamento do programa
#Em seguida foi inicializada a variável matrix de dimensões MxN, como se trata de uma matriz binária
#optou por povoar a matriz com zeros e uns aleatoriamente, sendo mostrado abaixo a parte relevante
#do código, relativa a esta etapa

#A abordagem de análise tomada foi por meio da contagem de de todos os "1" da última linha para a primeira
#sendo contabilizado "+1" ao passo que se encontra "1" e parada a contagem ao passso que se encontra zeros
#assim é possível, não somente identificar  a quantidade de "1" na linhas acima, como também temos a 
#posição relativa de cada elemento

#Dando sequência, basicamente obtem-se, uma matriz secundária, chamada de "aux" no código apresentado
#que precisamente guarda as quantidade, conforme supracitado

#Por fim chega-se ao último passo, determinar a máxima área. Com a quantidade e posições, gera-se 
#histogramas com cada linha da matriz "aux", para melhor exemplificar, o processo é mostrado 
#por meio da Figura 1

#Agora o problema se tornou relativamente mais simples, sendo a área máxima encontrada, determinando
#a máxima área dos histogramas
#Para finalizar explica-se melhor o código que realiza este calculo mostrado abaixo:

#for m in range(0, line_2, 1):
    #for k in range(0, col,1):
        #while st[-1] != -1 and aux[m, st[-1]] >= aux[m, k]:
            #H = aux[m, st.pop()]
            #W = k - st[-1] -1
            #area = max(area, H*W)
        #st.append(k)
    #while st[-1] != -1:
        #H = aux[m, st.pop()]
        #W = col - st[-1] -1
        #area = max(area, H*W)

#Utilizando um estruturamento linear de dados, mantido pela váriavel st, calcula-se largura e comprimento
#dos retângulos, primeiro passo é garantir que todos os histograma sejam rodados, para isso
#programou-se dois loops, inicialmente rodando a linha e posteriormente rodando as colunas que serão
#analisadas. Ao adentrar no histograma proposto a váriavel st é inicializado como -1, para que 
#se possa analisar os extremos do histograma
#O que foi chamado de primeira condicional é rodada N vezes, de maneira que caso a condição imposta, de
#se o último elemento de st for igual a 1 e 

#Algorithm:

#Initialise a stack S.
#Push the first index of A[] into the stack.
#Traverse through the array A[] and compare the height of A[i] with the height at the top of the stack.
#If the height is:
#Greater than A[S.top()], push it into the stack.
#Less than A[S.top()], keep popping the elements until A[i] >= A[S.top()].
#Keep maximizing the area while popping the elements from the stack.
#Push the index i for each element.
#Return the maximum element.

#The idea is similar to finding the Next Greater element using stack. 
#In this problem, instead of finding the next greater element, 
#we will maintain two arrays left[] and right[] denoting the smaller elements 
#on the left and right