#11. **Palíndromo** 🔁: Verifique se uma string é um palíndromo.
# Uma string palídroma é uma string que se lida ao contrário tem o mesmo significado que 
# se lida normalmente

# recebe a palavra 
frase = str(input("Insira uma palavra: "))

# comando trata frase: torna todas letras minusculas, remove espaço em caracteres 
#ajudar a verificar se um caractere é alfanumérico (letra ou número).
frase = "".join(caractere for caractere in frase.lower() if caractere.isalnum())

# inverte o texto
frase_invertida = frase[::-1]

# verifica e exibe resultado
if frase == frase_invertida:
    print("A frase é palimdroma")
else:
    print("A frase nao é palimdroma")