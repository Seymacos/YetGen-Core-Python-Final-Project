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
        self.width =self.image.get_width()
        self.height =self.image.get_height()
        self.is_jumping = False
        self.jump_height = 15  # Zıplama yüksekliği
        self.jump_speed = 15
        self.gravity = 1  # Yerçekimi kuvveti
        self.velocity_y = 0
        self.velocity_x = 0
        self.move_speed = 5  # Yatay hareket hızı
        self.is_alive = True  # Mario'nun canlı olup olmadığını belirler
        
    def update(self, world, enemies):
        if not self.is_alive:
            return  # Eğer Mario ölmüşse, hiçbir işlem yapılmaz
      
        dx=0
        dy=0
        
        #Klavye girdileri
        key= pygame.key.get_pressed()

        #Karakterin zıplaması
        if key[pygame.K_SPACE] and not self.is_jumping:
            self.velocity_y=-self.jump_speed
            self.is_jumping=True

        #Yerçekiminin düşmeye etkisi
        self.velocity_y+=self.gravity
        #Y düzleminde hareket -dikey-
        dy += self.velocity_y


        #X düzleminde hareket -yatay-
        if key[pygame.K_LEFT]:
            dx-=self.move_speed

        if key[pygame.K_RIGHT]:
            dx+=self.move_speed


        # Çarpışma kontrolü
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                dx = 0  # Yatay hareket durdurulur

            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                if self.velocity_y < 0:
                    dy = tile[1].bottom - self.rect.top  # Yukarıya doğru çarpışma
                elif self.velocity_y >= 0:
                    dy = tile[1].top - self.rect.bottom  # Aşağıya doğru çarpışma
                    self.is_jumping = False
                    self.velocity_y = 0
        # Çarpışma kontrolü (düşmanlarla)
        if self.check_collision_with_enemies(enemies):
            self.is_alive = False
            print("Mario öldü!")  # Oyun sonu mesajı veya işlemi
       
       #Oyuncunun koordinatları    
        self.rect.x+=dx
        self.rect.y+=dy

        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
            self.is_jumping = False
            self.velocity_y=0


        # Ekran sınırları içinde kalmasını sağla
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
   
    def check_collision_with_enemies(self, enemies):
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                return True
        return False


    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255,255,255), self.rect,2)    
