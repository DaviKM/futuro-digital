velocidade = float(input("Insira a velocidade do carro: "))

if velocidade > 80:
    km_excedente = velocidade - 80
    valor_multa = km_excedente * 5
    print(f"Valor da multa: {valor_multa:.2f}")