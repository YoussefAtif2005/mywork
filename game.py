import random as r
n=r.randint(1, 100)
a=input("Entrer votre nombre: ")
b=int(a)
if b<n:
    print("Inférieur.")
elif b>n:
    print("Supérieur.")
else:
    print("Correcte")        

while b!=n:
    print("Veuiller réssayer:")
