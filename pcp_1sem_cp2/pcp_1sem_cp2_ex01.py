def calcular_transporte():

    codigo_estado = int(input("Digite o código do estado de origem (1 a 5): "))
    peso_toneladas = float(input("Digite o peso da carga (em toneladas): "))
    codigo_carga = int(input("Digite o código da carga (10 a 40): "))

    peso_quilos = peso_toneladas * 1000

    if 10 <= codigo_carga <= 20:
        preco_por_kg = 100.00
    elif 21 <= codigo_carga <= 30:
        preco_por_kg = 250.00
    elif 31 <= codigo_carga <= 40:
        preco_por_kg = 340.00

    preco_carga = peso_quilos * preco_por_kg

    if codigo_estado == 1:
        percentual_imposto = 0.35 # 35%
    elif codigo_estado == 2:
        percentual_imposto = 0.25 # 25%
    elif codigo_estado == 3:
        percentual_imposto = 0.15 # 15%
    elif codigo_estado == 4:
        percentual_imposto = 0.05 # 5%
    elif codigo_estado == 5:
        percentual_imposto = 0.00 # isento (0%)


    valor_imposto = preco_carga * percentual_imposto


    valor_total = preco_carga + valor_imposto


    print("\n--- RESUMO DO CÁLCULO ---")
    print(f"Peso convertido: {peso_quilos:,.2f} kg")
    print(f"Preço da carga: R$ {preco_carga:,.2f}")
    print(f"Valor do imposto: R$ {valor_imposto:,.2f}")
    print(f"Valor total transportado: R$ {valor_total:,.2f}")

calcular_transporte()