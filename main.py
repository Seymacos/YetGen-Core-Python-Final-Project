import pygame
import sys
from enemies import Snake1, Snake2, badMushrooms, goodMushrooms, Bird
from marioDeneme import Mario
from scrolling_background import grid_screen , World, world_data



# Pygame'i başlat
pygame.init()

# Ekran boyutları
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("************")

# Renkler
LIGHT_BLUE = (173, 216, 230)

# background images 
sun= pygame.image.load("sun.png")
backg= pygame.image.load("sky.png")
backg_new= pygame.transform.scale(backg, (SCREEN_WIDTH, SCREEN_HEIGHT))

# ekranı bölüyoruz, parçaları yerleştirmeyi kolaylaştırmak için 12*20 (değişebilir)
tile_size= 40 # mainde grid_screen func çağırılacak
scroll_speed=3
background_scroll= 0

#world
world= World(world_data)

# Mario karakterini başlat
mario = Mario(SCREEN_WIDTH, SCREEN_HEIGHT)

# Arka planın x koordinatı
background_x = 0

# Düşmanları başlat (örnekler)
snake1 = Snake1(y=200, width=100, height=100, image_path="snake.png", speed=5, screen_width=SCREEN_WIDTH, new_width=100, new_height=100)
snake2 = Snake2(y=600, width=100, height=100, image_path="snake2.png", speed=2, screen_width=SCREEN_WIDTH, new_width=100, new_height=100)

# Tüm sprite'ları tutacak grup
all_sprites = pygame.sprite.Group()
all_sprites.add(snake1)

# Oyun döngüsü
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    #ekranı böl ve arka planı koy
    screen.blit(backg_new, (0,0))
    
    grid_screen()

    world.draw()
    # Mario'nun hareketini yönet
    mario.handle_input(keys)

    # Düşmanları güncelle
    all_sprites.update()

    # Arka planı kaydır
    background_x -= 3  # Arka planın kayma hızı


    # Arka planı sonsuz kaydırmak için arka planın tekrar eden parçalarını çiz
    # pygame.draw.rect(screen, LIGHT_BLUE, (background_x, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

    # Mario'yu ekrana çiz
    mario.draw(screen)

    # Düşmanları ekrana çiz
    all_sprites.draw(screen)
     
    # update the scroll position to make it continuous
    background_scroll+= scroll_speed
    if background_scroll>= SCREEN_WIDTH:
        background_scroll= 0
    pygame.display.update()

    # Ekranı güncelle
    pygame.display.flip()
    clock.tick(60)
