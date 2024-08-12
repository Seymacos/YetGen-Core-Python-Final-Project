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

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# Yılan sınıfı Soldan sağa doğru
class Snake2(pygame.sprite.Sprite):
    def __init__(self, y, width, height, image_path, speed, screen_width, new_width, new_height):
        super().__init__()
       
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.smoothscale(self.image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = 0 #Yılan ekranın sağ tarafından başlayacak
        self.x_change = speed #Yılanın hızı
        self.y_change = 0

    def update(self):
        self.rect.x += self.x_change

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class goodMushrooms(pygame.sprite.Sprite):
    def __init__(self,x,y,image_path, new_width, new_height):
        super().__init__()
        self.image= pygame.image.load(image_path)
        self.image = pygame.transform.smoothscale(self.image, (new_width, new_height))
        self.rect= self.image.get_rect()
        self.rect.y=y
        self.x=x


class badMushrooms(pygame.sprite.Sprite):
    def __init__(self,x,y,image_path, new_width, new_height):
        super().__init__()
        self.image= pygame.image.load(image_path)
        self.image = pygame.transform.smoothscale(self.image, (new_width, new_height))
        self.rect= self.image.get_rect()
        self.rect.y=y
        self.x=x
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image_path, speed, new_width, new_height):
        super().__init__()
       
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.smoothscale(self.image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.x_change = speed
        self.y_change = 0


    def update(self):
        self.rect.x += self.x_change
       
       
    def draw(self, surface):
        surface.blit(self.image, self.rect)

