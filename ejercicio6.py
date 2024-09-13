# Crea un programa que pida al usuario su calificación y luego imprima el mensaje "Aprobado" si la calificación es mayor o igual a 70, o "Reprobado" si la calificación es menor que 70.

calificacion = float(input("Introduce tu calificación: "))
if calificacion >= 70:
    print("Aprobado")
else:
    print("Reprobado")
