 #Lista de Exercícios

#Ex 01

def exercicio01():
   valor = input("Entre com um valor: ")

   if(valor.isnumeric() == True):
      print("O valor é composto apenas de números!")
   elif(valor.isalpha() == True):
      print("O valor é composto apenas de letras!")
   else:
      print("O valor é composto de números e letras!")


#Exercicio 02

def ex02():
   num = int(input("Entre com um número: "))
   num1 = num+1
   num2 = num-1
   print("O número seguinte é {} e o número anterior é {}".format(num1,num2))

#Exercício 03

def exercicio03():
   preco = float(input("Entre com o preço do produto: "))
   novoPreco = preco - preco*(10/100)
   print("O novo preço é de R$%.2f reais" %novoPreco)

#Exercicio 04

def exercicio04():
   m = (float(input("Entre com um valor em metros: ")))
   cm = m*100
   mm = m*1000

   print("O valor em metros é %.2fm, em centímetros é %.2fcm e em milímetros é %.2fmm" %(m,cm,mm))

#Exercício 05
def exercicio05():
   largura = int(input("Entre com a largura da parede: "))
   altura = int(input("Entre com a altura da parede: "))

   area = largura*altura
   tinta = area/2

   print("Area da parede é de {} m²".format(area))
   print("A quantidade de tinta necessária é de {} litros".format(tinta))

