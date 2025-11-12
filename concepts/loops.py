## while -> Executa repetidos blocos de código se uma condição for verdadeira
## for -> Executa uma sequência de um bloco de código em que uma ação vai mudando

##Ver notas de 3 alunos e depois fazer média

nomes = []
rm = [];
notas = [];

## x = variável temporária
## range() -> Método de repetição

for i in range(3) :
   nome = input("Insira nome do(a) aluno(a):")
   nomes.append(nome);

   rm_value = int(input("Insira o RM do(a) aluno(a): "));
   rm.append(rm_value);

   nota = float(input("Insira a nota do(a) aluno(a): "));
   notas.append(nota);

print(notas);
print(nomes);
print(rm);

total_notas = len(notas);

for i in range(total_notas):
   nota = notas[i];
   rm_aluno = rm[i];
   nome = nomes[i];
   print("O aluno ", nome, " com rm igual a ", rm_aluno, "tirou nota ", nota);

##Cálculo da média das notas

media_notas = 0;

i = 0;

while i < total_notas:
   nota = notas[i];
   media_notas = media_notas+nota;
   i = i+1;


media_notas = media_notas/total_notas;

print("Média das notas:", media_notas);


   



