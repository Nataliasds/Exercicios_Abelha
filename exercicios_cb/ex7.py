#Deseenvolva um programa que leia duas notas de um aluno,calcule e mostre a sua media.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = nota1 + nota2/2

print("A media entre {} e {} é {}".format(nota1, nota2, media))