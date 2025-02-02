idade = input("Qual sua idade? ")
nome = input("Qual o seu nome? ")

idade = int(idade)

if idade > 18 and nome == "Lucas":
    print("Aprovado")
else:
    print("Reprovado")