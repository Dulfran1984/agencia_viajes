list_viajeros = []
import os
sw = True
def fnt_limpiar():
    os.system("cls")
    print('Autor: Dulfran Montaño')
    print('Copyright(c) 2024')
    print('Universidad católica luis amigó\n')
    
def fnt_agente(op):
    fnt_limpiar()
    if op == '1':
        print('<<< AGREGAR VIAJERO >>>\n')
        viajero = ''
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        edad = input('Edad: ')
        if (int(edad) > 0 and int(edad) <= 25):
            viajero = nombre + ' ' + apellido + ' ' + edad
            list_viajeros.append(viajero)
            print('\nViajero agregado correctamente')
            input('Presione <ENTER> para continuar...')
        else:
            print('\nEdad incorrecta')
            input('Presione <ENTER> para continuar...')
    elif op == '2':
        fnt_limpiar()
        print('<<< MOSTRAR VIAJEROS >>>\n')
        if len(list_viajeros) == 0:
            print('\nNo hay viajeros registrados')
            input('Presione <ENTER> para continuar...')
        else:
            for i in list_viajeros:
                print(i)
            input('\nPresione <ENTER> para continuar...')
    
while sw == True:
    fnt_limpiar()
    opcion = input('<<< MENU PRINCIPAL >>>\n1. AGREGAR\n2. MOSTRAR\n3. SALIR\n4. -> ')
    fnt_agente(opcion)