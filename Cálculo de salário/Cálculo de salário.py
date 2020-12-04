hora = int(input("Quantas Horas o Funcionário Trabalhou No Mês?"))
valor = int(input("Qual o valor da hora trabalhada?"))
percentual = int(input("Qual o valor do percentual de desconto?"))

salarioBruto = hora*valor
print(f"Salário Bruto = {salarioBruto}")

desconto = (percentual*salarioBruto)/100
print(f"Total do Desconto = {desconto}")

salarioLiquido = salarioBruto - percentual
print(f"Salário Líquido = {salarioLiquido}")