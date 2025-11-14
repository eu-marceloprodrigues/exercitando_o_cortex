# 19. **Contagem de Vogais** 💬: Conte o número de vogais em uma string.

# recebe palavra a ser verificada
palavra = (input("Insira o texto a ser verificado aqui:\n"))

# Deixa texto em minusculo
palavra = palavra.lower()

contador = 0
vogais = 'aiueo'

for letra in palavra:
        if letra in vogais:
            contador += 1

print(f"Texto digitado: {palavra}\nTotal de vogais: O total de vogais é: {contador}")
