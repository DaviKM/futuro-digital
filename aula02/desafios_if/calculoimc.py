altura = float(input("Qual a sua altura? "))
peso = float(input("Qual o seu peso? "))

imc = peso / (altura * altura)

print(f"IMC: {imc}\n")
if imc < 18.5:
    print("Baixo peso")
elif imc < 25:
    print("Peso ideal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")