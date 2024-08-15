import pygame
pygame.init()

SCREEN_WIDTH= 1280
SCREEN_HEIGHT= 720
win= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

tile_size= 40 

# background images 
sun= pygame.image.load("sun.png")
backg= pygame.image.load("sky.png")
exit= pygame.image.load("exit.png")
exit_n= pygame.transform.scale(exit,(tile_size*2 ,tile_size))
background_new=pygame.transform.scale(backg, (SCREEN_WIDTH, SCREEN_HEIGHT))


# platform


# ekranı bölüyoruz, parçaları yerleştirmeyi kolaylaştırmak için 12*20 (değişebilir)
 # playerin büyüklüğüne ve hareketlerine göre parkur ve ekran yeniden şekillendirilebilir
def grid_screen(screen):
    for line in range(0,19):
        pygame.draw.line(screen, (255,255,255), (0, line * tile_size), (SCREEN_WIDTH, line * tile_size))
    for line in range(0,33):
        pygame.draw.line(screen, (255,255,255), (line * tile_size, 0), (line * tile_size, SCREEN_HEIGHT))

class World():
    def __init__(self, data):
        self.tile_list= []

        dirt_img= pygame.image.load("dirt.png")
        grass_img= pygame.image.load("grass.png")
        exit= pygame.image.load("exit.png")
        exit_n= pygame.transform.scale(exit,(tile_size*2 ,tile_size))

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
        
                if tile==7:
                    img= pygame.transform.scale(exit_n, (tile_size, tile_size*2))
                    img_rect= img.get_rect()
                    img_rect.x= col_count* tile_size
                    img_rect.y= row_count * tile_size
                    tile= (img, img_rect)
                    self.tile_list.append(tile) 
                col_count+=1
            row_count+=1

    def draw(self,screen):
        for tile in self.tile_list:
            win.blit(tile[0], tile[1])


