segundos_total = input("Digite um valor: ")
horas = segundos_total // 3600
resto = segundos_total % 3600
minutos = resto //60
print("{} segundos equivalem a {} horas, {} minutos e {} segundos.".format(segundos_total, horas, resto, minutos))


