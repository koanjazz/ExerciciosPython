'''name = (input("Digite Algo ? : "))
print("O tipo primitivo desse valor é ", type(name))
print("Só tem espaços ? ", name.isspace())
print("Só letra maiuscula", name.isupper())


print(name)'''


n1 = int(input("Digite um numero : "))
n2 = int(input("Digite outro valor : "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print("A soma é {}, o produto é {}, e a divisão é {} ".format(s,m,d))