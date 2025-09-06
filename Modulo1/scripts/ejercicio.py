"""
Cree un programa que permita ingresar los siguientes datos de una persona:
nombre, apellido, edad

Realice la suma de edad +10
"""

#1. Ingreso de datos

nombre_persona = input("Ingrese su nombre: ")
apellido_persona = input("Ingrese su apellido: ")
# debemos canvertir el dato a un entero
edad = int(input("Ingrese su edad: ")) 


edad_mas_10 = edad + 10


# imprimimos datos

print(f"Nombre: {nombre_persona}\nApellido: {apellido_persona}\nEdad: {edad}\nEdad + 10= {edad_mas_10}")


cadena_formateada = "Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nEdad + 10= {edad_sumada}"

print(cadena_formateada.format(
    nombre=nombre_persona,
    apellido=apellido_persona,
    edad=edad,
    edad_sumada=edad_mas_10)
)









