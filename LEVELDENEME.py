import pygame
import sys
from enemies import Snake1, Snake2, badMushrooms, goodMushrooms, Bird
from marioDeneme import Mario
from background_new import World, grid_screen
from menu import Menu

# Pygame'i başlat
pygame.init()

# Ekran boyutları
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
# oyun 
game_over=0
max_levels=3
level=1

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("************")

# Renkler
LIGHT_BLUE = (173, 216, 230)

# background images
sun = pygame.image.load("sun.png")
backg = pygame.image.load("sky.png")
backg_new = pygame.transform.scale(backg, (SCREEN_WIDTH, SCREEN_HEIGHT))


# ekranı bölüyoruz, parçaları yerleştirmeyi kolaylaştırmak için 12*20 (değişebilir)
tile_size = 40 # mainde grid_screen func çağırılacak

# 1 toprak , 2 çimli , 3 yılan sol , 4 yılan sağ, 5 iyi mant, 6 kötü mant, 7 çıkış

world_data = [
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0,1],
    [1,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,1],
    [1,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,3,3,3,2,0,0,0,0,0,0,0,0,0,2,1],
    [1,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,1],
    [1,0,0,0,5,2,2,6,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,2,2,2,2,1,1,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

world = World(world_data)

# Mario karakterini başlat
mario = Mario(SCREEN_WIDTH, SCREEN_HEIGHT)

# Düşmanları güncelle
all_sprites = pygame.sprite.Group()
world = World(world_data)

# Menü
menu = Menu(SCREEN_WIDTH, SCREEN_HEIGHT)
in_menu = True

# Oyun döngüsü
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if in_menu:
        # Menü ekranını çiz
        menu.draw_menu(screen)

        # Menü olaylarını yönet
        action = menu.handle_events()
        if action == "start":
            in_menu = False
        elif action == "options":
            # Option ekranı burada işlenebilir
            pass
        elif action == "quit":
            pygame.quit()
            sys.exit()
    else:
        keys = pygame.key.get_pressed()

        # ekranı böl ve arka planı koy
        screen.blit(backg_new, (0, 0))

        # Mario'nun hareketini yönet
        mario.update(world, all_sprites)
        all_sprites.update()

        # Mario'yu ekrana çiz
        grid_screen(screen)

        world.draw(screen)
        mario.draw(screen)
        world.all_sprites_group.update()

        # Düşmanları ekrana çiz
        all_sprites.draw(screen)
        
        # eğer player kaybettiyse:

        #eğer player kazandıysa:


    # Ekranı güncelle
    pygame.display.flip()
    clock.tick(60)
