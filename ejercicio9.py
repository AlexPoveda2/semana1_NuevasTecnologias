#Imprime la tabla de multiplicar del número ingresado hasta el 10.

numero = int(input("Introduce un número: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
