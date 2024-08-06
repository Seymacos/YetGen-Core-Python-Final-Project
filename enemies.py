import pygame
import random

# Pygame'i başlat
pygame.init()

# Ekran boyutları
screenWidth = 1280
screenHeight = 720

# Ekran oluştur
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Yılan sınıfı
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #eni boyu
        self.image = pygame.Surface([200, 10])
        #rengi
        self.image.fill((255, 0, 0))  
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screenWidth - self.rect.width)
        self.rect.y = random.randint(0, screenHeight - self.rect.height)
        #Yatay hareket hızı
        self.change_x = random.choice([-10, 10])
        #Dikey hareket hızı
        self.change_y = random.choice([-2, 2])

    def update(self):
        #X deki konum sabit
        self.rect.x += self.change_x
        #Y deki konum değişken
        self.rect.y += self.change_y
        #Yön değiştirme şimdilik aktif değil
        #if self.rect.right >= screenWidth or self.rect.left <= 0:
         #   self.change_x *= -1
        #if self.rect.bottom >= screenHeight or self.rect.top <= 0:
         #   self.change_y *= -1

# Tüm sprite'ları tutacak grup
all_sprites = pygame.sprite.Group()

# Yılanı oluştur ve gruba ekle
snake = Snake()
all_sprites.add(snake)

# Ana döngü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Sprite'ları güncelle
    all_sprites.update()

    # Ekranı açık sarıya boyayalım
    screen.fill((255, 255, 153))

    # Tüm sprite'ları çiz
    all_sprites.draw(screen)

    # Ekranı güncelle
    pygame.display.flip()

    # FPS ayarı
    pygame.time.Clock().tick(60)

pygame.quit()
