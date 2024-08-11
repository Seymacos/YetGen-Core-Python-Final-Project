import pygame 
pygame.init()

scwid= 1280
scheight=720
win= pygame.display.set_mode((scwid,scheight))
pygame.display.set_caption("Pikseller's Game")

# background images 
sun= pygame.image.load("sun.png")
backg= pygame.image.load("sky.png")
backg_new= pygame.transform.scale(backg, (scwid, scheight))


# platform
 

# ekranı bölüyoruz, parçaları yerleştirmeyi kolaylaştırmak için 12*20 (değişebilir)
tile_size= 40 # playerin büyüklüğüne ve hareketlerine göre parkur ve ekran yeniden şekillendirilebilir
scroll_speed=3
background_scroll= 0


def grid_screen():
    for line in range(0,19):
        pygame.draw.line(win,(255,255,255), (0,line* tile_size), (scwid, line* tile_size))
    for line in range(0,33):
        pygame.draw.line(win,(255,255,255), (line*tile_size,0), (line*tile_size, scheight))

class World():
    def __init__(self, data):
        self.tile_list= []

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
                if tile==7:
                    img= pygame.transform.scale(exit_img, (tile_size, tile_size*2))
                    img_rect= img.get_rect()
                    img_rect.x= col_count* tile_size
                    img_rect.y= row_count * tile_size
                    tile= (img, img_rect)
                    self.tile_list.append(tile) 
                col_count+=1
            row_count+=1

    def draw(self):
        #for tile in self.tile_list:
            #win.blit(tile[0], tile[1])
         # Adjust tile positions based on background_scroll
        for tile in self.tile_list:
            win.blit(tile[0], (tile[1].x - background_scroll, tile[1].y))


world_data = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,2,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,2,0,2,2,0],
    [0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0],
    [0,0,0,0,0,2,2,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,2,2,2,2,1,1,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]



world=World(world_data)

run= True 
while run:
    win.blit(backg_new, (0,0))
    

    grid_screen()
    world.draw()
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run= False

# update the scroll position to make it continuous
    background_scroll+= scroll_speed
    if background_scroll>= scwid:
        background_scroll= 0
    pygame.display.update()


