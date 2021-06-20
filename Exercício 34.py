print("-"*15)
print("Aumento Salarial")
print("-"*15)

salario=float(input("Digite o sálario do funcionário: "))

if salario>1250:
    nvsalario = salario + (salario*0.15)
else:
    nvsalario = salario + (salario*0.10)
print("O salário reajustado é de: R$ {}".format(nvsalario))