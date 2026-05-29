def inss(sal):
    if sal >= 1800:
        return 0.11 
    else:
        return 0.09

def transp(sal):
    if sal >= 1500:
        return 0.06 
    else:
        return 0.05
    
def bonus(sal):
    if sal >= 1240:
        return 700
    else:
        return 500
    
def cargo(sal):
    if sal >= 3000:
        return "Acionista"
    elif sal >= 2000:
        return "Gerente"
    else:
        return "Vendedor"
    
def liquido(sal):
    
    return (sal-(inss(sal)*sal + transp(sal)*sal) + bonus(sal))

nome = input("\nDigite o nome do trabalhador: ")
salario = float(input("Digite o salário bruto do trabalhador: ").replace(",","."))

print(f"============================================\n\
Nome: {nome}\n\
Cargo: {cargo(salario)}\n\
Salário Bruto: R${salario:.2f}\n\
--------------------------------------------\n\
Valor do INSS: R${(inss(salario)*salario):.2f} ({(100*inss(salario)):.0f}%)\n\
Valor do Vale Transporte: R${(transp(salario)*salario):.2f} ({(100*transp(salario)):.0f}%)\n\
Bônus: R${bonus(salario):.2f}\n\
--------------------------------------------\n\
Salário Liquido: R${liquido(salario):.2f}\n\
============================================")