from datetime import date # Importando Modulo Datetime
ano = int(input("Que ano quer analisar ? Coloque para Analisar  o Ano atual: ")) # Declarando Variável
if ano == 0: # Se ano for igual a zero
    ano = date.today().year # Usando modulo Importado

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # Condicional, Calculo para definir ano Bissexto, se resultado de ano dividido por 4 for
    # 0 e resultado de ano dividido 100 for diferente de 0 ou ano dividido por 400 o resultado for 0
    print("O ano {} é bissexto!!!! ".format(ano))
else:
    print("O ano {} não é bissexto !!!!!".format(ano))


