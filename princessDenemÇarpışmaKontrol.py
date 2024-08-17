import pygame

class Princess(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, world_data):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.world_data = world_data
        self.image_right = pygame.image.load("princessRight.png")
        self.image_right = pygame.transform.scale(self.image_right, (60, 80))
        self.image_left = pygame.image.load("princessLeft.png")
        self.image_left = pygame.transform.scale(self.image_left, (60, 80))
        self.image = self.image_right
        self.rect = self.image.get_rect()
        self.rect.x = self.screen_width // 2
        self.rect.y = self.screen_height - self.rect.height
        self.is_jumping = False
        self.jump_height = 10
        self.jump_speed = 10
        self.gravity = 1
        self.velocity_y = 0
        self.velocity_x = 0
        self.move_speed = 5
        self.is_alive = True
        self.find_starting_position()

    def find_starting_position(self):
        tile_size = 40
        rows = len(self.world_data)
        cols = len(self.world_data[0])
        for x in range(0, cols):
            for y in range(rows - 1, -1, -1):
                if self.world_data[y][x] == 0:
                    self.rect.x = x * tile_size
                    self.rect.y = y * tile_size
                    return
        self.rect.x = 0
        self.rect.y = self.screen_height - self.rect.height

    def update(self, world, enemies):
        if not self.is_alive:
            return

        dx = 0
        dy = 0

        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE] and not self.is_jumping:
            self.velocity_y = -self.jump_speed
            self.is_jumping = True
            self.image = self.image_right

        self.velocity_y += self.gravity
        dy += self.velocity_y

        if key[pygame.K_LEFT]:
            dx -= self.move_speed
            self.image = self.image_left
        if key[pygame.K_RIGHT]:
            dx += self.move_speed
            self.image = self.image_right

        self.rect.x += dx
        self.rect.y += dy

        self.check_tile_collision(dx, dy, world)

        if self.check_collision_with_enemies(enemies):
            self.is_alive = False
            print("Mario öldü!")

        if self.check_collision_with_exit(world):
            print("Yeni level'a geçtiniz!!")

        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
            self.is_jumping = False
            self.velocity_y = 0

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.screen_width:
            self.rect.right = self.screen_width

    def check_tile_collision(self, dx, dy, world):
        self.rect.x += dx
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect):
                if dx > 0:  # Sağ
                    self.rect.right = tile[1].left
                if dx < 0:  # Sol
                    self.rect.left = tile[1].right
                if dy > 0:  # Aşağı
                    self.rect.bottom = tile[1].top
                    self.is_jumping = False
                    self.velocity_y = 0
                if dy < 0:  # Yukarı
                    self.rect.top = tile[1].bottom
                    self.velocity_y = 0
        self.rect.x -= dx

    def check_collision_with_enemies(self, enemies):
        for enemy in enemies:
            if pygame.sprite.collide_rect(self, enemy):
                return True
        return False

    def check_collision_with_exit(self, world_data):
        tile_size = 40
        for row in range(len(world_data)):
            for col in range(len(world_data[row])):
                if world_data[row][col] == 7:
                    exit_rect = pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size)
                    if self.rect.colliderect(exit_rect):
                        return True
        return False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (173, 216, 230), self.rect, 2)
