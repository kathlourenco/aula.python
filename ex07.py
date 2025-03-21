custo_fabrica = float(input("Digite o custo de fábrica de um carro: "))
porcentagem_distribuidor = 0.28 * custo_fabrica
print("O valor da porcentagem do distribuidor é {} reais".format(porcentagem_distribuidor))
impostos = 0.45 * custo_fabrica
print("O valor dos impostos do carro é de {} reais".format(impostos))
custo = custo_fabrica + porcentagem_distribuidor + impostos
print("O valor total gasto para a compra de um carro, em reais é {}".format(custo))

