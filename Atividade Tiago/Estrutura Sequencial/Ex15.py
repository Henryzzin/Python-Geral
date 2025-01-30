valor=float(input("Quanto você ganha por hora? "))
horas=float(input("Quantas horas você trabalha no mês? "))
salariobruto=valor*horas
ir=salariobruto*.11
inss=salariobruto*.08
sind=salariobruto*.05
salario=salariobruto-ir-inss-sind
print("Salário bruto: R$",salariobruto)
print("Imposto de Renda: R$", ir)
print("INSS: R$", inss)
print("Sindicato: R$",sind)
print("Salário Líquido: R$", salario)

