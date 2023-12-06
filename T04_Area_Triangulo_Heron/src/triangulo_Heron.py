from math import sqrt
def perimetro(a:float,b:float,c:float)->float:
    if a>0 and b>0 and c>0:
        return a+b+c
        
def area_por_heron(a:float,b:float,c:float)->float:
    if a>0 and b>0 and c>0 and (a+b)>c and (a+c)>b and (b+c)>a :
        sp=perimetro(a,b,c)/2
        res=sqrt(sp*(sp-a)*(sp-b)*(sp-c))
        if res>0 :
                return res
    