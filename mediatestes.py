print("Introduza a nota dos testes")
t1, t2, t3, t4 = int(input()), int(input()), int(input()), int(input())
med = (t1 + t2+ t3 +t4)/ 4
if (med>=10):
    print("Aprovado!")
else:
    print("Reprovado!")
