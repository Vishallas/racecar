import serial
import sys
import pygame

pygame.init()

display = pygame.display.set_mode((300,300))
arduino = serial.Serial('com9',112500)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP :
                print("Accelerate")
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            print("KEYDOWN")
    pygame.display.update()
