from enemies import EnemyClass
from background import BackgroundClass
from marioCharacter import CharacterClass
import pygame

# Pygame'i başlat
pygame.init()

# Ekran boyutları
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Saat nesnesi oluştur
clock = pygame.time.Clock()

# Diğer dosyalardan sınıf örneklerini oluştur
enemy = EnemyClass()
background = BackgroundClass()
character= CharacterClass()

# Ana oyun döngüsü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Arka planı çiz
    background.draw(screen)

    # Düşmanları çiz ve güncelle
    enemy.update()
    enemy.draw(screen)

    character.update()
    character.draw(screen)
    # Ekranı güncelle
    pygame.display.flip()

    # FPS ayarı
    clock.tick(60)

pygame.quit()
