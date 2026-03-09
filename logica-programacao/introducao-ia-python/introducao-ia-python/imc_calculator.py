# Calculadora de IMC

# pedir dados ao usuário
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# calcular IMC
imc = peso / (altura ** 2)

# mostrar resultado
print("Seu IMC é:", round(imc, 2))

# classificação
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")
