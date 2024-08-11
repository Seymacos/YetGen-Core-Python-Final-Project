import pygame
import sys

# Pygame'i başlat
pygame.init()

# Ekran boyutları
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Super Mario Benzeri Oyun")

# Renkler
LIGHT_BLUE = (173, 216, 230)

# Mario karakteri
mario_img = pygame.image.load("mario.png")
mario_rect = mario_img.get_rect()
mario_rect.x = SCREEN_WIDTH // 2  # Mario'yu ekranın ortasına yerleştir
mario_rect.y = SCREEN_HEIGHT - mario_rect.height  # Mario'nun başlangıç y pozisyonu

# Zıplama değişkenleri
is_jumping = False
jump_height = 20  # Zıplama yüksekliği
max_jump_duration = 15  # Maksimum zıplama süresi
jump_count = 0  # Zıplama süresi sayacı
fall_speed = 7  # Düşme hızı

# Ekran kayması
background_x = 0  # Arka planın x koordinatı

# Oyun döngüsü
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Zıplama kontrolü
    if keys[pygame.K_SPACE] and not is_jumping and mario_rect.y == SCREEN_HEIGHT - mario_rect.height:
        is_jumping = True
        jump_count = 0

    if is_jumping:
        if keys[pygame.K_SPACE] and jump_count < max_jump_duration:
            mario_rect.y -= jump_height
            jump_count += 1
        else:
            is_jumping = False

    # Mario düşüşü
    if not is_jumping:
        if mario_rect.y < SCREEN_HEIGHT - mario_rect.height:
            mario_rect.y += fall_speed
        else:
            mario_rect.y = SCREEN_HEIGHT - mario_rect.height

    # Ekranı kaydır
    background_x -= 3  # Arka planın kayma hızı

    # Ekranı temizle ve arka planı çiz
    screen.fill(LIGHT_BLUE)

    # Mario'yu ekrana çiz (ekranın ortasında sabit kalır)
    screen.blit(mario_img, mario_rect)

    # Arka planı ekrana çiz (arka plan kayıyor)
    # Arka planı sonsuz kaydırmak için arka planın tekrar eden parçalarını çiz
    pygame.draw.rect(screen, LIGHT_BLUE, (background_x, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

    # Ekranı güncelle
    pygame.display.flip()
    clock.tick(60)
