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

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.screen_height = screen.get_height()
        self.screen_width = screen.get_width()
        self.background = pygame.image.load("mario_background.png")
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
        
        # Load existing images for buttons
        self.sound_on_img = pygame.image.load('soundOn.png')
        self.sound_off_img = pygame.image.load('soundOff.png')
        self.start_img = pygame.image.load('start.png')
        self.exit_img = pygame.image.load('exitGame.png')
        
        # Load new image for save button
        self.save_img = pygame.image.load('saveButton.png')  # Use your new save button image

        # Initialize sounds
        self.start_music = pygame.mixer.Sound('startMusic.wav')
        self.start_music_channel = self.start_music.play(-1)
        self.sound_on = True

        # Initialize buttons with images
        self.start_button = Button(500, 200, 280, 70, 'start.png')
        self.exit_button = Button(480, 400, 280, 70, 'exitGame.png')
        self.sound_on_button = Button(1000, 45, 280, 70, 'soundOn.png')
        self.sound_off_button = Button(1100, 50, 280, 70, 'soundOff.png')
        self.save_button = Button(100, 200, 280, 70, 'save.png')  # Use new save button image

        # Input box setup
        self.input_box = pygame.Rect(100, 100, 300, 50)
        self.color_inactive = pygame.Color("blue")
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.active = False
        self.text = ''
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.box_color = pygame.Color(255, 219, 88)
        self.prompt_text = self.font.render("", True, (255,255, 255))
        self.prompt_text = self.font.render("Enter your username", True, (255, 255, 255))
        self.saved_message = None
        self.error_message = None

    def menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.is_clicked(event.pos):
                    if not self.text:
                        self.error_message = "Enter your username!"
                        self.saved_message = None
                    else:
                        self.error_message = None
                        self.saved_message = None
                        return "start"
                if self.exit_button.is_clicked(event.pos):
                    pygame.quit()
                    sys.exit()
                if self.sound_on_button.is_clicked(event.pos) and not self.sound_on:
                    self.start_music_channel.unpause()
                    self.sound_on = True
                if self.sound_off_button.is_clicked(event.pos) and self.sound_on:
                    self.start_music_channel.pause()
                    self.sound_on = False
                if self.save_button.is_clicked(event.pos) and self.text:
                    try:
                        with open("username.txt", "w") as f:
                            f.write(self.text)
                        self.saved_message = "Username saved!"
                        self.error_message = None
                    except IOError as e:
                        self.saved_message = f"Kullanıcı adı kaydedilemedi: {e}"
                elif self.save_button.is_clicked(event.pos):
                    self.error_message = "Enter your username!"
                    self.saved_message = None
                if self.input_box.collidepoint(event.pos):
                    self.active = not self.active
                    self.error_message = None  # Clear error message when focusing on the input box
                else:
                    self.active = False
                self.color = self.color_active if self.active else self.color_inactive
            
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        if not self.text:
                            self.error_message = "Enter your username!"
                        else:
                            self.error_message = None
                            self.text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
                    self.txt_surface = self.font.render(self.text, True, self.color)
        
        return None

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.start_img, (500, 200))
        self.screen.blit(self.exit_img, (480, 400))
        self.screen.blit(self.sound_on_img, (1000, 45))
        self.screen.blit(self.sound_off_img, (1100, 50))
        self.screen.blit(self.save_img, (100, 200))  # Draw save button

        # Draw title in the middle of the screen
        title_font = pygame.font.Font(None, 100)  # Larger font for the title
        title_text = title_font.render('PIKSELS', True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(self.screen_width // 2, 100))  # Adjust vertical position if needed
        self.screen.blit(title_text, title_rect)


        pygame.draw.rect(self.screen, self.box_color, self.input_box)
        pygame.draw.rect(self.screen, self.color, self.input_box, 2)
        self.screen.blit(self.txt_surface, (self.input_box.x + 10, self.input_box.y + 10))
        self.screen.blit(self.prompt_text, (self.input_box.x, self.input_box.y - 30))

        if self.saved_message:
            saved_message_surface = self.font.render(self.saved_message, True, (0, 255, 0))
            self.screen.blit(saved_message_surface, (self.screen_width // 2 - saved_message_surface.get_width() // 2, self.screen_height // 2 + 50))
        if self.error_message:
            error_message_surface = self.font.render(self.error_message, True, (255, 0, 0))
            self.screen.blit(error_message_surface, (self.screen_width // 2 - error_message_surface.get_width() // 2, self.screen_height // 2 - 50))

        pygame.display.update()