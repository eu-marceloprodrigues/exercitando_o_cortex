#6. **Fatorial** ✨: Calcule o fatorial de um número.
#Como calcular fatorial um número inteiro positivo n (representado por n!), você multiplica n por 
#todos os números inteiros positivos menores que ele, até chegar ao número 1.
#Por exemplo, 5! (cinco fatorial) é 5 x 4 x 3 x 2 x 1, que resulta em 120. 

print("CALCULADORA DE FATORIAL!!!\n")
numero=int(input("Insira um número maior que 0: \n"))

fatorial = 1
while numero >= 1:
    fatorial = numero*fatorial
    numero -= 1
print("Valor fatorial: ", fatorial)