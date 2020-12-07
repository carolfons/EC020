import numpy as np

#IMPORTANDO O DATASET spacee.csv
space = np.loadtxt('space.csv',
                   delimiter=';',#delimitador ;
                   dtype=str,#tipo string
                   encoding='utf-8')

#total de linhas: 4323
def ex01():
    qtd = 0
    qtdTotal = 0

    success = space[space[:,7]=='Success'].shape[0]
    total = space.shape[0]
    #varrendo o array
    perc = (success*100)/(total) #percentagem
    print(' A porcentagem de Sucessos foi de {} % ' .format(perc))


def ex02():
#   pegando um array apenas com as infos
    infos = space[1:]
#   separando apenas as missões com cost > 0
    custo = infos[space[1:,6].astype(np.float)>0]
#   formando um array apenas com os custos e transformando em float
    custo = custo[:,6].astype(np.float)
#   somando os custos
    custoTotal = np.sum(custo)
#   somando a quantidade de items no array
    missoes = np.size(custo)
#   calculando a média
    media = custoTotal/missoes
#   saída de dados
    print('A média de dastos de uma missão é: %.2f' %media )

def ex03():
    totalUsa = 0

#   criando um array cópia apenas com a coluna de Localização
    arrLocation = space[1:, 2].copy()
#   procurando os indices que possuem a string USA
    arrLocationUsa = np.char.find(arrLocation, 'USA')
#   somando o total de viagens realizadas pelos EUA
    for i in arrLocationUsa:
        if(i != -1):
            totalUsa += 1

#   saída de dados
    print("Os EUA realizaram um total de {} missões".format(totalUsa))

def ex04():
#   separando as informações apenas da empresa SpaceX
    spacex = space[space[:, 1] == 'SpaceX']
#   Separando apenas a coluna de custos e transformando de string em float
    custo = spacex[:, 6].astype(np.float)
#   pegando o maior custo usando a função max()
    custoMax = np.max(custo)
#   Saída de dados
    print( 'Maior custo de viagem %.1f' % custoMax )

def ex05():

#   formando um array apenas das empresas
    empresas = np.unique(space[:, 1])


#   for para ler as informações
    for empresa in empresas:
#       formando um array que conta quantas missões cada empresa fez
        num_missoes = space[space[:, 1] == empresa].shape[0]
#       saída de dados
        print('A empresa {} realizou {} missões'.format(empresa, num_missoes))
print("Exercício 01: ")
ex01()
print()
print("Exercício 02: ")
ex02()
print()
print("Exercício 03: ")
ex03()
print()
print("Exercício 04: ")
ex04()
print()
print("Exercício 05: ")
ex05()