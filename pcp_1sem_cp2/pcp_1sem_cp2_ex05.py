def pode_aprovar(idade, renda, valor):
    if idade >=18 and renda > (valor * 0.2):
        return True
    return False

def definir_taxa(parcelas):
    if parcelas <= 12:
        return 0.03
    elif parcelas <= 24:
        return 0.05
    else:
        return 0.08

def calcular_parcelas(valor, taxa, parcelas):
    numerador = taxa * (1 + taxa) ** parcelas
    denominador = (1 + taxa) ** parcelas - 1
    parcela = valor * (numerador / denominador)
    return parcela

def calcular_total(parcela, parcelas):
    return parcela * parcelas

def calcular_juros(total, valor):
    return total - valor

print("=======================================")

nome = input("Nome: ")
idade = int(input("Idade: "))
renda = float(input("Renda: "))
valor = float(input("Valor do empréstimo: "))
parcelas = int(input("Quantidade de parcelas: "))

if pode_aprovar(idade, renda, valor):
    taxa = definir_taxa(parcelas)
    v_parcela = calcular_parcelas(valor, taxa, parcelas)
    v_total = calcular_total(v_parcela, parcelas)
    v_juros = calcular_juros(v_total, valor)

    print(f"\nAPROVADO")
    print(f"Cliente: {nome}")
    print(f"Valor: R$ {valor:.2f}")
    print(f"Taxa: {taxa * 100}%")
    print(f"Parcela: R$ {v_parcela:.2f}")
    print(f"Total: R$ {v_total:.2f}")
    print(f"Juros: R$ {v_juros:.2f}")
else:
    print("NEGADO: Não atende aos requisitos.")