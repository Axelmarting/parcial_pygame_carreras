import pygame

class Pausa:
    posicion = 0,0
    juego_pausado = True
    visible = False
    posicion_abandonar = (380,160)
    foto_boton_abandonar = pygame.image.load(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\ordenado\fotos\botonAbandonar.png")
    rectangulo_abandonar = foto_boton_abandonar.get_rect(topleft=posicion_abandonar)

    def dibujar(self, pantalla):
        if self.visible:
            foto_pausa = pygame.image.load(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\ordenado\fotos\Menu_pausa.png")
            pantalla.blit(foto_pausa, (self.posicion))
            pantalla.blit(self.foto_boton_abandonar, self.posicion_abandonar)

    def reiniciar(self):
        # self.juego_pausado = True
        self.visible = False