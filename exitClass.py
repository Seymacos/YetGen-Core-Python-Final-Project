import pygame

class Exit(pygame.sprite.Sprite):
    def __init__(self,x,y,image_path,new_width, new_height):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self, surface):
        surface.blit(self.image, self.rect)