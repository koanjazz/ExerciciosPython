numero = int(input("Digite um numero: "))
resultado = numero % 2 #todo resto da divisão por qualquer numero par é 0, ou resto da divisão por qualquer numero impar é 1
#print("O resultado foi {}".format(resultado))

if resultado == 0: #Se resultado for igual a 0
    print("Esse numero é PAR!!!!!!")
else:
    print("Esse numero é IMPAR!!!!!")