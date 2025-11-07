#2. **Números e Operações Básicas** ➕➖✖️➗: Calcule a soma, subtração, multiplicação e divisão de dois números.
#######################FUNÇÕES#####################################################################################

def soma(numero1,numero2):
    print("O resultado desta operação é:", numero1+numero2)

def subtracao(numero1,numero2):
    print("O resultado desta operação é:", numero1-numero2)

def multiplicacao(numero1,numero2):
    print("O resultado desta operação é:", numero1*numero2)

def divisao(numero1,numero2):
 print("O resultado desta operação é:", numero1/numero2)

 ###########################PROGRAMA###############################################################################

numero1 = int(input("Insira o primeiro numero: "))
numero2 = int(input("Insira o segundo numero: "))

opcao = int(input("Insira a operação desejada:\n1-SOMA\n2-SUBTRAÇÃO\n3-MULTIPLICACAO\n4-DIVISAO\n"))

if opcao == 1:
    print("Opção selecionada: SOMA\n")
    soma(numero1, numero2)
if opcao == 2:
    print("Opção selecionada: SUBTRAÇÃO\n")
    subtracao(numero1, numero2)
if opcao == 3:
    print("Opção selecionada: MULTIPLICACÃO\n")
    multiplicacao(numero1, numero2)
if opcao == 4:
    print("Opção selecionada: DIVISÃO\n")
    divisao(numero1, numero2)        

