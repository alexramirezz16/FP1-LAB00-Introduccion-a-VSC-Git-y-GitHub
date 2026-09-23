from datetime import datetime
nombre = str(input(f"Introduzca su nombre: "))
hora_actual = 22
if hora_actual < 12:
    print(f"Buenos días, {nombre}")
elif hora_actual < 20:
    print(f"Buenas tardes, {nombre}")
elif 21 <= hora_actual <= 23:
    print(f"Buenas noches, {nombre}")