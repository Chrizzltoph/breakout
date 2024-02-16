# Importieren der Pygame-Bibliothek
import pygame, sys, time, random
from pygame.locals import *

# unser Multiplikator 
MULTIPLIKATOR = 20

# Spielfeld erzeugen über Berechnung
fenster = pygame.display.set_mode((20 * MULTIPLIKATOR, 30 * MULTIPLIKATOR))

# Titel für Fensterkopf
pygame.display.set_caption("Breakout in Python")
spielaktiv = True

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

# genutzte Farben
ORANGE  = ( 255, 140,   0)
SCHWARZ = (   0,   0,   0)
WEISS   = ( 255, 255, 255)

# Spielfeld mit Mauersteinen 
karte=[
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0],
[0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
[0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

# Hintergrundfarbe Fenster
fenster.fill(WEISS)

# Korrekturfaktor berechnen
def kor(zahl):
    zahl = zahl * MULTIPLIKATOR
    return zahl

# Spielelement zeichnen
def element_zeichnen(spalte,reihe):
    pygame.draw.rect(fenster, ORANGE, [kor(spalte)+1, kor(reihe)+1,kor(1)-1,kor(1)-1])

# Ausgabe Mauersteine im Spielfenster
for x in range(0,20):
    for y in range(0,27):
        if karte[y][x] != 0:
            element_zeichnen(x,y)

# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            spielaktiv = False
            print("Spieler hat beendet")

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(10)

pygame.quit()