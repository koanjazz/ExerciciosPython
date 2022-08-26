distancia = float(input("Qual a distancia da sua viagem: "))

passagem = distancia * 0.50
passagem1 = distancia * 0.45

if distancia < 200:
    print("O preço de sua Passagem será de  R${}".format(passagem))
else:
    print("O preço da sua passagem será {}".format(passagem1))
