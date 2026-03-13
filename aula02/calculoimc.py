altura = float(input("Qual a sua altura? "))
peso = float(input("Qual o seu peso? "))

imc = peso / (altura * altura)

print(f"IMC: {imc}")
if imc < 18.5:
    print("\nBaixo peso")
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")