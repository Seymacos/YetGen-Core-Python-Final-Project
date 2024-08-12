import pygame

# Yılan sınıfı Sağdan sola doğru
class Snake1(pygame.sprite.Sprite):
    def __init__(self, y, width, height, image_path, speed, screen_width, new_width, new_height):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.smoothscale(self.image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = screen_width
        self.x_change = -speed

    def update(self):
        self.rect.x += self.x_change
        if self.rect.right < 0:
            self.rect.left = self.rect.width  # Yılan ekranın solundan çıkarsa, sağa geri dön

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Diğer düşman sınıfları (Snake2, goodMushrooms, badMushrooms, Bird) de bu dosyaya eklenebilir.
