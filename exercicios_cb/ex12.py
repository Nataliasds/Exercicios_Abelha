#faça um algoritimo que leia o preço de um produto 
#e mostre seu novo preço,com 5% de desconto.

p = float(input("Digite o preço do produto: "))

des = p * 0.05
n_p = p - des

print("O novo preço do produto com 5% de desconto é:", n_p)