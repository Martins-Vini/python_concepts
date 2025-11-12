##Verificação de carteira de motorista

idade = int(input("Insira sua idade: "));
permission = False;

if(idade > 17): 
    permission = True;
    print("Permissão concedida ->", permission);
else :
     print("Permissão negada ->", permission);

salario = float(input("Insira seu salário:"));

## Condições encadeadas

if salario <= 3000 :
    print("Programador junior");
elif salario > 3000 and salario <= 8000 :
    print("Programador Pleno");
elif salario > 8000 and salario <= 10000 :
    print("Programador sênior");
elif salario > 10000 :
    print("Gerente de projetos");