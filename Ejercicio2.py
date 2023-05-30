sexo = input("sexo: ")
nombre = input("nombre: ")
edad = int(input("edad: "))
altura = float(input("altura: "))
print("\n")
if edad >= 18:
    print("Es mayor de edad")
if sexo.lower() == "femenino" and altura > 1.7:
    print("Es una mujer alta.")
elif sexo.lower() == "masculino" and altura > 1.80:
    print("Es un hombre alto.")