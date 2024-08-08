import pygame
import random

# Pygame'i başlat
pygame.init()

# Ekran boyutları
screenWidth = 1280
screenHeight = 720

# Ekran oluştur
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Resim yolu
image_path =  "C:\\Users\\USER\\Downloads\\snake.png"
# Yılan sınıfı
class Snake(pygame.sprite.Sprite):
    def __init__(self, y, width, height, image_path, speed):
        super().__init__()
        self.image = pygame.image.load(image_path)
        #self.image = pygame.transform.scale(self.image, (width, height))  # Resmi yılan boyutuna ölçeklendir
        self.image = pygame.transform.smoothscale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = screenWidth #Yılan ekranın sağ tarafından başlayacak
        self.x_change = speed #Yılanın hızı
        self.y_change = 0

    def update(self):
        self.rect.x -= self.x_change #Yılanı sağdan sola hareket ettir.
   
    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Tüm sprite'ları tutacak grup
all_sprites = pygame.sprite.Group()

snake1 = Snake(y=600, width=100, height=100, image_path=image_path, speed=5)
snake2 = Snake(y=600, width=100, height=100, image_path=image_path, speed=10)
snake3 = Snake(y=600, width=100, height=100, image_path=image_path, speed=2)

all_sprites.add(snake1, snake2,snake3)

# Ana döngü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Yılanı güncelle
    all_sprites.update()

    # Ekranı açık sarıya boyayalım
    screen.fill((255, 255, 153))

    # Yılanı çiz
    all_sprites.draw(screen)

    # Ekranı güncelle
    pygame.display.flip()

    # FPS ayarı
    pygame.time.Clock().tick(60)

pygame.quit()
