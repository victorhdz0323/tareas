numero = int(input("Ingresa un número mayor o igual a 12: "))
if numero < 12:
    print("El número debe ser 12 o mayor.")
else:
    primo = True
    if numero < 2:
        primo = False
    else:
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                primo = False
                break

    if primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")
