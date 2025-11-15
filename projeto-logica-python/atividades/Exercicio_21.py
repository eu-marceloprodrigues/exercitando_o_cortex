# 21. **Conversor de Moeda** 💱: Converta valores entre diferentes moedas.
# Criar API para buscar cotação na internet
# USD -> dolar
# BRL -> real
# BTC -> bitcoin
# EUR -> euro

import requests

# Função pegar_cotação solicita capta a cotação atual, atraves de uma API 
def pegar_cotação(moeda_local, moeda_destino, valor_a_converter):
    conversao = valor_a_converter
    link = f"https://economia.awesomeapi.com.br/last/{moeda_local}-{moeda_destino}?]" #Prepara conexao
    requisição = requests.get(link) # Faz conexão
    dic_resposta = requisição.json() # Recebe dados em formato json
    
    cotacao = dic_resposta[f"{moeda_local}{moeda_destino}"]["bid"] # Filtra dados
    cota = float(cotacao) 
    converte_valor(cota, conversao) # Chama outro metodo para converter valor

def converte_valor(cotacao, valor_a_converter):
    valor_convertido = cotacao * valor_a_converter
    print(f"O valor convertido é R$ {valor_convertido: .2f}")

#INicio
opcao = input("Converta Dólar, Euro ou Bitcoin para Real:\n1-Dólar\n2-Euro\n3-Bitcoin\n")
valor_a_converter= float(input("Insira o valor a converter R$ "))

real = "BRL"

if opcao == '1':
    moeda = 'USD'
    pegar_cotação(moeda, real, valor_a_converter)
    
elif opcao == '2':
    moeda = 'EUR'
    pegar_cotação(moeda, real, valor_a_converter)
elif opcao == '3':
    moeda = 'BTC'
    pegar_cotação(moeda, real, valor_a_converter)

    
