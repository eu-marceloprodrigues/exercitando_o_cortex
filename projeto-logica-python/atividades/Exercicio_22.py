# 22. **Anagramas** 🔠: Verifique se duas strings são anagramas.
try:
    #Pede duas strings
    primeira_palavra = input("Insira uma palavra: \n")
    segunda_palavra = input("Insira outra palavra: \n")

    primeira_palavra = primeira_palavra.lower().replace(" ","")
    segunda_palavra = segunda_palavra.lower().replace(" ","")

    #Deixa letras em minusculo e ordena caracteres, fazendo comparação.
    if sorted(primeira_palavra) == sorted(segunda_palavra):
        print(f"As palavras {primeira_palavra} e {segunda_palavra}. Trata-se de um anagrama.")
    else:
        print(f"As palavras {primeira_palavra} e {segunda_palavra}. Não são um anagrama.")
except Exception as erro:
    print(f"Falha {erro}")
