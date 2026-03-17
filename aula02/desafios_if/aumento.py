sal = float(input("Insira o salário atual: "))

if sal < 1500:
    novo_sal = sal + (sal * 0.15)
else:
    novo_sal = sal + (sal * 0.1)

print(f"Novo salário: {novo_sal:.2f}")