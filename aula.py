'''
# morango 19,90kg (ate 5kg) mais fica 15,20kg
# maçã 8,80kg (ate 5k) mais fica 7,50kg
# mais de 8kg e der mais de 25, ele ganha desconto de 10% sobre o total
# escrever quantidade em kgs e o preço

morangopeso = float(input("Digite a quantidade de morangos em kgs: "))
macapeso = float(input("Digite a quantidade de maçãs em kgs: "))

if morangopeso >= 5:
    morangokg = 15.2
else:
    morangokg = 19.5

if macapeso >= 5:
    macakg = 7.5
else:
    macakg = 8.8

valorfrutas = (morangopeso * morangokg) + (macapeso * macakg)
pesototal = (morangopeso + macapeso)

if pesototal >= 8 or valorfrutas >= 25:
    valorfrutas = valorfrutas - (valorfrutas * 0.1)

float(valorfrutas)

print("Você comprou " + str(morangopeso) + " Kgs de morango, " + str(macapeso) + " Kgs de maçã, seu total ficou R$" + str(valorfrutas))
'''


'''
# ler as notas, calcular media e atribuir conceito
# A = 9 - 10
# B = 7.5 - 9
# C = 6 - 7.5
# D = 4 - 6
# E = 4 - 0
# A ou B = aprovado, resto reprovado

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
media = (nota1 + nota2) / 2

if media > 9:
    conceito = "A"
elif media < 9 and media >= 7.5:
    conceito = 'B'
elif media < 7.5 and media >= 6:
    conceito = 'C'
elif media < 6 and media >= 4:
    conceito = 'D'
elif media < 4:
    conceito = 'E'

if conceito == 'A' or conceito == 'B':
    aprovacao = "APROVADO"
else:
    aprovacao = "REPROVADO"

print("Média do aluno: " + str(media) + "\n")
print("Resultado: " + conceito + "\n")
print("Aprovação: O alundo foi " + aprovacao)
'''


numero = input("Digite um numero de 3 digitos: ")

if (numero[0] < numero[1] and numero[2]) and (numero[1] < numero[2]):
    print("Esse numero é formado por numero em ordem crescente!")
else:
    print("Esse numero é formado por numeros em ordem decrescente!")
