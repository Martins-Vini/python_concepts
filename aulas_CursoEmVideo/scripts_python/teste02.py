# Verificando tipos primitivos
def verificador():
    dado = int(input("Insira um número:"));
    dado2 = float(input("Insira um número inteiro:"));
    msg = str(input("Insira uma mensagem:"));
    booleandata = bool(input("Insira um tipo booleano:"));
    print(dado)
    print(type(dado))
    print(dado2)
    print(type(dado2))
    print(msg)
    print(type(msg))
    print(booleandata)
    print(type(booleandata))

verificador();