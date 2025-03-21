dias_trabalhados = int(input("Digite quantos dias o funcionário trabalhou: "))
imposto = (8 * 80) / 100
imposto_dois = imposto * dias_trabalhados
salario = dias_trabalhados * 80
salario_final = salario - imposto_dois
print("O valor recebido pelo funcionário foi de {} reais.".format(salario_final))
