import pygame

class Menu:
    posicion_fondo = 0,0
    visible = True
    posicion_jugar = (380,330)
    posicion_scores = (380,530)
    foto_boton_jugar = pygame.image.load(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\fotos\botonJugar.png")
    rectangulo_jugar = foto_boton_jugar.get_rect(topleft=posicion_jugar)
    foto_boton_scores = pygame.image.load(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\fotos\botonScores.png")
    rectangulo_scores = foto_boton_scores.get_rect(topleft=posicion_scores)

    def dibujar(self, pantalla):
        if self.visible:
            foto_menu = pygame.image.load(r"C:\Users\Axel\Desktop\Programacion_1\segundo_parcial\fotos\menu_principal.png")
            pantalla.blit(foto_menu, (self.posicion_fondo))
            pantalla.blit(self.foto_boton_jugar, self.posicion_jugar)
            pantalla.blit(self.foto_boton_scores, self.posicion_scores)

        