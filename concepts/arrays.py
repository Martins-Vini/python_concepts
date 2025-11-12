lista_nomes = ["Vini", "Miguel", "Caio"];
print(lista_nomes[0]);

lista_idades = [17, 19, 21, 20, 17, 17, 18, 15, 16, 12, 9, 18];
print(lista_idades);

##Métodos simples em python

## Append -> Adiciona elementos no último índice do array

lista_nomes.append("Rogers")
lista_idades.append(19);
print(lista_nomes);
print(lista_idades);

## len, min e max

print("Total de idades da lista:", len(lista_idades));
print("Maior idade:", max(lista_idades));
print("Menor idade:", min(lista_idades));