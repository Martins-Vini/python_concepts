#Calcular aluguel de carro

dias = int(input("Por quantos dias o carro foi alugado?"))
km = float(input("Quantos quilômetros foram percorridos?")) 

preco = (km*0.15)+(dias*60)

print("O preço total a pagar é de R$ {:.2f}".format(preco))