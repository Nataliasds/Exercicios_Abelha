#Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input("Escolha um Número: "))

for n in range (11):
  print(f'{numero} x {n} = {numero*n}')