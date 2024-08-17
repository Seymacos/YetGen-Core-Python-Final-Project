import pygame
import sys

class Menu:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.menu_items = ["Start", "Options", "Quit"]
        self.selected_item = 0
        self.font_path = "SuperMario256.ttf"
        self.font = pygame.font.Font(self.font_path, 74)
        self.small_font = pygame.font.Font(self.font_path, 50)
        self.background = pygame.image.load("mario_background.png")
        self.background = pygame.transform.scale(self.background, (screen_width, screen_height))
        
    def draw_menu(self, screen):
        screen.fill((135, 206, 235))
        screen.blit(self.background, (0, 0))
        for i, item in enumerate(self.menu_items):
            if i == self.selected_item:
                label = self.font.render(item, True, (0, 0, 0))
            else:
                label = self.small_font.render(item, True, (0, 0, 0))
            
            label_rect = label.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + i * 100))
            screen.blit(label, label_rect)
        
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selected_item = (self.selected_item + 1) % len(self.menu_items)
                elif event.key == pygame.K_UP:
                    self.selected_item = (self.selected_item - 1) % len(self.menu_items)
                elif event.key == pygame.K_RETURN:
                    if self.menu_items[self.selected_item] == "Start":
                        return "start"
                    elif self.menu_items[self.selected_item] == "Options":
                        return "options"
                    elif self.menu_items[self.selected_item] == "Quit":
                        pygame.quit()
                        sys.exit()
        return "menu"

