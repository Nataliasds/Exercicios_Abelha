#crie um programa que leia quanto dinheiro uma pessoa tem na carteira 
#e mostre quantos dolares ela pode comprar

real = float(input("Digite a quantidade de dinheiro em reais: "))
dolar = 4.98

conv = real / dolar

print(f"Voce tem {conv} em dolar")