'''cat = float(input("Comprimento do Cateto Oposto : "))
adj = float(input("Comprimento do Cateto Adjacente : "))
hip = (cat ** 2 + adj **2) ** (1/2)
print("A hipotenusa vai medir {:.2f} ".format (hip))'''

import math
cat = float(input("Comprimento do Cateto Oposto : "))
adj = float(input("Comprimento do Cateto Adjacente : "))
hip = math.hypot(cat, adj)
print("A hipotenusa vai medir {:.2f} ".format (hip))