# 8. **Números Primos** 🧮: Verifique se um número é primo.
# Números primos são divisiveis por 1 e ele mesmo
import math

def verifica_n_primo(numero):
    #Verifica se um número é primo.
    if numero < 2:
        return False
    #Não precisamos verificar divisores maiores que a raiz quadrada
    for n in range(2, int(math.sqrt(numero))+1):
        if numero % n == 0:
            return False
    return  True
    

#------------------------------------------------------------------------------------------------------------------------#
print("!!!VERIFICADOR DE NÚMEROS PRIMOS!!!!")
numero= int(input("Insira um valor: \n"))

validacao = (verifica_n_primo(numero))

if validacao == True:
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")

