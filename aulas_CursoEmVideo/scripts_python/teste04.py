#Verificador e número

def verificarTipo():
    valor = input("Insira qualquer valor:")
    if(valor.isalpha() == True):
        print("O valor é numérico")
    elif(valor.isnumeric() == True):
        print("O valor é numérico")
    
verificarTipo()