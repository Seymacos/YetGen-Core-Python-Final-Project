import pygame
# Mario karakteri sınıfı
class Mario(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load("mario.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.screen_width // 2  # Mario'yu ekranın ortasına yerleştir
        self.rect.y = self.screen_height - self.rect.height  # Mario'nun başlangıç y pozisyonu
        self.is_jumping = False
        self.jump_height = 15  # Zıplama yüksekliği
        self.max_jump_duration = 15  # Maksimum zıplama süresi
        self.jump_speed = 15
        self.gravity = 1  # Yerçekimi kuvveti
        self.velocity_y = 0
        self.velocity_x = 0
        self.move_speed = 5  # Yatay hareket hızı

    def handle_input(self, keys):
        # Yatay hareket
        if keys[pygame.K_LEFT]:
            self.velocity_x = -self.move_speed
        elif keys[pygame.K_RIGHT]:
            self.velocity_x = self.move_speed
        else:
            self.velocity_x = 0  # Tuş bırakıldığında dur

        # Zıplama başlangıcı
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = -self.jump_speed

    def handle_jump(self):
        if self.is_jumping:
            # Yerçekimi etkisini uygula
            self.velocity_y += self.gravity
            self.rect.y += self.velocity_y

            # Zeminle çarpışmayı kontrol eder
            if self.rect.bottom >= self.screen_height:
                self.rect.bottom = self.screen_height
                self.is_jumping = False
                self.velocity_y = 0
        
    def update(self, keys):
        self.handle_input(keys)  # Kullanıcı girişlerini kontrol et
        self.handle_jump()  # Zıplama ve yerçekimi işlemlerini yap

        # Yatay hareketi uygula
        self.rect.x += self.velocity_x

        # Ekran sınırları içinde kalmasını sağla
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.screen_width:
            self.rect.right = self.screen_width



    def draw(self, screen):
        screen.blit(self.image, self.rect)    


"""
class healtyBar ():
    def __init__(self,image,x,y,healty):

        super().__init__()
        self.image= pygame.image.rect
        self.rect= self.image.get_rect()
        self.rect.y=y
        self.x=x

    def draw(self, screen):
        screen.blit(self.image, self.rect)        
        """   