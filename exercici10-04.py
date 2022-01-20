#Este juego es para adivinar si ha salido piedra, papel o tijera

import random 

x=random.randrange(0,3)
"""
Pedra=0
Paper=1
Tisores=2
"""
#print (x)
j=int(input("Introdueix pedra=0 o tisores=2 o paper=1  x="))
if x==0 and j==2 or x==1 and j==0 or x==2 and j==1:
    print("Has ganado")
elif x==0 and j==0 or x==1 and j==1 or x==2 and j==2:
    print("Has empatado")
else:
    print("Has perdido")
