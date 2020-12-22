import numpy as np
import pandas as pd

#   lendo o dataset
dfPaises = pd.read_csv('paises.csv', delimiter = ';')

#   VALORES DAS COLUNAS
#colunas = dfPaises.columns.values
#print(colunas)

def ex01():
#   Separando o dataFrame em apenas páises que contém oceania
    oceania = dfPaises[dfPaises['Region'].str.contains('OCEANIA')]
#   Paises da Oceania:
    print(oceania['Country'])
#   Pegando o tamanho do df
    qtdOceania = len(oceania)
#   Qunatidade de países da Oceania
    print(qtdOceania)
    print()

def ex02():
#   Separando uma tabela da população mundial
    population = dfPaises['Population']
#   procurando o país com a maior população usando a função .max() e formando um df
    maiorPop = dfPaises[dfPaises['Population']== population.max()]
#   Separando as colunas de país e região
    pais_regiao = ['Country','Region']
#   printando apenas as colunas selecionadas
    print(maiorPop.filter(items = pais_regiao))
    print()

def ex03():
#   Agrupando o df em regiões
    dfRegion = dfPaises.groupby('Region')
#   calculando a média com a função .describe() no df de Regiões
    media = dfRegion.describe()
#   Separando apenas a coluna de média
    mean = media['Literacy (%)']['mean']
#   saída de dados
    print(mean)
    print()

def ex04():
#   Separando um df apenas com países com coastline = 0
    noCoast = dfPaises[dfPaises['Coastline (coast/area ratio)'] == 0]
#   Criando um novo arquivo
    noCoast.to_csv('noCoast.csv', sep=';', header=True)
#   Lendo o novo df
    dfNoCoast = pd.read_csv('noCoast.csv', delimiter = ';')


def ex05():
    def humanHelp (Deathrate):
        if(Deathrate<9):
            return('Balanced')
        else:
            return('Urgent')

#   criando a nova coluna no df
    dfPaises['Humanitarian Help'] = dfPaises['Deathrate'].apply(humanHelp)
#   verificando se foi inserido no cabeçãlho do df
    print(dfPaises.head(0))

