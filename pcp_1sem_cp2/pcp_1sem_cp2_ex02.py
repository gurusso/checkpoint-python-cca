#Exercício 2

valores = input("Digite os 3 lados do triângulo separados por espaço: ").split()
lados = [float(i) for i in valores]


lados.sort(reverse=True)

a = lados[0]
b = lados[1]
c = lados[2]

if a >= (b + c):
    print("NAO FORMA TRIANGULO")

else:

    if (a ** 2) == (b ** 2 + c ** 2):
        print("TRIANGULO RETANGULO")

    elif (a ** 2) > (b ** 2 + c ** 2):
        print("TRIANGULO OBTUSANGULO")

    elif (a ** 2) < (b ** 2 + c ** 2):
        print("TRIANGULO ACUTANGULO")

    if a == b and b == c:
        print("TRIANGULO EQUILATERO")

    elif a == b or b == c or a == c:
        print("TRIANGULO ISOSCELES")

print("---FIM---")