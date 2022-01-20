print("Este programa recibe tres números y devuelve la suma.")
total = 0
 
for i in range(7):
    x = int(input("Introduce un número: "))
    total = total + x
print("El total es:", total)

if total > 0:
    print ("El total es: Positiu")
elif total < 0:
    print ("El total es: Negatiu")
else:
    print ("El total es: 0")