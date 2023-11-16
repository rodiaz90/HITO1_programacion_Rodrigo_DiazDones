from menu import *
#función encargada de añadir registros introducidos por el usuario
def registro_cliente():

    while True:

        nombre = input("\nIndique su nombre: ")
        apellidos = input("\nIndique sus apellidos: ")
        dni = input("\nIndique su NIE/DNI: ")
        direccion = input("\nIndique su dirección: ")

        with open("clientes.txt", "a") as archivo:
            archivo.write(f"{nombre};{apellidos};{dni};{direccion}\n")

        cerrar = int(input("\nsi desea terminar pulse 1 de lo contrario pulse 2: ")) #introduzco un controlador para salir del bucle cuando el usuario desee.
        if cerrar == 1:
            break    
    
#funcuón encargada de abrir el archivo e imprimir su contenido
def ver_clientes():

    while True:

        with open("clientes.txt", "r") as archivo:
            contenido=archivo.read()
            print(f"\n{contenido}")
        
        cerrar = int(input("\nsi desea terminar pulse 1 de lo contrario pulse 2: ")) #introduzco un controlador para salir del bucle cuando el usuario desee.
        if cerrar == 1:
            break
        
#función encargada de realizar la busqueda en el archivo clientes.txt
def buscar_cliente():

    while True:

        busqueda = input("\nIndique SU DNI para identificar el cliente: ")
        with open("clientes.txt", "r") as archivo:
            contenido=archivo.readlines()
            encontrado = False #interruptor off
            for linea in contenido:
                a, b, c, d = linea.strip().split(";") #cada línea del documento está dividida en ";" y aquí procedo a separarlo para su posterior análisis
                if c == busqueda:
                    print (f"\nRegistro localizado:\n{linea}")
                    encontrado= True #interruptor in
                
            if not encontrado: #si interruptor off
                    print ("\nNo existe ese cliente en nuestros registros\n") #control de errores en caso de que no se encuentre

        cerrar = int(input("\nsi desea terminar pulse 1 de lo contrario pulse 2: ")) #introduzco un controlador para salir del bucle cuando el usuario desee.
        if cerrar == 1:
            break            