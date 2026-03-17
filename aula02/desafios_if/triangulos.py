l1 = float(input("Digite o primeiro lado: "))
l2 = float(input("Digite o segundo lado: "))
l3 = float(input("Digite o terceiro lado: "))

if (l1 + l2 + l3 - max(l1, l2, l3)) > max(l1, l2, l3):
    print("Pode formar um triângulo")
else:
    print("Não pode formar um triângulo")