# 1. Pedir nombre del operador (solo letras)
while True:
    operador = input("Nombre del operador: ")
    if operador.isalpha():
        break
    print("Error: El nombre debe contener solo letras.")

# Inicializar las variables para los turnos
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

# 2. Menú repetitivo hasta salir
while True:
    print("""
    1. Reservar turno
    2. Cancelar turno (por nombre)
    3. Ver agenda del día
    4. Ver resumen general
    5. Cerrar sistema \n""" )
    
    opcion = input("Elija una opción (1-5): ")
    if not opcion.isdigit():
        print("Error: Ingrese un número válido.")
        continue
        
    opcion_num = int(opcion)
    if opcion_num < 1 or opcion_num > 5:
        print("Error: Opción fuera de rango.")
        continue

 
# OPCIÓN 1: RESERVAR TURNO

    if opcion_num == 1:
        while True:
            dia = input("Elegir día (1=Lunes, 2=Martes): ")
            if dia in ["1", "2"]:
                break
            print("Error: Ingrese 1 para Lunes o 2 para Martes.")
            
        while True:
            paciente = input("Nombre del paciente: ")
            if paciente.isalpha():
                break
            print("Error: El nombre debe contener solo letras.")
            
        if dia == "1":  # LUNES
            if paciente in [lunes1, lunes2, lunes3, lunes4]:
                print(f"Error: El paciente '{paciente}' ya tiene un turno reservado para el Lunes.")
            else:
                if lunes1 == "":
                    lunes1 = paciente
                    print(f"Turno reservado para {paciente} el Lunes (Turno 1).")
                elif lunes2 == "":
                    lunes2 = paciente
                    print(f"Turno reservado para {paciente} el Lunes (Turno 2).")
                elif lunes3 == "":
                    lunes3 = paciente
                    print(f"Turno reservado para {paciente} el Lunes (Turno 3).")
                elif lunes4 == "":
                    lunes4 = paciente
                    print(f"Turno reservado para {paciente} el Lunes (Turno 4).")
                else:
                    print("Error: No hay cupos disponibles para el Lunes.")

        elif dia == "2":  # MARTES
            if paciente in [martes1, martes2, martes3]:
                print(f"Error: El paciente '{paciente}' ya tiene un turno reservado para el Martes.")
            else:
                if martes1 == "":
                    martes1 = paciente
                    print(f"Turno reservado para {paciente} el Martes (Turno 1).")
                elif martes2 == "":
                    martes2 = paciente
                    print(f"Turno reservado para {paciente} el Martes (Turno 2).")
                elif martes3 == "":
                    martes3 = paciente
                    print(f"Turno reservado para {paciente} el Martes (Turno 3).")
                else:
                    print("Error: No hay cupos disponibles para el Martes.")

# OPCIÓN 2: CANCELAR TURNO (POR NOMBRE)
 
    elif opcion_num == 2:
        while True:
            dia = input("Elegir día (1=Lunes, 2=Martes): ")
            if dia in ["1", "2"]:
                break
            print("Error: Ingrese 1 para Lunes o 2 para Martes.")
            
        while True:
            paciente = input("Nombre del paciente a cancelar: ")
            if paciente.isalpha():
                break
            print("Error: El nombre debe contener solo letras.")

        cancelado = False
        if dia == "1":
            if lunes1 == paciente:
                lunes1 = ""
                cancelado = True
            elif lunes2 == paciente:
                lunes2 = ""
                cancelado = True
            elif lunes3 == paciente:
                lunes3 = ""
                cancelado = True
            elif lunes4 == paciente:
                lunes4 = ""
                cancelado = True
                
        elif dia == "2":
            if martes1 == paciente:
                martes1 = ""
                cancelado = True
            elif martes2 == paciente:
                martes2 = ""
                cancelado = True
            elif martes3 == paciente:
                martes3 = ""
                cancelado = True

        if cancelado:
            print(f"Turno de '{paciente}' cancelado exitosamente.")
        else:
            print(f"No se encontró a '{paciente}' en el día seleccionado.")


# OPCIÓN 3: VER AGENDA DEL DÍA

    elif opcion_num == 3:
        while True:
            dia = input("Elegir día para consultar (1=Lunes, 2=Martes): ")
            if dia in ["1", "2"]:
                break
            print("Error: Ingrese 1 para Lunes o 2 para Martes.")

        if dia == "1":
            print("\n--- AGENDA LUNES ---")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        elif dia == "2":
            print("\n--- AGENDA MARTES ---")
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")


# OPCIÓN 4: VER RESUMEN GENERAL

    elif opcion_num == 4:
        # Calcular ocupados Lunes
        ocupados_lunes = 0
        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1
        libres_lunes = 4 - ocupados_lunes

        # Calcular ocupados Martes
        ocupados_martes = 0
        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1
        libres_martes = 3 - ocupados_martes

        print("\n--- RESUMEN GENERAL ---")
        print(f"Lunes : {ocupados_lunes} ocupados | {libres_lunes} disponibles")
        print(f"Martes: {ocupados_martes} ocupados | {libres_martes} disponibles")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos ocupados: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos ocupados: Martes")
        else:
            print("Día con más turnos ocupados: Empate entre Lunes y Martes")


# OPCIÓN 5: CERRAR SISTEMA

    elif opcion_num == 5:
        print("Saliendo del sistema de agenda")
        break