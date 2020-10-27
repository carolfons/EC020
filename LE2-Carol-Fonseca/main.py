import numpy as np
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#Exercícios Propostos de EC020

#Exercício01
def ex01():
#criando a tupla
    numExtenso = ('um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')
#entrada de dados
    num = int(input("Entre com qualquer número de 1-10"))
    aux = 1


    for nomes in numExtenso:
        if (aux == num):
            print(numExtenso[aux-1])
            break
        else:
            aux = aux+1

def ex02():
    num1 = int(input('Entre com o primeiro valor: '))
    num2 = int(input('Entre com o segundo valor: '))
    num3 = int(input('Entre com o terceiro valor: '))
    num4 = int(input('Entre com o quarto valor: '))

    t = (num1, num2, num3, num4)

    nove = t.count(9)

    print()
    if nove > 0 :
        print('O número 9 apareceu {} vez(es) na tupla'. format(nove))
    else:
        print("O número 9 não aparece na tupla")
    print()
    if 3 in t:
        pos = t.index(3)
        print("o valor 3 está na posição: ", pos)

def ex03():
    lista = []

    for a in range(0,5):
        num = int(input('Entre com o valores numéricos: '))
        lista.append(num)

    valorMax = max(lista)
    valorMin = min(lista)

    pos1 = lista.index(valorMax)
    pos2 = lista.index(valorMin)

    print("O maior valor dessa lista é: {} e sua posição é: {}".format(valorMax,pos1))
    print("O menor valor dessa lista é: {} e sua posição é: {}".format(valorMin, pos2))


def ex04():

    lista = []
    cont = 0
    while True:
        num= input('Entre com um valor numérico (digite uma letra para sair):')

        if num.isalpha():
            break
        else:
            num = int(num)
            lista.append(num)

    for i in range(len(lista)):
        cont+=1

    print()
    print("Foram digitados {} números.".format(cont))
    print("A lista em ordem decrescente: ")
    lista.reverse()
    print(lista)
    resultado = 5 in lista

    if resultado == True:
        print("O valor 5 está na lista")
    else:
        print('O valor 5 não está na lista')


def ex05():
    lista = []
    listaPar = []
    listaImpar = []
    while True:
        num = input('Entre com um valor numérico (digite uma letra para sair):')

        if num.isalpha():
            break
        else:
            num = int(num)
            lista.append(num)

    for i in range(len(lista)):
        if lista[i] %2 == 0:
            listaPar.append(lista[i])
        else:
            listaImpar.append(lista[i])

    print()
    print('Lista par: ', listaPar)
    print('Lista Impar: ', listaImpar)
    print("Lista Original: ",lista)

def ex06():
    nome = input("Entre com o nome do jogador: ")
    partidas = int(input("Entre com quantas partidas ele jogou: "))
    gols = 0


    for i in range(0,partidas):
        gol = int(input("Entre com quantos gols ele fez no {} jogo: ".format(i+1)))
        gols = gols+gol

    totalGols = partidas*gols

    #criando o dicionario
    jogador = {
        'nome': nome,
        'partidas': partidas,
        'gols': gols,
        'totalDeGols': totalGols
    }

    #qtdGols = jogador['partidas']*jogador['gols']

    #varrendo o dicionário e mostrando as infos
    for k, v in jogador.items():
        print('{} : {}'.format(k, v))

def ex07():
    dados1 = {'nome': 'Carla', 'idade': 10, 'sexo': 'F'}
    dados2 = {'nome': 'Jose', 'idade': 20, 'sexo': 'M'}
    dados3 = {'nome': 'Ana', 'idade': 30, 'sexo': 'F'}
    dados4 = {'nome': 'Felipe', 'idade': 40, 'sexo': 'M'}
    somatorio = 0
    pessoas = [dados1, dados2, dados3, dados4]
    lista_mulheres = []
    lista_acima_media = []
    print(str(len(pessoas)) + " pessoas")

    for cont in range(0, len(pessoas)):
        somatorio = somatorio + pessoas[cont]['idade']

        if pessoas[cont]['sexo'] == 'F':
            lista_mulheres.append(pessoas[cont]['nome'])

    media = somatorio / len(pessoas)

    for cont in range(0, len(pessoas)):
        if pessoas[cont]['idade'] > media:
            lista_acima_media.append(pessoas[cont]['nome'])

    print("media = " + str(media))
    print(lista_mulheres)
    print(lista_acima_media)

def ex08():
    matriz = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
    lista = []
    lista = matriz.shape
    print(lista)
    if lista[0] % 2 == 0:  # n de linhas do shape par
        print("PAR")
        array_par = np.arange(lista[1])
        print(array_par)
    else:
        array_impar = np.linspace(0, 100, matriz.size)
        print(array_impar)

def ex09():
    arr = np.array(['Caroline','Victória','Sarah','Roberto','Zuko'])
    arr2 = np.array(['Kiara','Luana','Luiza','Gabrielle','Marisa'])
    arrayOrd = np.concatenate((arr,arr2))
    print()
    print("Array ordenado: ", np.sort(arrayOrd))
    print()
    mtz = arrayOrd.reshape(5,2)
    print('Array 2-d: ', mtz)

