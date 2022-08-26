prod = float(input("Qual o valor do produto "))
desc = prod - (prod * 5 / 100)

print("Um produto que custava {:.2f} R$ vai passar a custar {:.2f} R$ com desconto de 5%". format(prod, desc))