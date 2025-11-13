lista_notas = []

i = 0

# Verificação de entrada
try:
    while i <= 5:
        # verifica nota, se foi digitado uma nota maior que 10 ou qualquer caractere que nao seja numero
        nota = input("Insira o valor da nota: \n")
        if nota.isdigit() and int(nota) <= 10:
            entrada = float(nota)
            lista_notas.append(entrada)
            i = i+1
        else:
            print("Erro, insira uma nota valida: ")
except ValueError as erro:
    print(f"Erro critico {erro}")

# Calculo da media
soma_notas = sum(lista_notas)
media_nota = soma_notas/ len(lista_notas)

print(f"A soma total das notas é: {soma_notas}\nA média total das notas é de: {media_nota :.2f}") # < -- aplica limitação decimal