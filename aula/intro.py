print("Iniciando o Comparador de Valores.")

value1 = int(input("Escreva o primeiro valor: "))
value2 = int(input("Escreva o segundo valor: "))

if value1 > value2:
    print('O primeiro valor é maior.')
elif value2 == value1:
    print('Os valores são iguais.')
else:
    print('O segundo valor é maior que o primeiro.')