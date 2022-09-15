# **Avaliação de desenvolvimento**

O presente programa visa solucionar o seguinte problema: Dada uma matriz binária 2D de tamanho MxN preenchida com '0' (zero) e '1' (um), encontre o retângulo de maior área contendo apenas '1' e retorne o valor de sua área

<p align="center">
  <img width="401" height="207" src="https://i.imgur.com/sRybxrW.png">
</p>



# Solução

Conforme supracitado, o intuito do presente problema é obter a maior área contendo apenas '1' de uma matriz MxN. Primeiramente inciou-se o processo gerando aleatoriamente, com uso da função random, a quantidade de linhas e colunas da matriz, assim como os valores dos elementos (0 e 1), de modo a garantir a universalidade do algoritmo, ou seja, uma tentativa de reproduzir a aleatoriedade que é apresentado no universo. Como forma de facilitar a apresentação dos dados, da matriz e da maior área, limitou as quantidades possíveis de linhas e colunas em 20, contudo é possível facilmente modificá-lo e aumentar ou diminuir conforme a necessidade



```python
lines = random.randint(1,20) #Quantidade de Linhas

col = random.randint(1,20) #Quantidade de Colunas

#Geração aleatória de 0 e 1's para os elementos de uma matriz

            for i in range(0,col,1):
              for j in range(0,lines,1):
                       matrix[j,i] = random.randint(0,1)

```



Vale-se ressaltar que o processo garante tanto que M seja diferente de N, como seja igual, no programa foi feita uma condicional, a fim de garantir que somente os casos em que M é diferente de N sejam analisados, caso se apresente tal necessidade, o simples fato de retirar o termo de comentário (#) permite que as duas linhas sejam computadas.



```python
#Condicional Matriz MxN (M != N)
              #if lines == col:
#col = random.randint(1,20)

#: Simbologia que apresenta um comentário em meio ao código


```



Em seguida após inicializada a variável matrix (*matrix = n.zeros((lines,col))*), uma matriz de MxN, a abordagem de análise tomada foi por meio da contagem de todos os “1” partindo da última linha da matriz até a primeira, de modo que foi contabilizado +1 ao passo que se encontra uns e a contagem é parada ao passo que se encontra zeros, fato este que permite, não somente identificar a quantidade de “1”, como também suas posições relativas e para dar a devida sequência, declarou-se uma matriz secundária, chamada de “aux” que guarda as quantidades de “1” presentes, de modo que o código. Isso permite gerar histogramas com cada linha da matriz auxiliar, portanto o problema se torna relativamente mais simples, sendo a área máxima determinada pela máxima área presente nos histogramas.



```python
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


```



Como processo final declara-se a váriavel “*st*”, uma lista de valores, que servirá para a análise do processo, conforme caminha-se da esquerda para a direita e posteriormente da direita para a esquerda, comparando as alturas e possibilidades de áreas, é colocado dentro dessa lista os índices dos valores, ou seja, os valores relativos a uma determinada coluna, que são retirados ou colocados com base na comparação entre os módulos dos valores correspondentes ao índice em questão. Ou seja, o loop realizado analisa linha a linha da matriz auxiliar, compara os módulos, em outras palavras, as alturas de cada barra do histograma, passa por duas condições, sendo averiguado se a barra é maior ou igual a posterior, caso não seja dá-se continuidade até encontrar o elemento que satisfaça a relação, com isso é possível maximizar a área, portanto determinando a maior área possível presente na matriz



```python
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

#pop(): comando utilizado para retirar o último elemento
#append(): comando utilizado para inserir os índices


```
