import pygame

# Initialize Pygame
pygame.init()

# Set up display (1280x720)
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Super Mario Clone")

# Set up the clock for FPS
clock = pygame.time.Clock()

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()  # Load player image with transparency
        self.rect = self.image.get_rect()
        self.rect.center = (100, 620)  # Starting position (x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.jump_strength = -15
        self.gravity = 0.8
        self.on_ground = False

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def jump(self):
        if self.on_ground:
            self.velocity.y = self.jump_strength
            self.on_ground = False

    def update(self):
        self.velocity.y += self.gravity  # Apply gravity
        self.rect.y += self.velocity.y  # Apply vertical movement

        if self.rect.bottom >= 720:  # Check for ground collision
            self.rect.bottom = 720
            self.on_ground = True
            self.velocity.y = 0

# Initialize player with Mario PNG image
player = Player("mario.png")
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-player.speed, 0)
    if keys[pygame.K_RIGHT]:
        player.move(player.speed, 0)
    if keys[pygame.K_UP]:  # Use up arrow key for jumping
        player.jump()

    all_sprites.update()

    screen.fill((135, 206, 250))  # Sky blue background
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
