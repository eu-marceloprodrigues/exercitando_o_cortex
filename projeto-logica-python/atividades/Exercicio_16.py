# 16. **Busca Binária** 🔎: Implemente um algoritmo de busca binária em uma lista ordenada.
lista = [1,2,3,4,5,6,7]

valor_procurado = float(input("Insira um valor para pesquisa: \n"))

# definir ponteiros
primeiro = 0 
ultimo = len(lista)-1

while primeiro <= ultimo:
    # definir meio
    meio = (primeiro + ultimo) // 2
    chute = lista[meio]

    if chute == valor_procurado:
        print("Achou")
        break
    elif chute < valor_procurado:
        primeiro = meio +1
    else:
        ultimo = meio - 1
    
# verifica se numero indicado esta na lista
if valor_procurado not in lista:
    print("Não esta na lista")

