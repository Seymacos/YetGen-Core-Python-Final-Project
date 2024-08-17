import pygame
import sys

class Button:
    def __init__(self, x, y, width, height, image):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

class Menu():
    def __init__(self,screen):
        self.screen=screen
        self.screen_height=screen.get_height()
        self.screen_width= screen.get_width()
        self.background = pygame.image.load("mario_background.png")
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
        
        # Load existing images for buttons
        self.sound_on_img = pygame.image.load('soundOn.png')
        self.sound_off_img = pygame.image.load('soundOff.png')
        self.start_img = pygame.image.load('start.png')
        self.exit_img = pygame.image.load('exitGame.png')
        
        # Load new image for save button
        self.save_img = pygame.image.load('save.png')  # Use your new save button image

        # Initialize sounds
        self.start_music = pygame.mixer.Sound('startMusic.wav')
        self.start_music_channel = self.start_music.play(-1)
        self.sound_on = True
        #buttons
        self.start_button = pygame.Rect(500, 200, 280, 70)
        self.exit_button = pygame.Rect(480, 400, 280, 70)
        self.sound_on_button = pygame.Rect(1000, 45, 280, 70)
        self.sound_off_button = pygame.Rect(1100, 50, 280, 70)

    def menu_events(self): # menüdeki hareketlerin toplandığı fonksiyon. 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.collidepoint(event.pos):
                    # Ana oyunu başlatmak için döngüden çıkın
                    return "start"
                if self.exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                if self.sound_on_button.collidepoint(event.pos) and not self.sound_on:
                    self.start_music_channel.unpause()
                    self.sound_on = True
                if self.sound_off_button.is_clicked(event.pos) and self.sound_on:
                    self.start_music_channel.pause()
                    self.sound_on = False
            return None
        
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.start_img, (500, 200))
        self.screen.blit(self.exit_img, (480, 400))
        self.screen.blit(self.sound_on_img, (1000, 45))
        self.screen.blit(self.sound_off_img, (1100, 50))
        self.screen.blit(self.save_img, (100, 200))  # Draw save button




        pygame.draw.rect(self.screen, self.box_color, self.input_box)
        pygame.draw.rect(self.screen, self.color, self.input_box, 2)
        self.screen.blit(self.txt_surface, (self.input_box.x + 10, self.input_box.y + 10))
        self.screen.blit(self.prompt_text, (self.input_box.x, self.input_box.y - 30))
        self.screen.blit(self.save_prompt_text, (self.save_button.rect.x + 10, self.save_button.rect.y + 10))

        if self.saved_message:
            saved_message_surface = self.font.render(self.saved_message, True, (0, 255, 0))
            self.screen.blit(saved_message_surface, (self.screen_width // 2 - saved_message_surface.get_width() // 2, self.screen_height // 2 + 50))
        if self.error_message:
            error_message_surface = self.font.render(self.error_message, True, (255, 0, 0))
            self.screen.blit(error_message_surface, (self.screen_width // 2 - error_message_surface.get_width() // 2, self.screen_height // 2 - 50))

        pygame.display.update()