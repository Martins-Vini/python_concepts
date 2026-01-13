# Programaque mostre a tabuada de um número

n = int(input("Insira um número para demonstrar sua tabuada:"));


#Uso de for em python com método range() para contagem ou usado para varrer arrays
i = 0;
for i in range(11):
    print("{}*{} = {}".format(n,i, n*i)) 