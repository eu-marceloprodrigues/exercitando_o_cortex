#4. **Conversor de Temperatura** 🌡️: Converta uma temperatura de Celsius para Fahrenheit e vice-versa.
# Converter de Celsius para Fahrenheit -> F = C x 1,8 + 32
# Converter de Fahrenheit para Celsius -> C=(F-32)/1,8
def CelsisusToFahrenheit(temperatura):
    fahrenheit = (temperatura*1.8) + 32
    print(f"Temperatura de Celcius para Farenheit:",fahrenheit,"F°")

def FahrenheitToCelsius(temperatura):
    celcius = (temperatura-32)/1.8
    print(f"Temperatura de Farenheit para Celsius:",celcius, "C°")
    

temperatura = int(input("Insira a temperatura que deseja converter:\n "))

opcao= int(input("Escolha qual opção de conversão:\n" \
"1-CELSIUS PARA FARENHEIT\n2-FARENHEINT PARA CELSIUS\n"))

if opcao == 1:
    CelsisusToFahrenheit(temperatura)
else:
    FahrenheitToCelsius(temperatura)