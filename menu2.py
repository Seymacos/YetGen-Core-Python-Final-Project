import pygame
import sys

# Pygame başlat
pygame.init()

# Menü sınıfı:
class Menu():
    def __init__(self,screen):
        self.screen=screen
        self.screen_height=screen.get_height()
        self.screen_width= screen.get_width()
        self.background = pygame.image.load("mario_background.png")
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
        self.sound_on_img= pygame.image.load('soundOn.png')
        self.sound_off_img= pygame.image.load('soundOff.png')
        self.start_img= pygame.image.load('start.png')
        self.exit_img = pygame.image.load('exitGame.png')
        self.start_music = pygame.mixer.Sound('startMusic.wav')
        self.start_music_channel = self.start_music.play(-1)  # Sonsuz döngüde çalması için -1 kullanılır
        self.sound_on = True
        #butonlar
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
                    return "start" # main dosyasında "start" çalştığında menü döngüsü biter,oyun başlar
                if self.exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                # arkaplan müziğini kapatıp açar
                if self.sound_on_button.collidepoint(event.pos) and not self.sound_on:
                    self.start_music_channel.unpause()
                    self.sound_on = True
                if self.sound_off_button.collidepoint(event.pos) and self.sound_on:
                    self.start_music_channel.pause()
                    self.sound_on = False
            return None
        
    def draw(self): # menüyü ekrana çizer
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.start_img, (500, 200))
        self.screen.blit(self.exit_img, (480, 400))
        self.screen.blit(self.sound_on_img, (1000, 45))
        self.screen.blit(self.sound_off_img, (1100, 50))
        pygame.display.update()

