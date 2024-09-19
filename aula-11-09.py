'''
print("Tabuada do 2")

p = 0

while p < 20:
    p = p+2
    print(p)

print("Tabuada do 5")

x = 0

while x < 50:
    x = x+5
    print(x)

print("Tabuada do 7")

y = 0

while y < 70:
    y = y+7
    print(y)


texto = input("Insira algo aqui: ")

for x, i in enumerate(texto, 1):
    numero = x

print("Esse texto possui", numero, "caracteres.")
'''

'''
p1 = "Curso"
p2 = "Python"
contador = 0

while contador < 10:
    contador = contador+1
    print(p1, "\n")
    print(p2, "\n")
'''


'''
nota = int(input("Digite sua nota: "))

if nota in range(0, 10):
    print("A sua nota é valida! (", nota, ")")
else:
    print("A sua nota é invalida! (", nota, ")")
'''


idadeNovo = 3000
idadeVelho = 0
print("Para finalizar a execução, digite um numero negativo")
idade = int(input("Digite a idade: "))

while idade > 0:
    if idade < idadeNovo: # surgiu uma pessoa mais nova
        idadeNovo = idade
    if idade > idadeVelho:
        idadeVelho = idade
    if idade < 0:
        break
print("Nova", idadeNovo)
print("Velho", idadeVelho)
'''

print("Para terminar a leitura, digite um numero negativo", "\n")
idade = int(input("Digite a idade: "))
idadeNova =
idadeVelha = 

while idade < 0:
'''



'''

n = int(input("Insira um numero: "))
orig = n
inv = 0

while n > 0:
    inv = inv*10 + n % 10
    n = n // 10
    print(inv)
if inv == orig:
    print("Palindromo")
else:
    print("não é")
'''

n = int(intput("Insira um numero: "))

s = 0
inv = 0

while n > 0:
    inv = inv*10 + n % 10
    inv = inv % 10
    n = n // 10

    s = s + inv

    print(inv, n)
print("Soma = ", s)
'''
