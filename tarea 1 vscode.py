def adivina_el_numero():
    numero_secreto = 45

    nombre = input("Por favor, ingrese su nombre: ")
    apellido = input("Por favor, ingrese su apellido: ")
    edad = input("Por favor, ingrese su edad: ")

    intento = int(input(f"Hola {nombre} {apellido}, ingresa un número para adivinar el número secreto: "))

    if intento == numero_secreto:
        print(f"ganaste {nombre} {apellido} el número secreto era {numero_secreto}.")
    else:
        print(f" muchas gracias por participar {nombre} {apellido} el numero que indicaste no es el numero secreto.")

adivina_el_numero ()

#tarea de Eliana Bustamante Rivera

#parte 2 de la tarea 
#la extencion error lens me permite ver la linea exacta donde hay un error con el codigo y me dice cual es el 