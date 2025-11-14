# 20. **Tabuada** ➗: Imprima a tabuada de um número.

# Usuário insere a tabuada desejada
tabuada = int(input('Insira qual a tabuada voce deseja: '))

print(f'--- Tabuada do {tabuada} ---')

# Calculo e exibição de resultados
for numero in range(1, 11):
  resultado = tabuada * numero
  print(f'{tabuada} x {numero} = {resultado}')


    


