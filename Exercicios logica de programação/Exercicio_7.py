#7. **Fibonacci** 🌀: Gere a sequência de Fibonacci até um número n.
#A sequência de Fibonacci é uma série de números inteiros onde cada termo é a soma dos dois anteriores,
#começando com 0 e 1, resultando na sequência 0, 1, 1, 2, 3, 5, 8, e assim por diante.

#iniciar a sequencia em 0

#numero_atual + numero_anterior = proximo_numero (ate o valor especicicado pelo usuario)

numero_limite = int(input("Insira o valor final da sequencia: \n"))

termo_start1 = 0
termo_start2 = 1
termo3 = 0

while termo3 <= numero_limite:
    print("{}.".format(termo3), end="")
    termo3 = termo_start1 + termo_start2
    termo_start1 = termo_start2
    termo_start2 = termo3

print( " Fim ")