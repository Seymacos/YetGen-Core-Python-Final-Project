import pygame
import random

# Pygame'i başlat
pygame.init()

# Ekran boyutları
screenWidth = 1280
screenHeight = 720
backgroundWidth=1600
# Ekran oluştur
screen = pygame.display.set_mode((screenWidth, screenHeight))
a1=0.07
new_width1 = int(screenWidth * a1)
new_height1 = int(screenHeight * a1)
a2=0.1
new_width2 = int(screenWidth * a2)
new_height2 = int(screenHeight * a2)

image_path1 = "snake.png"
image_path2 = "snake2.png"
image_path3= "C:\\Users\\USER\\Downloads\\pngwing.com.png"
image_path4= "C:\\Users\\USER\\Downloads\\pngwing.com (1).png"
image_path5="C:\\Users\\USER\\Downloads\\I want an evil  73041113-7bd8-4b6a-97ad-ea25dfddc33e.png"
# Yılan sınıfı Sağdan sola doğru
class Snake1(pygame.sprite.Sprite):
    def __init__(self, y, width, height, image_path, speed):
        super().__init__()
        
        self.image = pygame.image.load(image_path)
        #self.image = pygame.transform.scale(self.image, (width, height))  # Resmi yılan boyutuna ölçeklendir
        self.image = pygame.transform.smoothscale(self.image, (new_width1, new_height1))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = screenWidth #Yılan ekranın sağ tarafından başlayacak
        self.x_change = - speed #Yılanın hızı
        self.y_change = 0

    def update(self):
        self.rect.x += self.x_change #Yılanı soldan sağa hareket ettir.
        # Yılan ekranın sol tarafından çıkarsa, ekranın sağ tarafına geri dön
        if self.rect.right < 0:
            self.rect.left = screenWidth  
    def draw(self, surface):
        surface.blit(self.image, self.rect)


# Yılan sınıfı Soldan sağa doğru
class Snake2(pygame.sprite.Sprite):
    def __init__(self, y, width, height, image_path, speed):
        super().__init__()
        
        self.image = pygame.image.load(image_path)
        #self.image = pygame.transform.scale(self.image, (width, height))  # Resmi yılan boyutuna ölçeklendir
        self.image = pygame.transform.smoothscale(self.image, (new_width2, new_height2))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = 0 #Yılan ekranın sağ tarafından başlayacak
        self.x_change = speed #Yılanın hızı
        self.y_change = 0

    def update(self):
        self.rect.x += self.x_change #Yılanı soldan sağa hareket ettir.
        # Yılan ekranın sol tarafından çıkarsa, ekranın sağ tarafına geri dön
        if self.rect.left > screenWidth:
            self.rect.right = 0  
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class goodMushrooms(pygame.sprite.Sprite):
    def __init__(self,x,y,image_path):
        super().__init__()

        self.image= pygame.image.load(image_path)
        self.image = pygame.transform.smoothscale(self.image, (new_width1, new_height1))
        self.rect= self.image.get_rect()
        self.rect.y=y
        self.x=x

class badMushrooms(pygame.sprite.Sprite):
    def __init__(self,x,y,image_path):
        super().__init__()

        self.image= pygame.image.load(image_path)
        self.image = pygame.transform.smoothscale(self.image, (new_width2, new_height2))
        self.rect= self.image.get_rect()
        self.rect.y=y
        self.x=x
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image_path, speed):
        super().__init__()
        
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.smoothscale(self.image, (new_width2, new_height2))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.x_change = speed 
        self.y_change = 0

    def update(self):
        self.rect.x += self.x_change 
       
        if self.rect.left > screenWidth:
            self.rect.right = 0  
    def draw(self, surface):
        surface.blit(self.image, self.rect)
'''
    def poops(self,x,y):
        poops=[]
            # Pisleme: belirli aralıklarla
        if random.randint(1, 50) == 1:
           poops.append(x, y)

    # Pislikleri güncelle ve çiz
        for poop in poops:
           poop[1] += 7  # Pisliği aşağı hareket ettir
           pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(poop[0], poop[1], 10, 20))

   '''



# Tüm sprite'ları tutacak grup
all_sprites = pygame.sprite.Group()

snake1 = Snake1(y=200, width=100, height=100, image_path=image_path1, speed=5)
snake2 = Snake2(y=600, width=100, height=100, image_path=image_path2, speed=2)
mushrooms1= goodMushrooms(200,100,image_path3)
mushrooms2= badMushrooms(200,400,image_path4)
bird = Bird(x=200,y=600, width=100, height=100, image_path=image_path5, speed=2)
#all_sprites.add(snake1, snake2,snake3)
all_sprites.add(snake1,snake2,mushrooms1,mushrooms2,bird)


# Ana döngü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Yılanı güncelle
    all_sprites.update()

    # Ekranı açık sarıya boyayalım
    #screen.fill((255, 255, 153))
  
    # Yılanı çiz
    all_sprites.draw(screen)

    # Ekranı güncelle
    pygame.display.flip()

    # FPS ayarı
    pygame.time.Clock().tick(60)

pygame.quit()
