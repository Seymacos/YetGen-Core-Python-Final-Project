import pygame
import sys

# Pygame'i başlat
pygame.init()

# Ekran boyutları
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mario Game - Main Menu")

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 235)

# Yazı tipi ayarları
font_path = r"C:\Users\Bartu Vatansever\Desktop\oyunum\SuperMario256.ttf"
font = pygame.font.Font(font_path, 74)
small_font = pygame.font.Font(font_path, 50)

# Menü seçenekleri
menu_items = ["Start", "Options", "Quit"]
selected_item = 0

# Arka plan resmi
background_path = r"C:\Users\Bartu Vatansever\Desktop\oyunum\mario_background.png"
background = pygame.image.load(background_path)
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_menu():
    screen.fill(SKY_BLUE)
    screen.blit(background, (0, 0))
    for i, item in enumerate(menu_items):
        if i == selected_item:
            label = font.render(item, True, BLACK)
        else:
            label = small_font.render(item, True, BLACK)
        
        label_rect = label.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + i * 100))
        screen.blit(label, label_rect)

    pygame.display.flip()

def main():
    global selected_item
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_item = (selected_item + 1) % len(menu_items)
                elif event.key == pygame.K_UP:
                    selected_item = (selected_item - 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    if menu_items[selected_item] == "Start":
                        print("Starting game...")
                    elif menu_items[selected_item] == "Options":
                        print("Opening options...")
                    elif menu_items[selected_item] == "Quit":
                        pygame.quit()
                        sys.exit()

        draw_menu()

if __name__ == "__main__":
    main()
