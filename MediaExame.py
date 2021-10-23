print("Introduza a nota dos testes:")
t1, t2 = int(input()), int(input())
med = (t1+t2)/2
if (med >=10):
    print("Aprovado!")
else:
    print("Introduza a nota do exame:")
    exame = int(input())
    nota_final = (med*0.4) + (exame*0.6)
    if (nota_final>=10):
        print("Parabéns, está aprovado!")
    else:
        print("Infelizmente está reprovado")
