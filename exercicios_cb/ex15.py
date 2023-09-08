#escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
#sabendo que o carro custa R$0,15 po Km rodando

kmpercorridos = float(input("Digite a quantidade de quilômetros percorridos: "))
diasalugados = int(input("Digite a quantidade de dias de aluguel: "))

precokm = 0.15
precodia = 60

valorkm = kmpercorridos * precokm
valordia = diasalugados * precodia

precototal = valorkm + valordia

print("O preço a pagar pelo aluguel do carro é de R$", precototal)