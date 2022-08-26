din = float(input("Quanto dinheiro voce tem na carteira : "))
dol = din / 5.22  # *0.19 com multiplicação
eu = din * 0.18
print ("Com R${:.2f} você pode comprar US${:.2f} ".format(din, dol))
print("Com R${:.2f} você pode comprar EU${:.2f}".format(din, eu))