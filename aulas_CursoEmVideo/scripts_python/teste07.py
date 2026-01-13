from math import sqrt, floor;

num = int(input('Digite um número: '))
raiz = sqrt(num)

print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
print('A raiz inteira de {} é igual a {}'.format(num, floor(raiz)))