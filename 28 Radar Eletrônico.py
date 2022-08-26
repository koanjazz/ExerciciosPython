carro = float(input("Qual velocidade atual do carro: "))
if carro > 80:
    print("MULTADO !!! VOCÊ EXCEDEU O LIMITE PERMITIDO QUE É DE 80KM/H")
    multa = (carro-80) * 7
    print("VOCÊ DEVE PAGAR UMA MULTA DE R$ {:.2f}".format(multa))
print("TENHA UM BOM DIA! DIRIJA COM SEGURANÇA")
