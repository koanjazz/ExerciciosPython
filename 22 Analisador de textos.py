nome = str(input("Digite seu Nome Completo : ")).strip()
print("Analisando seu nome ...")
print("Seu nome em Maiúscula é {}".format(nome.upper()))
print("Seu nome em Minúscula é {}".format(nome.lower()))
#print('-'.join(nome))
div = (nome.split())
print("Seu primeiro nome é {}".format(div[0]))
print("Seu primeiro nome tem {}".format(nome.find (" ")))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))









"""frase = "    curso em video python"
print(frase[:13])
print(frase[::2])
print(frase.count("o"))
print(frase.upper().count("O"))
print(len(frase))
print(len(frase.strip()))
print(frase.replace("python" , "andorid"))
print(frase)

nome = "Curso em video python"
nome = nome.replace("python", "android")
print (nome)"""