#12. **Calculadora Simples** 🧮: Crie uma calculadora que suporte as quatro operações básicas.
import flet as ft
from flet import Colors
from decimal import Decimal

#Configurando aparaencia dos botoes
botoes = [{'operador':'AC', 'fonte': Colors.BLACK, 'fundo' : Colors.BLUE_GREY_100 },
          {'operador':'±', 'fonte': Colors.BLACK, 'fundo': Colors.BLUE_GREY_100 },
          {'operador':'%', 'fonte': Colors.BLACK, 'fundo' : Colors.BLUE_GREY_100 },
          {'operador':'/', 'fonte': Colors.WHITE, 'fundo' : Colors.ORANGE },
          {'operador':'7', 'fonte': Colors.WHITE, 'fundo' : Colors.WHITE24 },
          {'operador':'8', 'fonte': Colors.WHITE, 'fundo' : Colors.WHITE24 },
          {'operador':'9', 'fonte': Colors.WHITE, 'fundo' : Colors.WHITE24 },
          {'operador':'*', 'fonte': Colors.WHITE, 'fundo' : Colors.ORANGE },
          {'operador':'4', 'fonte': Colors.WHITE, 'fundo' : Colors.WHITE24 },
          {'operador':'5', 'fonte': Colors.WHITE, 'fundo' : Colors.WHITE24 },
          {'operador':'6', 'fonte': Colors.WHITE, 'fundo' : Colors.WHITE24 },
          {'operador':'-', 'fonte': Colors.WHITE, 'fundo' : Colors.ORANGE },
          {'operador':'1', 'fonte': Colors.WHITE, 'fundo' : Colors.WHITE24 },
          {'operador':'2', 'fonte': Colors.WHITE, 'fundo' : Colors.WHITE24 },
          {'operador':'3', 'fonte': Colors.WHITE, 'fundo' : Colors.WHITE24 },
          {'operador':'+', 'fonte': Colors.WHITE, 'fundo' : Colors.ORANGE },
          {'operador':'0', 'fonte': Colors.WHITE, 'fundo' : Colors.WHITE24 },
          {'operador':'.', 'fonte': Colors.WHITE, 'fundo' : Colors.WHITE24 },
          {'operador':'=', 'fonte': Colors.WHITE, 'fundo' : Colors.ORANGE },
        ]

# Definindo configurações de pagina
def main(page: ft.Page):
   page.bgcolor = '#0000'
   page.title= 'Calculadora'
   page.window.resizable = False
   page.window.always_on_top = True
   page.window.height = 390
   page.window.width = 270
   page.window.center()    

   result = ft.Text(value= '0', color= Colors.WHITE, size= 20)

   def calculate(operador, value_at):
      try:
        value = eval(value_at)

        if operador == '%':
            value/= 100
        elif operador == '±':
            value = -value
      except:         
        return 'Error'   
      
      digits = min(abs(Decimal(value).as_tuple().exponent),5)
      return format(value,f'.{digits}f')

   def select(e):
      value_at = result.value if result.value not in ('0','Error') else ''
      value = e.control.content.value

      if value.isdigit():
         value = value_at + value
      elif value == 'AC':
         value = '0'
      else:
         if value_at and value_at[-1] in ('/','*','-','+','.'):
             value_at = value_at[:-1]
         
         value = value_at + value

         if value[-1] in ('=','%','±'):
            value = calculate(operador=value[-1], value_at = value_at)

      result.value = value
      result.update()
      
   display = ft.Row (width = 270,
                     controls=[result],
                     alignment = 'end')
   
#configuração do botao
   botao = [ft.Container(
      content=ft.Text(value=botao['operador'], color=botao['fonte']),
      width=50,
      height=50,
      bgcolor=botao['fundo'],
      border_radius= 100,
      alignment=ft.alignment.center,
      on_click=select      
   )for botao in botoes]

# preparando exibições de botao na tela
   keyboard = ft.Row(
      width=270,
      #quebra linha apos chegar no final do display
      wrap=True, 
      controls=botao,
      alignment='end'
   )

   
   page.add(display, keyboard)

ft.app(target=main)
