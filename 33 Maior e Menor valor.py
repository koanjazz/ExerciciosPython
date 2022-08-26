primeiro = int(input("Digite Primeiro numero:"))
segundo = int(input("Digite o segundo numero:"))
terceiro = int(input("Digite o teceiro numero:"))


# Definindo o menor numero
menor = primeiro
if segundo < primeiro and segundo < terceiro:
    menor = segundo

if terceiro < primeiro and terceiro < segundo:
    menor = terceiro

#definindo o maior numero
maior = primeiro
if segundo > primeiro and segundo > terceiro:
    maior = segundo

if terceiro > primeiro and terceiro > segundo:
    maior = terceiro



print("O menor valor digitado é {}".format(menor))
print("O maior valor digitado é {}".format(maior))