import numpy as np
import pygame
import sys
import math

#POLITECNICO GRANCOLOMBIANO, INGENIERIA DE SOFTWARE, PARADIGMAS DE PROGRAMACION

#JUEGO: CUATRO EN LINEA

# Descripcion: En el presente codigo se realiza la construccion y el modelamiento del juego denominado cuatro en linea como parte del trabajo de la
# asignatura de paradigmas de programacion, el cual consiste en demostrar las destrezas de estrategia matematica al intentar formar una linea consecutiva de 4 piezas
# de su color, donde cada una de ellas tendra un valor de diez puntos, gana el jugador que consigue obtener 40 puntos en linea recta, bien sea esta vertical, horizontal o
# diagonal (ascendente o descendente), impidiendo a su vez que su contrincante alcance dicho objetivo.

# Destrezas que se desarrollan en el juego:
# Concentracion, memoria cognitiva y sensorial, agilidad mental, rapidez matematica de suma aritmetica, pensamiento altoritmico y criterio para la planificacion estrategica.

#Realizado por:
# 1. Diego Alexander Vallejo        100226028
# 2. Yorlandi Grajales Ospina       100261272
# 3. Richard Giovanny Florez Lopez  100223463
# 4. Alvaro Andres Medina           100272405


# Colores utilizados en RGB
AZUL =      (51,69,255)
NEGRO =     (0,0,0)
ROSA =      (189,43,157)
AMARILLO =  (226,235,35)
VERDE =     (10,184,11)

# Declaracion de las filas y columnas a usar en el juego.
CONTADOR_FILA =6
CONTADOR_COLUMNA =7

#Funcion crear tablero
def crear_tablero():
    tablero = np.zeros((CONTADOR_FILA,CONTADOR_COLUMNA))
    return tablero

#Funcion dejar caer la pieza.
def caer_pieza(tablero, fila, col, pieza):
    tablero [fila][col]=pieza

#Funcion verificar una localizacion valida
def es_localizacion_valida(tablero, col):
    return tablero [CONTADOR_FILA-1][col]==0

#Funcion para alcanzar la siguiente fila abierta
def alcanzar_siguiente_fila_abierta(tablero, col):
    for f in range(CONTADOR_FILA):
        if tablero[f][col]==0:
            return f

#Funcion para imprimir el tablero de juego
def imprimir_tablero(tablero):
    print(np.flip(tablero,0))

#Funcion para definir la jugada ganadora
def jugada_ganadora(tablero, pieza):

    # Revisar localizaciones horizontales para ganar
    for c in range (CONTADOR_COLUMNA-3):
        for f in range (CONTADOR_FILA):
            if tablero[f][c]== pieza and tablero[f][c+1]== pieza and tablero[f][c+2]==pieza and tablero[f][c+3]== pieza:
                return True

    # Revisar localizaciones verticales para ganar
        for c in range (CONTADOR_COLUMNA):
            for f in range (CONTADOR_FILA-3):
                if tablero[f][c]== pieza and tablero[f+1][c]== pieza and tablero[f+2][c]==pieza and tablero[f+3][c]== pieza:
                    return True

    #Revisar posibles diagonales
        for c in range (CONTADOR_COLUMNA-3):
            for f in range (CONTADOR_FILA-3):
                if tablero[f][c]== pieza and tablero[f+1][c+1]== pieza and tablero[f+2][c+2]==pieza and tablero[f+3][c+3]== pieza:
                    return True

    #Revisar negativamente diagonales
        for c in range (CONTADOR_COLUMNA-3):
            for f in range (3, CONTADOR_FILA):
                if tablero[f][c]== pieza and tablero[f-1][c+1]== pieza and tablero[f-2][c+2]==pieza and tablero[f-3][c+3]== pieza:
                    return True    

#Funcion para dibujar el tablero de juego
def dibujar_tablero(tablero):
    for c in range(CONTADOR_COLUMNA):
        for f in range (CONTADOR_FILA):
            pygame.draw.rect(screen, AZUL, (c*TAMANO_CUADRADO, f*TAMANO_CUADRADO+TAMANO_CUADRADO, TAMANO_CUADRADO, TAMANO_CUADRADO) )
            pygame.draw.circle(screen, NEGRO, (int(c*TAMANO_CUADRADO+TAMANO_CUADRADO/2), int(f*TAMANO_CUADRADO+TAMANO_CUADRADO+TAMANO_CUADRADO/2)), RADIO)

    for c in range(CONTADOR_COLUMNA):
        for f in range (CONTADOR_FILA):                
            if tablero[f][c] == 1:
                pygame.draw.circle(screen, ROSA, (int(c*TAMANO_CUADRADO+TAMANO_CUADRADO/2), height-int(f*TAMANO_CUADRADO+TAMANO_CUADRADO/2)), RADIO)
            elif tablero[f][c] ==2:
                pygame.draw.circle(screen, AMARILLO, (int(c*TAMANO_CUADRADO+TAMANO_CUADRADO/2), height-int(f*TAMANO_CUADRADO+TAMANO_CUADRADO/2)), RADIO)
    pygame.display.update()


tablero = crear_tablero()
imprimir_tablero(tablero)
game_over = False
turno = 0

pygame.init()

TAMANO_CUADRADO = 100

width = CONTADOR_COLUMNA * TAMANO_CUADRADO
height = (CONTADOR_FILA+1) * TAMANO_CUADRADO

size = (width,height)

RADIO = int(TAMANO_CUADRADO/2-5)

screen = pygame.display.set_mode(size)
dibujar_tablero(tablero)
pygame.display.update()

#Fuente usada en el tablero de juego
myfont = pygame.font.SysFont("monospace",36)

while not game_over:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, NEGRO, (0,0, width, TAMANO_CUADRADO))
            posx = event.pos[0]
            if turno == 0:
                pygame.draw.circle(screen, ROSA, (posx, int(TAMANO_CUADRADO/2)), RADIO)
            else:
                pygame.draw.circle(screen, AMARILLO, (posx, int(TAMANO_CUADRADO/2)), RADIO)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen,NEGRO, (0,0, width, TAMANO_CUADRADO))
            #print (event.pos)

            #Preguntar por entrada jugador 1.
            if turno ==0:
                posx = event.pos[0]
                col = int(math.floor(posx/TAMANO_CUADRADO))

                if es_localizacion_valida(tablero, col):
                    fila = alcanzar_siguiente_fila_abierta (tablero, col)
                    caer_pieza(tablero, fila, col, 1)

                    if jugada_ganadora(tablero,1):
                        label = myfont.render("Jugador 1 gana, 40 puntos¡",1,ROSA)
                        screen.blit(label,(40,10))
                        game_over = True

            #Preguntar por entrada jugador 2.
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/TAMANO_CUADRADO))

                if es_localizacion_valida(tablero, col):
                    fila = alcanzar_siguiente_fila_abierta (tablero, col)
                    caer_pieza(tablero, fila, col, 2)
                    
                    if jugada_ganadora(tablero,2):
                        label = myfont.render("Jugador 2 gana, 40 puntos ¡¡",1,AMARILLO)
                        screen.blit(label,(40,10))
                        game_over = True


            imprimir_tablero(tablero)
            dibujar_tablero(tablero)

            turno += 1
            turno = turno % 2

            #Finalizar juego.
            if game_over:
                pygame.time.wait(4000)
