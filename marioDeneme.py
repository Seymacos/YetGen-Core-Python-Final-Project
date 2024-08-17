import pygame
import sys
from enemies import Ghosts, Mushrooms,Bird
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
# Mario karakteri sınıfı
class Mario(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load("mario.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.screen_width // 2  # Mario'yu ekranın ortasına yerleştir
        self.rect.y = self.screen_height - self.rect.height  # Mario'nun başlangıç y pozisyonu
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.is_jumping = False
        self.jump_height = 15  # Zıplama yüksekliği
        self.jump_speed = 15
        self.gravity = 1  # Yerçekimi kuvveti
        self.velocity_y = 0
        self.velocity_x = 0
        self.move_speed = 5  # Yatay hareket hızı
        self.is_alive = True  # Mario'nun canlı olup olmadığını belirler
        self.world_data = world_data
        # Mario'nun başlangıç konumunu belirle
        self.find_starting_position()        


    def find_starting_position(self):
        tile_size = 40  # Eğer farklı bir tile boyutu kullanıyorsanız, burayı güncelleyin
        rows = len(self.world_data)
        cols = len(self.world_data[0])

        # Ekranın sol alt köşesinden başlamayı hedefle
        for x in range(0, cols):
            for y in range(rows - 1, -1, -1):
                # Mario'nun çimenli yerlerde olmamasını sağla
                if self.world_data[y][x] == 0:
                    self.rect.x = x * tile_size
                    self.rect.y = y * tile_size
                    return

        # Eğer uygun bir yer bulunamazsa, ekranın sol alt köşesinde kal
        self.rect.x = 0
        self.rect.y = self.screen_height - self.rect.height

    def update(self, world, enemies):
        if not self.is_alive:
            return  # Eğer Mario ölmüşse, hiçbir işlem yapılmaz
      
        dx = 0
        dy = 0
        
        # Klavye girdileri
        key = pygame.key.get_pressed()

        # Karakterin zıplaması
        if key[pygame.K_SPACE] and not self.is_jumping:
            self.velocity_y = -self.jump_speed
            self.is_jumping = True

        # Yerçekiminin düşmeye etkisi
        self.velocity_y += self.gravity
        # Y düzleminde hareket - dikey
        dy += self.velocity_y

        # X düzleminde hareket - yatay
        if key[pygame.K_LEFT]:
            dx -= self.move_speed
        if key[pygame.K_RIGHT]:
            dx += self.move_speed

        # Çarpışma kontrolü
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                dx = 0  # Yatay hareket durdurulur

            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                if self.velocity_y < 0:
                    dy = tile[1].bottom - self.rect.top  # Yukarıya doğru çarpışma
                elif self.velocity_y >= 0:
                    dy = tile[1].top - self.rect.bottom  # Aşağıya doğru çarpışma
                    self.is_jumping = False
                    self.velocity_y = 0

        # Çarpışma kontrolü (düşmanlarla)
        if self.check_collision_with_enemies(enemies):
            self.is_alive = False
            print("Mario öldü!")  # Oyun sonu mesajı veya işlemi

        if self.check_collision_with_exit(exit_gate):
         # Oyuncuyu durdur
            self.display_win()  # Kazandınız mesajını göster
            return

        
        # Oyuncunun koordinatları
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
            self.is_jumping = False
            self.velocity_y = 0

        # Ekran sınırları içinde kalmasını sağla
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.screen_width:
            self.rect.right = self.screen_width

    def check_collision_with_enemies(self, enemies):
        for enemy in enemies:
            if pygame.sprite.collide_rect(self, enemy):
                return True
        return False
    exit_sprite=Exit()
    def check_collision_with_exit(self,exit_sprite):
        if pygame.sprite.collide_rect(self,exit_sprite):
            return True
        return False
    
    def display_win(self):
        font = pygame.font.Font(None, 74)  # Büyük bir yazı tipi oluştur
        text = font.render('KAZANDINIZ!', True, (255, 0, 0))  # Kırmızı renkte yazı
        text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        self.screen.blit(text, text_rect)
        pygame.time.delay(4000)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
