usuario_correcto = "alumno"
clave_correcta = "python123"

#2. Permitir máximo 3 intentos para ingresar usuario y clave.
#3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.

intentos_maximos = 3
acceso_concedido = False

for intento in range(1, intentos_maximos + 1):
    print(f"Intento {intento}/{intentos_maximos}")
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.\n")
        acceso_concedido = True
        break
    else:
        print("Error: credenciales inválidas.\n")

if not acceso_concedido:
    print("Cuenta bloqueada.")
else:
    while acceso_concedido:
        print("""
        1) Estado
        2) Cambiar clave
        3) Mensaje
        4) Salir
        """)
        opcion = input("Ingrese una opcion valida:")

        #validacion del menu
        if not opcion.isdigit():
            print("Error: ingrese un número válido.\n")
            continue

        opcion_num = int(opcion)
        if opcion_num < 1 or opcion_num > 4:
            print("Error: opción fuera de rango.\n")
            continue

        # Opciones del menú
        if opcion_num == 1:
            print("Estado: Inscripto\n")

        elif opcion_num == 2: #cambio de clave
            while True:
                nueva_clave = input("Nueva clave: ")
                if len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres.\n")
                    continue

                confirmacion = input("Confirmar nueva clave: ")
                if nueva_clave != confirmacion:
                    print("Error: las claves no coinciden. Intente nuevamente.\n")
                    continue

                clave_correcta = nueva_clave
                print("Clave cambiada con éxito.\n")
                break

        elif opcion_num == 3:
            print("Mensaje: 'El éxito es la suma de pequeños esfuerzos repetidos día tras día'\n")

        elif opcion_num == 4:
            print("Sesión cerrada. ¡Hasta luego!")
            break