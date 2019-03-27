# Autor: Sofía Daniela Méndez Sandoval, AO1242259
# Descripción: Espirógrafo


import pygame
import math


ANCHO = 640
ALTO = 480

BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)



def dibujar(r, R, l):

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        k = r/R
        for angulo in range(0, 360 *r//math.gcd(r, R)):
            a = math.radians(angulo)
            x = int(R*(((1-k)*math.cos(a)+l*k*math.cos((1-k)/k*a))))
            y = int(R*(((1-k)*math.sin(a)-l*k*math.sin((1-k)/k*a))))
            pygame.draw.circle(ventana, ROJO, (x + ANCHO // 2, ALTO // 2 - y), 1)


        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()



def main():

    r = int(input("\n¿Cuál es el radio menor? "))
    R = int(input("¿Cuál es el radio mayor? "))
    l = float(input("¿Cuál es el valor de l? "))

    dibujar(r, R, l)


main()