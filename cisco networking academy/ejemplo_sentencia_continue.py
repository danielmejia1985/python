import os
os.system("clear")

# Ejemplo de la sentencia o instrucción continue

for i in range(1, 10, 1):
    if i == 3:
        print("tres")
        continue
    elif i == 6:
        print("seis")
        #continue
    else:
        print("else")
    
    print(i)

print("fin..")