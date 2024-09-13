# Crea un programa que pida al usuario un número y determine si es par o impar.

numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
