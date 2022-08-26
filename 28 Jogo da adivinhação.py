import random
numero = random.randint(0,5)
print(80 * ("="))
num = int(input("Vou pensar em um número entre 0 e 5. Tente adivinhar... "))
print(80 *("="))
print()

if numero == num:
    print("PARABÉNS VOCÊ CONSEGUIU ME VENCER!!!!!")
else:
    print("GANHEI!!!! EU PENSEI NO NUMERO {} E NÃO NO {}".format(numero,num))



