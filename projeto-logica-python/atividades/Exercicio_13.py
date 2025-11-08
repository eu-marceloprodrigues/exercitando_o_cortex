#13. **Máximo e Mínimo** 📊: Encontre o maior e o menor número de uma lista.
lista = []
i = 0
while i < 5:
    try:
        valor = input("Insira um numero: ")
        
        if valor.isdigit():
            lista.append(valor)
            i = i+1
        else:
            print("Entrada inválida. Por favor, digite apenas números.")
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")

print(f"Os números escolhidos foram{lista}.\nO maior valor da lista é: {max(lista, key=int)}\nO menor valor da lista é {min(lista, key=int)} ")
