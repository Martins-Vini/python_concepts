#Uso do input para entrada de dados e conversão de dados

nome = input("Insira seu nome: ");
idade = int(input("Insira sua idade: ")); ## conversão de dado para número inteiro
peso = float(input("Insira seu peso: ")); ## Conversão de dado para número decimal

print("nome:", nome, "idade:", idade, "peso:", peso);

##Uso de type para saber tipo da variável

print(type(nome));
print(type(idade));
print(type(peso));
