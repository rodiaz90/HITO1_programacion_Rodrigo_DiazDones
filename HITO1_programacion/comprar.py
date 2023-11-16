from control_stock import * #importo el módulo necesario para que reste el stock que se está comprando 

def comprar():
    #primero se identificar al cliente
    busqueda = input("\nIndique su DNI para identificarse como cliente: ")

    try:
        with open("clientes.txt", "r") as archivo:
            contenido = archivo.readlines()
            encontrado = False
            dcf = [] #lista en la que se va a guardar los datos que me interesan del cliente para posteriormente unirlos con los datos de compra

            for linea in contenido:
                a, b, c, d = linea.strip().split(";") #cada línea del documento está dividida en ";" y aquí procedo a separarlo para su posterior análisis
                if c == busqueda:
                    print(f"\n-----Bienvenid@: {a}------")
                    dcf = f"{a};{b};{c}" #aquí se genera el contenido de la lista anterior
                    encontrado = True
                    break
            
            if not encontrado:
                print("\nCliente no encontrado.\n") #control de errores
                return

            while True:
            
            #abre el archivo correspondiente para mostrar artículos
                with open("articulos.txt", "r") as archivo:
                    contenido = archivo.readlines()
                    print("\n-----Artículos disponibles----")
                    for linea in contenido:
                        art, cant, precio = linea.strip().split(";")
                        print(f"\n{art} precio unidad {precio}")

                #imputs para hacer la lista de la compra
                seleccion = input("\nEscriba el nombre del artículo que desee comprar: ")
                cantidad = int(input("\nIndique la cantidad: "))
                total = int(cantidad) * float(precio)
                lista_art = f"{seleccion};{cantidad};{total}"

                restar(seleccion, cantidad) #importo la funcion de control de stock
                
                #abre el archivo, pega el contenido de los datos cliente con los de lista de compra y los escribe en listacompra.txt
                with open("listacompra.txt", "a") as archivo:
                    archivo.write(f"{dcf};{lista_art}\n")

                cerrar = int(input("\nsi desea terminar pulse 1 de lo contrario pulse 2: ")) #introduzco un controlador para salir del bucle cuando el usuario desee.
                if cerrar == 1:
                    break
                
    except Exception as e:
        print(f"\nError inesperado: {e}")            