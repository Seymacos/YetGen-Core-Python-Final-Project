import pygame

#Yılan sınıfı 
class Ghosts(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, move_distance=40, speed=1):
        super().__init__()
        self.original_image = pygame.image.load(image_path) 
        self.image = pygame.transform.scale(self.original_image, (80,40))#Boyutun ölçeklendirilmesi
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_distance = move_distance  # Hareket mesafesi
        self.speed = speed
        self.direction = 1  # 1 sağa, -1 sola hareket eder
        self.start_x = x  # Başlangıç x konumu
        self.end_x = x + move_distance  # Hedef x konumu


    def update(self):
        # Yılanın hareketini günceller.
        self.rect.x += self.speed * self.direction

        # Hareket mesafesine ulaştığında yönü değiştirir.
        if self.rect.x >= self.end_x or self.rect.x <= self.start_x:
            self.direction *= -1


        # Güncellenmiş rect boyutlarını yeniden belirleyin
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

#Mantar sınıfı
class Mushrooms(pygame.sprite.Sprite):
    def __init__(self,x,y,image_path, new_width, new_height):
        super().__init__()
        self.image= pygame.image.load(image_path)
        self.image = pygame.transform.smoothscale(self.image, (new_width, new_height))
        self.rect= self.image.get_rect()
        self.rect.y=y
        self.rect.x=x

    def draw(self, surface):
        surface.blit(self.image, self.rect)

#Kuş sınıfı
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, move_distance=40, speed=1):
        super().__init__()
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, (50,40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_distance = move_distance  # Hareket mesafesi
        self.speed = speed
        self.direction = 1  # 1 sağa, -1 sola hareket eder
        self.start_x = x  # Başlangıç x konumu
        self.end_x = x + move_distance  # Hedef x konumu


    def update(self):
        # Yılanın hareketini güncelle
        self.rect.x += self.speed * self.direction

        # Hareket mesafesine ulaştığında yönü değiştir
        if self.rect.x >= self.end_x or self.rect.x <= self.start_x:
            self.direction *= -1
        # Görüntüyü döndürür.
        if self.direction == 1:
            # Sağ yönünde hareket ederken
            self.image = pygame.transform.flip(self.image, False, False)
        else:
            # Sol yönünde hareket ederken
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect(topleft=self.rect.topleft)

    def draw(self, surface):
        surface.blit(self.image, self.rect)