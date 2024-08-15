import pygame 
from enemies import Snake1, Snake2, badMushrooms, goodMushrooms, Bird
pygame.init()

tile_size= 40 # mainde grid_screen func çağırılacak

#Geid bir düzen oluşturur.
def grid_screen(screen,SCREEN_WIDTH,SCREEN_HEIGHT):
    for line in range(0,19):
        pygame.draw.line(screen,(255,255,255), (0,line* tile_size), (SCREEN_WIDTH, line* tile_size))
    for line in range(0,33):
        pygame.draw.line(screen,(255,255,255), (line*tile_size,0), (line*tile_size, SCREEN_HEIGHT))

#World sınıfı
class World():
    def __init__(self, data):
        self.tile_list= []
        self.bad_mushrooms_list = pygame.sprite.Group()

        #Kullanılan resimlerin yüklenmesi.
        dirt_img= pygame.image.load("dirt.png")
        grass_img= pygame.image.load("grass.png")
        exit_img=pygame.image.load("exit.png")

        row_count=0
        for row in data:
            col_count=0
            for tile in row:
                if tile==1:
                    img= pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect= img.get_rect()
                    img_rect.x= col_count* tile_size
                    img_rect.y= row_count * tile_size
                    tile= (img, img_rect)
                    self.tile_list.append(tile) 
                if tile==2:
                    img= pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect= img.get_rect()
                    img_rect.x= col_count* tile_size
                    img_rect.y= row_count * tile_size
                    tile= (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    bad_mushroom = badMushrooms(col_count * tile_size, row_count * tile_size, "BadMushrooms.png", tile_size, tile_size)
                    self.bad_mushrooms_list.add(bad_mushroom)
                   #Exit fayansı
                if tile==7:
                    img= pygame.transform.scale(exit_img, (tile_size, tile_size*2))
                    img_rect= img.get_rect()
                    img_rect.x= col_count* tile_size
                    img_rect.y= row_count * tile_size
                    tile= (img, img_rect)
                    self.tile_list.append(tile) 
                col_count+=1
            row_count+=1

    #Faynasları çizilmesini sağlar.
    def draw(self, screen, background_scroll):
 
        for tile in self.tile_list:
            screen.blit(tile[0], (tile[1].x - background_scroll, tile[1].y))
        self.bad_mushrooms_list.draw(screen)
   #Çarpışmaları kontrol eder.
    def check_collision(self, rect):
        for tile in self.tile_list:
            if tile[1].colliderect(rect):
                return tile[1]
        return None




