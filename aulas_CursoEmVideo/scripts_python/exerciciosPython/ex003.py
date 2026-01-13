def takeNumber():
    n1 = float(input("Insira o primeiro número"))
    n2 = float(input("Insira o segundo número"))
    return n1,n2
    
def somar(a,b):
    print("A soma de {} e {} é igual a {}".format(a,b, a+b))


n1, n2 = takeNumber()
somar(n1,n2)