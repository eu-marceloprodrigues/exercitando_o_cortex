# 14. **Ordenação** 📈: Implemente um algoritmo de ordenação (por exemplo, Bubble Sort).
# O que é bubble sort? -> Algoritmo simples que ordena valores de uma lista, onde o número maior sempre ira para
#as extremidades da lista.

# O que preciso fazer?

# 1 - Declarar lista
lista = []

# 2 - Inserir valores na lista
i = 0
while i < 5:
    try:
        valor = input("Insira um numero: ")
        
        if valor.isdigit():
            entrada = int(valor)
            lista.append(entrada)
            i = i+1
        else:
             print("Opção invalida!, tente novamente") 
    except ValueError as erro:
        print("Entrada inválida. Por favor, digite apenas números.")

# 3 - criar um for para percorrer a lista
# 4 - criar variavel para receber valor, comparar e substituir
n = len(lista)

for i in range(n-1):
    troca = False
    for j in range(n-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
            troca = True
    if not troca:
        break

# 5 - exibindo resultados
print(lista)



        


# 4 - criar um outro for incrementado +1 para percorrer 
# 5 - comparar os dois valores 
# 6 - substituir valores 