#Exercício 06
def exercicio06():
   num = int(input("Entre com o número: "))

   unidade = num%10
   dezena = (num%100)//10
   centena = (num%1000)//100
   milhar = (num//1000)


   print("O numero digitado foi: {}".format(num))
   print("valor do milhar: {}".format(milhar))
   print("O valor da centena: {} ".format(centena))
   print("O valor da dezena: {}".format(dezena))
   print("O valor da unidade: {}".format(unidade))

#Exercício 07

def exercicio07():
   nome = input("Entre com o nome: ")
   if("da Silva" in nome):
      print("O nome possui 'da Silva'")
   else:
      print("O nome não possui 'da Silva'")

#exercício 08
def exercicio08():
   velocidade = int(input("Entre com a velocidade: "))

   if(velocidade == 80):
      print("Boa Viagem!")
   else:
      e = velocidade - 80
      multa = e*50
      print('Multado no valor de {}'.format(multa))

#Exercício 09
def exercicio09():
   num = int(input("Entre com o número: "))
   if(num%2==0):
      print("O número {} é par".format(num))
   else:
      print("O número {} é impar".format(num))


#Exercício 10
def exercicio10():
   km = int(input("Entre com a distância da viagem em km: "))

   if(km<200):
      valor = km*0.5
   else:
      valor = km*0.45

   print("O preço da passagem será de R$%.2f" %valor)

#Exercício 11
def exercicio11():

   numero = []

   numero.append(int(input("Entre com o primeiro número: ")))
   numero.append(int(input("Entre com o segundo número: ")))
   numero.append(int(input("Entre com o terceiro número: ")))

   print("O maior valor é:", max(numero))
   print("O maior valor é:", min(numero))

#Exercício 12
def exercicio12():

   sal = float(input("Entre com o salário: "))
   if(sal>1500):
      sal=sal+(sal*10/100)
   else:
      sal = sal+(sal*15/100)

   print("Você receberá R$%.2f"%sal)

#Exercicio 13
def exercicio13():
   ano = int(input("Entre com o ano de nascimento: "))
   idade = 2020-ano

   if(idade<=9):
      print("MIRIM")
   elif(idade<=14):
      print("INFANTIL")
   elif(idade<=19):
      print("JÚNIOR")
   else:
      print("MASTER")

#Exercicio 14
def ex14():
   peso = float(input("Entre com o peso: "))
   altura = float(input("Entre com a altura: "))

   imc = peso/(altura*altura)

   if(imc<18.5):
      print("Abaixo do peso")
   elif(imc<25):
      print("Peso Ideal")
   elif(imc<30):
      print("Sobrepeso")
   else:
      print("Obesidade Mórbida")

#Exercicio 15
def ex15():
   pag = int(input("Entre com o valor: "))
   forma = input("Entre com a forma de pagamento: ")

   if("à vista" in forma or "a vista" in forma or "À vista" in forma):
      valor = pag-(pag*10/100)
      print("O novo preço é de R$%.2f" %valor)
   elif("Cartão á vista" in forma or "cartao a vista" in forma):
      valor = pag-(pag*5/100)
      print("O novo preço é de R$%.2f" %valor)
   else:
      valor = pag+(pag*15/100)
      print("O novo preço é de R$%.2f" % valor)

#Exercício 16
def ex16():

   soma = 0
   for i in range(1,7):

      num = int(input("Entre com o número: "))
      if(num%2==1):
         soma = soma+num
   print("O resultado é: ", soma)

#Exercicio 17
def ex17():
   aux=0
   for c in range(0,5):
      ano = int(input("Entre com o ano de nascimento: "))
      idade = 2020-ano
      if(idade>18):
         aux=aux+1
   print("A quantidade de pessoas maior de idade é: ", aux)

#Exercicio 18
def ex18():

   peso = []
   for i in range(0,5):
      peso.append(float(input("Entre com o peso: ")))

   print("O maior peso é: ", max(peso))
   print("O menor peso é: ", min(peso))

#exercicio 19
def ex19():
   maiorIdade = 0
   menorIdade = 0
   media = 0
   maisVelho = ''

   n = 1
   aux = 0

   while n != 0:
      nome = str(input("Entre com o nome: "))
      idade = int(input("Entre com a idade: "))
      sexo = str(input("Informe o seu sexo (Masc ou Fem): ").lower())

      if(idade>maiorIdade and sexo == 'masc'):
         maioridade = idade
         maisVelho = nome
      elif(idade <= 20 and sexo == 'fem'):
         menorIdade +=1

      media += idade

      aux +=1

      n = int(input("Deseja continuar? (1-Sim | 0-Não)"))

   print('\n')
   print("A idade média do grupo é: {}"
         "\nO homem mais velho é: {}"
         "\nA quantidade de mulheres com menos de 20 anos é: {}".format(media/aux,maisVelho,menorIdade))

#Exercicio 20
def ex20():
   num1 = int(input("Entre com o primeiro número: "))
   num2 = int(input("Entre com o segundo número: "))
   num = 0

   while num != 4:
      print("-------------------------------------------")
      print("1 - Somar")
      print("2 - Multiplicar")
      print("3 - Qual é o maior número")
      print("4 - Sair do programa")
      num = int(input("Entre com a opção: "))
      print("--------------------------------------------")
      if (num == 1):
         print("A soma é: {}".format(num1 + num2))
      elif (num == 2):
         print("A multiplicação é {}".format(num1 * num2))
      elif(num == 3):
         if(num1>num2):
            print("O primeiro número é maior que o segundo")
         else:
            print("O segundo número é maior que o primeiro")


   print("Fim do programa!")

def main():
   aux = 0
   while aux != 21:
      print("--------------------------------")
      print("Qual exercício deseja visualizar?")
      print("1 - Exercício 01")
      print("2 - Exercício 02")
      print("3 - Exercício 03")
      print("4 - Exercício 04")
      print("5 - Exercício 05")
      print("6 - Exercício 06")
      print("7 - Exercício 07")
      print("8 - Exercício 08")
      print("9 - Exercício 09")
      print("10 - Exercício 10")
      print("11 - Exercício 11")
      print("12 - Exercício 12")
      print("13 - Exercício 13")
      print("14 - Exercício 14")
      print("15 - Exercício 15")
      print("16 - Exercício 16")
      print("17 - Exercício 17")
      print("18 - Exercício 18")
      print("19 - Exercício 19")
      print("20 - Exercício 20")
      print("21 - Exercício 21")
      aux = int(input("Sair do programa!"))
      print("----------------------------------")

      if(aux == 1):
         exercicio01()
      elif(aux == 2):
         ex02()
      elif(aux == 3):
         exercicio03()
      elif(aux == 4):
         exercicio04()
      elif(aux == 5):
         exercicio05()
      elif(aux==6):
         exercicio06()
      elif(aux==7):
         exercicio07()
      elif(aux==8):
         exercicio08()
      elif(aux==9):
         exercicio09()
      elif(aux==10):
         exercicio10()
      elif(aux==11):
         exercicio11()
      elif (aux == 12):
         exercicio12()
      elif (aux == 13):
         exercicio13()
      elif (aux == 14):
         ex14()
      elif (aux == 15):
         ex15()
      elif (aux == 16):
         ex16()
      elif(aux==17):
         ex17()
      elif (aux == 18):
         ex18()
      elif (aux == 19):
         ex19()
      elif (aux == 20):
         ex20()
      else:
         print("Fim do programa!")

main()

