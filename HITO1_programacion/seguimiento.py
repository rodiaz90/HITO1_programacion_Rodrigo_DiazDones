def seguimiento ():

    seguir = input("\nIndique DNI de cliente para econtrar factura: ") 
    residencia = int(input("\nSi su lugar de residencia es España escriba 1 en caso contrario escriba 2: ")) 
    factura = []
    suma_total = 0
    terminado = True

    try:

        while True:

            if residencia == 1:

                with open ("listacompra.txt", "r") as archivo:
                    lineas = archivo.readlines()
                    for linea in lineas:
                        a, b, c, d, e, f = linea.strip().split(";")#cada línea del documento está dividida en ";" y aquí procedo a separarlo para su posterior análisis 
                        if seguir == c:
                            factura = f"{d}----{f}\n" #toma los datos que me interesan
                            suma_total += float(f) #suma el importe de las compras
                            print (factura)
                        else:
                            print("\nNo hay compras de ese cliente\n") #control de errores
                            terminado = False
                            break

                if terminado:
                        iva = suma_total * 1.21 #multiplca la suma de las compras por el IVA
                        print(f"total a pagar + 21% de IVA {iva}\n")    
                        print("Se envía SMS con datos de compra\n")   
            elif residencia != 1: #si su residencia es otra
                with open ("listacompra.txt", "r") as archivo:
                    lineas = archivo.readlines()
                    for linea in lineas:
                        a, b, c, d, e, f = linea.strip().split(";") #cada línea del documento está dividida en ";" y aquí procedo a separarlo para su posterior análisis
                        if seguir == c:
                            factura = f"{d}----{f}\n" #toma los datos que me interesan
                            suma_total += float(f) #suma el importe de las compras
                            print (factura)
                        else:
                            terminado = False #control de errores
                            break

                if terminado:
                        print(f"total a pagar: {suma_total}\n")    
                        print("Se envía SMS con datos de compra\n") 

            cerrar = int(input("\nsi desea terminar pulse 1 de lo contrario pulse 2: ")) #introduzco un controlador para salir del bucle cuando el usuario desee.
            if cerrar == 1:
                break        

    except Exception as e:
        print(f"\nError inesperado: {e}")                