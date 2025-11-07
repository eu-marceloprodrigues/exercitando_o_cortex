#10. **Inversão de String** 🔄: Inverta uma string.
frase = str(input("Digite uma frase, vamos inverte-la para voce: "))
frase_invertida = frase[::-1]
 #A sintaxe [::-1] cria uma fatia (slice) da string que começa no 
#fim, vai até o começo e tem um passo de -1, invertendo a ordem dos caracteres. 
print(f"A sua frase invertida fica: {frase_invertida}")