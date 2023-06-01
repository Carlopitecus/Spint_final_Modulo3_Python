import random
import string
from os import system

clientes = [
    {"nombre": "Victor",  "apellido": "Rojas", "cuenta_usuario": "", "contraseña":"", "telefono":""},
    {"nombre": "Juan",    "apellido": "Diaz",  "cuenta_usuario": "", "contraseña":"", "telefono":""},
    {"nombre": "Roberta", "apellido": "Perez", "cuenta_usuario": "", "contraseña":"", "telefono":""},
    {"nombre": "Marcela", "apellido": "Soto",  "cuenta_usuario": "", "contraseña":"", "telefono":""},
    {"nombre": "Tulio",   "apellido": "Sierra", "cuenta_usuario": "", "contraseña":"", "telefono":""},
    {"nombre": "Elsa",    "apellido": "Silva", "cuenta_usuario": "", "contraseña":"", "telefono":""},
    {"nombre": "Luffy",   "apellido": "Torres", "cuenta_usuario": "", "contraseña":"", "telefono":""},
    {"nombre": "Pamela",  "apellido": "Tapia", "cuenta_usuario": "", "contraseña":"", "telefono":""},
    {"nombre": "Jesica",  "apellido": "Piña", "cuenta_usuario": "", "contraseña":"", "telefono":""},
    {"nombre": "Carla",   "apellido": "Espinoza", "cuenta_usuario": "", "contraseña":"", "telefono":""}
]

# Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios
for cliente in clientes:
    print(cliente["nombre"])
    print(cliente["apellido"])
    print()

# Mediante una función, a todos los usuarios se les creará una cuenta automáticamente
def completar_datos():
    system("cls")    

    for cliente in clientes:
        # Se crea la cuenta del usuario
        cliente["cuenta_usuario"] = cliente["nombre"] + cliente["apellido"]

        ## Se crea la contraseña mezclando Números y letras hasta completar 10 caracteres 
        caracteres = string.ascii_letters + string.digits
        cliente["contraseña"]=''.join(random.choice(caracteres) for _ in range(10))

        # Pregunta si el número telefonico tiene 8 digitos, si es distinto de 8 pregunta otra vez
        while len(cliente["telefono"]) != 8:
            cliente["telefono"] = input("Ingrese un número de telefono,para " + cliente["cuenta_usuario"] +  " debe contener 8 digitos: ")

    system("cls") 
    print("nombre: " + cliente["nombre"])
    print("Apellido: " + cliente["apellido"])
    print("Cuenta de Usuario: " + cliente["cuenta_usuario"])
    print("Contraseña: " + cliente["contraseña"])
    print("Telefono: " +  cliente["telefono"])

ingresar_datos = input("Desea completar los datos de los clientes? (Responda con si o no): ")
if ingresar_datos == "si":
    completar_datos()