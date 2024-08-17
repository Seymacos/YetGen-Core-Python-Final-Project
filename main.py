import pygame
import sys
from enemies import Ghosts, Mushrooms, Bird
from marioDeneme import Mario
from background_new import World
from menu2 import Menu

# Pygame'i başlat
try:
    pygame.init()
except Exception as e:
    print(f"Pygame başlatılırken bir hata oluştu: {e}")
    sys.exit()

# Ekran boyutları
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
game_over = 0


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("*PIKSELS")

# Renkler
LIGHT_BLUE = (173, 216, 230)
BLACK = (0, 0, 0)

# background images
sun = pygame.image.load("sun.png")
backg = pygame.image.load("sky.png")
backg_new = pygame.transform.scale(backg, (SCREEN_WIDTH, SCREEN_HEIGHT))


# ekranı bölüyoruz, parçaları yerleştirmeyi kolaylaştırmak için 12*20 (değişebilir)
tile_size = 40 # mainde grid_screen func çağırılacak

world_data = [
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,2,0,0,2,0,2,2,0,1,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,5,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,2,0,2,2,2,2,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,5,0,0,0,0,0,2,2,2,2,2,0,0,0,0,5,0,0,0,2,0,0,1],
    [7,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,1],
    [0,0,0,5,0,2,2,0,0,1,1,1,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,2,2,2,2,1,1,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

# Dünya nesnesini oluştur
world = World(world_data)

# Mario karakterini başlat
mario = Mario(SCREEN_WIDTH, SCREEN_HEIGHT)

# Menü
menu = Menu(screen)

in_menu = True

# Oyun döngüsü
clock = pygame.time.Clock()

#def draw_game_over(screen):
#    try:
#        font = pygame.font.Font(None, 74)  # Büyük bir yazı tipi oluştur
#        text = font.render('Oyun Bitti!', True, (255, 0, 0))  # Kırmızı renkte yazı
#        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
#        screen.blit(text, text_rect)
    
def draw_game_over(screen):
    # oyunBitti.jpg resmini yükle
    game_over_image = pygame.image.load('oyunBitti.jpg')
    # Resmi ekranın ortasına yerleştir
    image_rect = game_over_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    # Resmi ekrana çiz
    screen.blit(game_over_image, image_rect)    
    
#    except Exception as e:
#        print(f"Game over yazısı çizilirken bir hata oluştu: {e}")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if in_menu:
        # Menü ekranını çiz
        menu.draw()

        # Menü olaylarını yönet
        action = menu.menu_events()
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

        # Ekranı böl ve arka planı koy
        screen.blit(backg_new, (0, 0))

        # Mario'nun hareketini yönet
        mario.update(world, world.all_sprites_group)

        # Ekranı güncelle
        world.draw(screen)
        mario.draw(screen)
        world.all_sprites_group.update()
        world.all_sprites_group.draw(screen)

        if not mario.is_alive:
            if not game_over:
                game_over = True
                game_over_start_time = pygame.time.get_ticks()  # Şu anki zamanı al

            # Mario öldüyse, oyunun bitişini işleyin
            screen.fill(LIGHT_BLUE)  # Ekranı arka plan rengiyle doldur
            draw_game_over(screen)
            pygame.display.flip()

            # 3 saniye boyunca bekle
            current_time = pygame.time.get_ticks()
            if current_time - game_over_start_time >= 3000:  # 3000 ms = 3 saniye
                # Başlangıç ekranına dön
                in_menu = True
                game_over = False
                mario = Mario(SCREEN_WIDTH, SCREEN_HEIGHT)  # Mario'yu yeniden başlat
                world = World(world_data)  # Dünya nesnesini yeniden oluştur
        else:
            game_over = False
            
        

    # Ekranı güncelle
    pygame.display.flip()
    clock.tick(60)      