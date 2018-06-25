#-*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Método 1
def metodo1(data, media):
    covariancia = 0
    # Cálculo das diferenças
    for i in data:
        diferenca = (i.reshape(6, 1) - media)
        covariancia += np.dot(diferenca, diferenca.T)

    # Calculando o produto
    covariancia = covariancia * (1.0 / float(len(data)))

    return covariancia

# Método 2
def metodo2(data, media):
    # Matriz de correlação
    correlacao = 0
    for i in data:
        correlacao += np.dot(i.reshape(6, 1), i.reshape(6, 1).T)
    correlacao *= (1.0 / float(len(data)))

    covariancia = (correlacao - np.dot(media, media.T))

    return  covariancia

# Método 3
def metodo3(data, media):
    # Matriz de correlação
    correlacao2 = 0
    for n in xrange(0, len(data)):
        x = data[n].reshape((6, 1))
        correlacao2 = (n / float(n + 1) * correlacao2) + ((1 / float(n + 1)) * np.dot(x, x.T))

    covariancia = (correlacao2 - np.dot(media, media.T))

    return covariancia

def plotarGrafico(linha, coluna, tipo):
    plt.scatter(x=linha, y=coluna, s=linha ,c='g')
    plt.xlabel("Linhas")
    plt.ylabel("Colunas")
    plt.title("Distribuicao dos coeficientes " + tipo)
    plt.axis([1,len(linha), 1, coluna[-1]])
    plt.show()

# Retorna o primeiro elemento positivo que a matriz tiver
def getPositivo(matriz):
    n = len(matriz)
    i = 0
    while i < n:
        j = 0
        while j < n:
            if matriz[i][j] > 0:
                return  (i,j)
            j += 1
        i += 1
# Retorna o primeiro elemento negativo que a matriz tiver
def getNegativo(matriz):
    n = len(matriz)
    i = 0
    while i < n:
        j = 0
        while j < n:
            if matriz[i][j] < 0:
                return (i, j)
            j += 1
        i += 1

# Lendo o arquivo
data = np.genfromtxt("coluna.dat", delimiter=",")

# Calculando a Matriz de Covariância pelos métodos

#Questão 1
# Matriz de covariância 1
matriz_cov = np.cov(data.transpose())

# Média geral
media = np.mean(data, axis=0).reshape((6, 1))

print  "\nQuestão 1 \n"
print "Método Padrão\n"
for linha in  matriz_cov:
    print linha


print "\nMétodo 1\n"
for linha in metodo1(data, media):
    print linha

print "\nMétodo 2\n"
for linha in metodo2(data, media):
    print linha

print "\nMétodo 3"
for linha in metodo3(data, media):
    print linha


#- O cálculo das matrizes de covariância através dos métodos diferem da matriz original somente na 12° casa decimal,
#assim podemos concluir com um arrendodamento que o resultado é igual para ambas.

# Questão 02
print  "\nQuestão 2 \n"

# Método 1
# A biblioteca Numpy não possui a função CORR..

# Método 2
cor_numpy = np.corrcoef(data.transpose())
print  "\nMétodo 2 - Matriz de Coeficientes de Correlação.\n"
for linha in cor_numpy:
    print linha

# Método 3
coeficientes = np.zeros((6,6))

# Utilizando a matriz de covariância do método 2
covariancia = metodo2(data, media)


for i in xrange(0,len(covariancia)):
    for j in xrange(0, len(covariancia)):
        d_i = [x for x in data[i]]
        d_j = [x for x in data[j]]
        coeficientes[i][j] = (covariancia[i][j] / (np.dot(np.std(d_i), np.std(d_j))))

print  "\nMétodo 3 - Matriz de Coeficientes de Correlação.\n"
for linha in coeficientes:
    print linha

# Questão 3

#- Baseado na análise da matriz de coeficientes gerada de acordo com a matriz de correlação da questão 2,
#foi posível analisar e obter os pares como segue.
#  Plotando os gráficos..

positivo = getPositivo(coeficientes)
negativo = getNegativo(coeficientes)


positivo_linha = [data[i][positivo[0]] for i in range(len(data))]
positivo_coluna = [data[i][positivo[1]] for i in range(len(data))]


#plotarGrafico(positivo_linha, positivo_coluna, "positivos")

negativo_linha = [data[i][negativo[0]] for i in range(len(data))]
negativo_coluna = [data[i][negativo[1]] for i in range(len(data))]

#plotarGrafico(negativo_linha, negativo_coluna, "negativos")

