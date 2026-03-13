nome = input("Digite seu nome: ")
idade = input("Qual a sua idade? ")
idade = int(idade) #OUUUU preferencialmente idade = int(input("Qual a sua idade? "))

anos_de_vida = 100 - idade

print(f"Olá, {nome}! Você tem {idade} anos.\nVocê tem {anos_de_vida} anos de vida restantes.")