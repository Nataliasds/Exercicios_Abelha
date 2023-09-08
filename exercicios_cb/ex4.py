#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçôes
#possivéis sobre ele.

v1 = input("Digite algo: ")

print("O tipo primitivo desse valor é", type(v1))
print("Só tem espaços ?", v1.isspace())
print("È um número?", v1.isnumeric())
print("É alfabético?", v1.isalpha())
print("Está em maiúscula?" , v1.isupper())
print("Está em minúscula?", v1.islower())


