from menu import *
from clientes import *
from comprar import *
from seguimiento import *
#importo todos los módulos necesarios para el funcionamiento del progama. 

while True:
    opcion = menu()
    if opcion == 1:
        registro_cliente()
    if opcion == 2:
        ver_clientes()
    if opcion == 3:
        buscar_cliente()
    if opcion == 4:
        comprar ()
    if opcion == 5:
        seguimiento ()
    if opcion == 6:
        print("\nHasta pronto!!!")
        break