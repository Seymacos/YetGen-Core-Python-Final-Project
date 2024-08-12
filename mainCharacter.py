import pygame

class Mario:
    def __init__(self, x, y):
        self.image = pygame.image.load('mario.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.jumpSpeed = 10
        self.gravity = 1
        self.isJumping = False
        self.velocity = 0

    def handleJump(self, keys):
        if keys[pygame.K_SPACE]:
            if not self.isJumping:
                self.isJumping = True
                self.velocity = -self.jumpSpeed
            elif self.velocity > -self.jumpSpeed * 2:
                self.velocity -= 1
        else:
            if self.isJumping:
                self.velocity += self.gravity

        self.rect.y += self.velocity

        # Ground collision check
        if self.rect.y >= 300:  # Assuming ground level is at y = 300
            self.rect.y = 300
            self.isJumping = False
            self.velocity = 0

    def update(self, keys):
        self.handleJump(keys)
        self.rect.x += 1  # Slow scroll to the right

        # Ensure Mario stays in the center of the screen
        if self.rect.centerx != 640:  # Assuming screen width is 1280
            self.rect.centerx = 640

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
