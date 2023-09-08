#faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua area e a quantidade de tinta necessaria para pintá-la, sabendo 
#que cada litro de tinta,pinta uma area de 2m2

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area = largura * altura
quantidade_tinta = area/2

print("A área da parede é:", area, "metros quadrados.")
print("Será necessário", quantidade_tinta, "litros para pintar completamente a parede.")
