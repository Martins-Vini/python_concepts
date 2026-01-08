#Fazendo uma soma com função

def somar():
    n1 = float(input("Insira o primeiro número:"))
    n2 = float(input("Insira o segundo número:"))
    s = n1+n2
    print("A soma de {} e {} é igual a {}".format(n1,n2,s))
    
somar()