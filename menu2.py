import pygame
import sys

# Pygame başlat
pygame.init()

class Menu():
    def __init__(self,screen_height,screen_width):
        self.screen_height=screen_height
        self.screen_widht= screen_width
        self.background = pygame.image.load("mario_background.png")
        self.background = pygame.transform.scale(self.background, (screen_width, screen_height))
        self.sound_on_img= pygame.image.load('soundOn.png')
        self.sound_off_img= pygame.image.load('soundOff.png')
        self.start_img= pygame.image.load('start.png')
        self.exit_img = pygame.image.load('exitGame.png')
        self.start_music = pygame.mixer.Sound('startMusic.wav')
# muzik
    def start_music():
        start_music_channel = start_music.play(-1)  # Sonsuz döngüde çalması için -1 kullanılır
        sound_on = True
# Ekran boyutlarını belirle
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Başlık ve ikon
pygame.display.set_caption("Giriş Ekranı")

# Arka plan, ses, ve tuş görsellerini yükle
background = pygame.image.load('mario_background.png')
backGround=pygame.transform.scale(background,(screen_width,screen_height))
sound_on_img = pygame.image.load('soundOn.png')
sound_off_img = pygame.image.load('soundOff.png')
start_img = pygame.image.load('start.png')
exit_img = pygame.image.load('exitGame.png')
start_music = pygame.mixer.Sound('startMusic.wav')

# Başlangıçta müzik çalsın


# Tuşları oluştur
start_button = pygame.Rect(500, 200, 280, 70)
exit_button = pygame.Rect(480, 400, 280, 70)
sound_on_button = pygame.Rect(1000, 45, 280, 70)
sound_off_button = pygame.Rect(1100, 50, 280, 70)

# Ana döngü
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                # main dosyayı çalıştır (örnek olarak, main.py)
                import main
            if exit_button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
            if sound_on_button.collidepoint(event.pos) and not sound_on:
                start_music_channel.unpause()  # Müziği devam ettir
                sound_on = True
            if sound_off_button.collidepoint(event.pos) and sound_on:
                start_music_channel.pause()  # Müziği durdur
                sound_on = False

    # Arka planı çiz
    screen.blit(backGround, (0, 0))

    # Tuşları çiz
    screen.blit(start_img, (500, 200))
    screen.blit(exit_img, (480, 400))
    screen.blit(sound_on_img, (1000, 45))
    screen.blit(sound_off_img, (1100, 50))
    pygame.display.update()

