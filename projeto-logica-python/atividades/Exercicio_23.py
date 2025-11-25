# 23. **Soma de Dígitos** 🔢: Some os dígitos de um número.

valor1 = input("Insira o primeiro valor: \n")
valor2 = input("Insira o segundo valor: \n")

if valor1.isdigit() and valor2.isdigit():
    soma = int(valor1) + int(valor2)
    print(f"O valor da soma é {soma}")
else:
    print("Um dos caracteres não é permitido, insira um valor válido.")