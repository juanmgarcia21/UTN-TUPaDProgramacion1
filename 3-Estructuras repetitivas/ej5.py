# Paso 1: Configuración del Personaje
while True:
    gladiador = input("Nombre del Gladiador: ")
    if gladiador.isalpha():
        break
    print("Error: Solo se permiten letras.")

# Paso 2: Inicialización de Estadísticas
vida_gladiador = 100        
vida_enemigo = 100          
pociones = 3                
dano_ataque_pesado = 15     
dano_enemigo = 12           
turno_gladiador = True      

print("\n=== INICIO DEL COMBATE ===")

# Paso 3: El Ciclo de Combate
while vida_gladiador > 0 and vida_enemigo > 0:
    print(f"\n{gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    
    # --- TURNO DEL JUGADOR ---
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    
    opcion = input("Opción: ")
    
    # Validación del menú
    if not opcion.isdigit():
        print("Error: Ingrese un número válido.")
        continue
        
    opcion_num = int(opcion)
    if opcion_num < 1 or opcion_num > 3:
        print("Error: Opción fuera de rango (elija 1, 2 o 3).")
        continue

    # Acción A: Ataque Pesado
    if opcion_num == 1:
        if vida_enemigo < 20:
            dano_final = dano_ataque_pesado * 1.5  # Golpe crítico (float)
            print("¡GOLPE CRÍTICO!")
        else:
            dano_final = float(dano_ataque_pesado)
            
        vida_enemigo -= int(dano_final)
        print(f"¡Atacaste al enemigo por {dano_final} puntos de daño!")

    # Acción B: Ráfaga Veloz
    elif opcion_num == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for golpe in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    # Acción C: Curar
    elif opcion_num == 3:
        if pociones > 0:
            vida_gladiador += 30
            pociones -= 1
            print(f"Te has curado. Recibes +30 HP. Pociones restantes: {pociones}")
        else:
            print("¡No quedan pociones! Pierdes la oportunidad de curarte.")

    # --- TURNO DEL ENEMIGO ---
    # Se ejecuta si el enemigo sigue vivo tras la acción del jugador
    if vida_enemigo > 0:
        vida_gladiador -= dano_enemigo
        print(f">> ¡El enemigo contraataca por {dano_enemigo} puntos de daño!")

# Paso 4: Fin del Juego
print("\n" + "="*40)
if vida_gladiador > 0:
    print(f"¡VICTORIA! {gladiador} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
print("="*40)