votos_brancos = int(input("Digite a quantidade de votos brancos: "))
votos_nulos = int(input("Digite a quantidade de votos nulos: "))
votos_totais = int(input("Digite a quantidade total de votos: "))
total_votos = votos_brancos + votos_nulos + votos_totais
porcentagem_brancos = (votos_brancos / total_votos) * 100
print("A porcentagem de votos brancos é de {}%".format(porcentagem_brancos))
porcentagem_nulos = (votos_nulos / total_votos) * 100
print("A porcentagem de votos nulos é de {}%".format(porcentagem_nulos))
votos_válidos = votos_brancos + votos_totais
print("A porcentagem de votos válidos é de {}%".format(votos_válidos))
