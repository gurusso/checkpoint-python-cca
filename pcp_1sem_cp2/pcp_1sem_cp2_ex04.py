def calcular_horas_extras(salario_base, horas):
    return horas * (salario_base * 0.015)

def calcular_descontos_faltas(salario_base, falta):
    return falta * (salario_base * 0.02)

def calcular_bonus(cargos, recebeu_bonus):
    if recebeu_bonus == 's':
        if cargos == 1:   # Gerente
            return 1000
        elif cargos == 2: # Analista
            return 500
        elif cargos == 3: # Assistente
            return 300
        else:            # Estagiário
            return 100
    return 0

nome = input("Digite o nome do funcionario: ")
print('DIGITE 1 PARA GERENTE')
print('DIGITE 2 PARA ANALISTA')
print('DIGITE 3 PARA ASSISTENTE')
print('DIGITE 4 PARA ESTAGIÁRIO')
cargo = int(input("Digite o cargo do funcionario: "))
salario = float(input("Digite o salario do funcionario: "))
horaex = int(input("Digite as horas extras trabalhadas do funcionario: "))
faltas = int(input("Digite quantas faltas o funcionario teve"))
bonus = input("Recebeu bonus por desempenho? (s ou n) ").lower()
vhoraex = calcular_horas_extras(salario, horaex)
dfaltas = calcular_descontos_faltas(salario, faltas)
vbonus = calcular_bonus(cargo, bonus)

salariobruto = salario + vhoraex + vbonus
salariofinal = salariobruto - dfaltas
print(f"O salário bruto foi de {salariobruto}")
print(f"O total de acrescimos foi de {vbonus + horaex}")
print(f"O valor total dos descontos foi de {dfaltas}")
print(f"O salário final foi de {salariofinal:.2f}")

