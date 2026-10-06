anos_exp = float(input("Anos de experiência na área: "))

if anos_exp >= 5:
    print("Categoria: Desenvolvimento Sênior")
elif anos_exp >= 2:
    print("Categoria: Desenvolvimento Pleno")
else:
    print("Categoria: Desenvolvimento Júnior")