import pygame 
pygame.init()

scwid= 1000
scheight= 700
win= pygame.display.set_mode((scwid,scheight))
pygame.display.set_caption("Pikseller's Game")

# background images 
sun= pygame.image.load("sun.png")
backg= pygame.image.load("sky.png")

run= True 
while run:
    win.blit(backg, (0,0))
    win.blit(sun, (100,100))

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run= False
            
    pygame.display.update()


