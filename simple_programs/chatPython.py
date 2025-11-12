##conceito de importação e exportação de módulos para aplicações

import os; ##Biblioteca que permite interação com o sistema operacional

mensagens = [];

nome = input("Insire seu nome:");

while True:
    os.system('cls') ##limpa o terminal
    if(len(mensagens) > 0): 
        for m in mensagens:
           print(m['nome'], '-', m['texto']);
     
    print("-------------");
    texto = input("mensagem: ");

    if(texto == "fim"):
        break;

    mensagens.append({
        "nome":nome,
        "texto":texto
    })