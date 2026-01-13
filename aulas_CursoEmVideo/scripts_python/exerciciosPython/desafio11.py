print("=====DESCONTO DE 15% DE UM PRODUTO=====")

preco = float(input("insira o preço do seu produto:"))

desc = preco*(15/100)
novoPreco = preco-desc

print("O preço do produto com 15% de desconto é igual a R${:.2f}".format(novoPreco))