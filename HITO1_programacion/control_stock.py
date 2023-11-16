def restar(seleccion, cantidad): #introduzco los valores generados en la funcion comprar
    lineas_actualizadas = [] #lista en las que se ecriben los resultados de las operaciones
    cambio = False #interruptor off

    try:
        with open("articulos.txt", "r") as archivo:
            for linea in archivo:
                nombre, stock, precio = linea.strip().split(";") #cada línea del documento está dividida en ";" y aquí procedo a separarlo para su posterior análisis

                if nombre == seleccion: #si el articulo que escibre el usiario coincide con el del archivo
                    
                    if int(cantidad) > int(stock): #cambia los parámetros a valores numéricos y comprueba que haya suficiente stock
                        print(f"\nError, nuestro Stock de {seleccion} es de {stock}\n")

                    else: #si hay suficiente stock procede a restar la cantidad retirada por el cliente
                        nueva_cantidad = int(stock) - int(cantidad)
                        textoaguardar = f"{nombre};{nueva_cantidad};{precio}\n" #escribe el contenido de la lista
                        lineas_actualizadas.append(textoaguardar) #guarda el contenido en la lista
                        cambio = True #interruptor on
                else:
                    lineas_actualizadas.append(linea) #si el articulo que escibre el usiario NO coincide con el del archivo escibre la línea y pasa a la siguiente  

        if cambio: #si interrupto on, escribe el archivo con el contenido actualizado de la lista "lineas_actualizadas"
            with open("articulos.txt", "w") as archivo:
                for i in lineas_actualizadas:
                    archivo.write(i)

    except Exception as e:
        print(f"\nError inesperado: {e}")

    return lineas_actualizadas #devuelve contenido de la lista para ser utilizado en el resto del programa
                    
