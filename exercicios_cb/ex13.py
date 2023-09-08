#faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario,
#com 15% de aumento.

s = float(input("Digite o salário do funcionário: "))

aumento = s * 0.15
n_s = s + aumento

print("O novo salário do funcionário com 15% de aumento é:", n_s)