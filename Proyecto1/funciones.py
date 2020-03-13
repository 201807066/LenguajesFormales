import platform
import os
import time
import opc1

#Método para el menu
def menu():
    limpiar()
    opc = 0

    while True:
        try:
            while opc != 6:
                print("1-Crear AFD")
                print("2-Crear Grámatica")
                print("3-Evaluar Cadenas")
                print("4-Reportes")
                print("5-Cargar archivos de entrada")
                print("6-Salir")
                opc = int(input("A que módulo desea ingresar: "))

                if opc == 1:
                    nombre =""
                    nombre = input("Ingrese el nombre para el AFD: ")
                    opc1.menu_opc1()
                    limpiar()
                    opc1()
                elif opc == 2:
                    print("Móddulo para la creación de grámatica\n")
                elif opc == 3:
                    limpiar()
                    print("Módulo para la evaluación de cadenas\n")
                elif opc == 4:
                    limpiar()
                    print("Módulo para los reportes\n")
                elif opc == 5:
                    limpiar()
                    print("Cargar archivos de entrada\n")
                elif opc == 6:
                    limpiar()
                    print("Gracias por utilizar la aplicación")
                else:
                    print("Opción incorrecta\n")
                    limpiar()
        except:
            print("*****Debe ingresar un opción correcta*****\n")
            limpiar()

#Método para limpiar pantalla
def limpiar():
    time.sleep(1)

    if platform.system()=='Windows':
        os.system('cls')
    else:
        os.system('clear')