# %% 
import random
from datetime import datetime


class Juego: 
    print("Empieza el juego")
    nombre_jugador = input("¿Cómo te llamas? ")
    hora = datetime.now().replace(microsecond=0)

    colores= {
        'verde': '\033[32m',
        'amarillo': '\033[93m',
        'rojo': '\033[91m',
        'End': '\033[0m',
        'azul': '\033[94m'
    }
    def color_numero(numero, color):
        return colores[color] + numero + colores['End']

    win = False
    quitar= ","

    # Generar lista Random
    listaRandom =[]
    for i in range(5):
        listaRandom.append(random.randint(1,9)) 

    textRandom  = ",".join(str(e) for e in listaRandom)

    for j in quitar:
        textRandom = textRandom.replace(j, "")
    print ("Numero ganador secreto ", listaRandom)

    #Inicializamos el tablero del juego
    tablero = []
    for i in range(5):
    tablero.append(['_' for l in range(5)])

    quitarEspacio = " "
    numerosDeJugadas = []
    ciclo_juego = 0
    while (not win) and (ciclo_juego < len(textRandom)):
        num_usu = input("ingrese su jugada")
        numerosDeJugadas.append(num_usu)
        for espacio in quitarEspacio:    
            num_usu = num_usu.replace(espacio, "")


        while len(num_usu) != len(textRandom):    
            print (f"Debe ingresar {len(textRandom)} numeros")
            num_usu = input("Intentelo de nuevo")
            for espacio in quitarEspacio:    
                num_usu = num_usu.replace(espacio, "")
                numerosDeJugadas.append(num_usu)

        #condicion de victoria
        if textRandom == num_usu:
            tablero[ciclo_juego] = [l for l in num_usu]
            win = True

        #compruebo numero en posicion
        else:
            numeroPosicion =[]
            for j in range (len(num_usu)):
                if num_usu[j] == textRandom[j]:
                    numeroPosicion.append(color_numero (num_usu[j],'verde'))
                elif num_usu [j] in textRandom:
                    numeroPosicion.append(color_numero(num_usu[j],'amarillo'))
                else:
                    numeroPosicion.append(color_numero(num_usu[j],'rojo'))
                
            tablero[ciclo_juego] = [l for l in numeroPosicion]

        #Dibujamos el tablero
        for i in range(5):
            print(" ".join(tablero[i]))
        
        ciclo_juego += 1

        if win:
            print("Ganaste", nombre_jugador)
            print("Fecha y hora de la jugada:", hora)
            print(f"Duracion de la partida:", datetime.now() - hora)
            print(f"Cantidad de intentos para ganar: {ciclo_juego}")
            print(f"Numeros con los que jugaste {numerosDeJugadas}")
        

        

# %%
