# Dissecando variáveis
# Ver se é: Número, tem espaços, é alfabético, é alfanumérico, é em maiúsculo, é em minúsculo, se é capitalizado

def verificar():
    valor = input("Insira o valor do dado de uma variável")
    print("A classe desse dado é {}".format(type(valor)))
    print("o dado é um número?", valor.isnumeric())
    print("o dado faz parte do alfabeto?", valor.isalpha())
    print("o dado é alfanumérico?", valor.isalnum())
    print("o dado é uma string só com espaços?", valor.isspace())
    print("o dado é um texto em maiúsculo?", valor.isupper())
    print("o dado é um texto minúsculo??", valor.islower())
    print("Esse dado tá capitalizado?", valor.istitle())
    
verificar()