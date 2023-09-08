#Escreva um programa que leia um valor em metrosw e o exiba convertido em centimetros e milimetros.

md = float(input("metros: "))
cm = md * 100
mm = md * 1000
print("A medida de {}m corresponde a {}cm e {}mm".format(md, cm, mm))