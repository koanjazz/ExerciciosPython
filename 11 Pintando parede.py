la = float(input("Largura da parede : "))
al = float(input("Altura da parede : "))

soma =  la * al
soma2 = la * al / 2
print("Sua parede tem a dimensão de {} x {} e sua área é de {}".format(la,al,soma))
print("Para pintar essa parede, você precisará de {} Litros de tinta!".format(soma2))