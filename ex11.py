numero = int(input('Informe um número com 3 digitos: '))          # 136
a = numero // 100     # 1
resto = numero % 100  # 36
b = resto // 10       # 3
c = resto % 10        # 6
print(f'Numero invertido: {c}{b}{a}')

numero = input('Numero: ')
numero = numero [::-1]
print(numero)


