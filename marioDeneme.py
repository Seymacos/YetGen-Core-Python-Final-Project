import pygame

# Mario karakteri sınıfı
class Mario:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load("mario.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.screen_width // 2  # Mario'yu ekranın ortasına yerleştir
        self.rect.y = self.screen_height - self.rect.height  # Mario'nun başlangıç y pozisyonu
        self.is_jumping = False
        self.jump_height = 20  # Zıplama yüksekliği
        self.max_jump_duration = 15  # Maksimum zıplama süresi
        self.jump_count = 0  # Zıplama süresi sayacı
        self.fall_speed = 7  # Düşme hızı

    def handle_input(self, keys):
        if keys[pygame.K_SPACE] and not self.is_jumping and self.rect.y == self.screen_height - self.rect.height:
            self.is_jumping = True
            self.jump_count = 0

    

