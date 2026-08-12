# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

# Contador para la regla anti-spam
forzar_seguidas = 0

# Pedir nombre del agente
while True:
    agente = input("Nombre del agente: ")
    if agente.isalpha():
        break
    print("Error: El nombre debe contener solo letras.")

print(f"\n¡Bienvenido Agente {agente}! La misión ha comenzado.")

# Ciclo principal del juego
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    # Verificar regla de bloqueo por alarma
    if alarma and tiempo <= 3:
        break

    print(f"\n--- ESTADO ACTUAL ---")
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {'ACTIVADA' if alarma else 'Desactivada'} | Código parcial: '{codigo_parcial}'")
    
    print("\nAcciones:")
    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")
    
    opcion = input("Elija una opción (1-3): ")
    if not opcion.isdigit():
        print("Error: Ingrese un número válido.")
        continue
        
    opcion_num = int(opcion)
    if opcion_num < 1 or opcion_num > 3:
        print("Error: Opción fuera de rango.")
        continue


# OPCIÓN 1: FORZAR CERRADURA
    if opcion_num == 1:
        forzar_seguidas += 1
        energia -= 20
        tiempo -= 2
        
        # Regla anti-spam
        if forzar_seguidas == 3:
            alarma = True
            print("\n¡ALERTA! Forzaste la cerradura 3 veces seguidas y se trabó. Se activó la alarma.")
        else:
            # Riesgo de alarma si energía es menor a 40
            if energia < 40:
                print("\n¡Atención! Energía baja, hay riesgo de activar la alarma.")
                while True:
                    riesgo = input("Elija un número de seguridad (1-3): ")
                    if riesgo.isdigit() and int(riesgo) in [1, 2, 3]:
                        break
                    print("Error: Ingrese un número entre 1 y 3.")
                
                if int(riesgo) == 3:
                    alarma = True
                    print("¡Cometiste un error al forzar! Se activó la alarma.")

            if not alarma:
                cerraduras_abiertas += 1
                print("¡Éxito! Abriste 1 cerradura.")


# OPCIÓN 2: HACKEAR PANEL

    elif opcion_num == 2:
        forzar_seguidas = 0 
        energia -= 10
        tiempo -= 3
        
        print("\nHackeando panel de seguridad...")
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Paso {paso}/4: Progreso del código -> {codigo_parcial}")

        if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("¡Código completado! Se abrió 1 cerradura automáticamente.")


# OPCIÓN 3: DESCANSAR

    elif opcion_num == 3:
        forzar_seguidas = 0  # Rompe la racha anti-spam
        tiempo -= 1
        
        # +15 energía (máximo 100)
        energia = min(100, energia + 15)
        
        # Si alarma ON: -10 energía extra
        if alarma:
            energia -= 10
            print("\nDescansaste, pero la tensión de la alarma encendida te restó 10 de energía extra.")
        else:
            print("\nDescansaste y recuperaste energía.")


# EVALUACIÓN DE CONDICIONES DE FIN DE JUEGO

print("\n" + "="*40)
if cerraduras_abiertas == 3:
    print("¡VICTORIA! Abriste las 3 cerraduras y lograste acceder a la bóveda.")
elif alarma and tiempo <= 3:
    print("DERROTA: El sistema se bloqueó debido a la alarma activa con poco tiempo restante.")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA: Te quedaste sin recursos (energía o tiempo).")
print("="*40)