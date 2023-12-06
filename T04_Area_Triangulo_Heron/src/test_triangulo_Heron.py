from triangulo_Heron import *
print("calculo del area de un triangulo por heron")
l1=float(input("lado 1: "))
l2=float(input("lado 2: "))
l3=float(input("lado 3: "))
area=area_por_heron(l1,l2,l3)
print("el area es:",area)
print("el perimetro es:",perimetro(l1,l2,l3))