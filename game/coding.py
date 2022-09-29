import pygame 
from sys import exit
pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # This is the main surface(display surface) it serves as the game window, anything displayed goes on here!
pygame.display.set_caption("My First Game")
clock = pygame.time.Clock()
White = (255,255,255)
some_surface = pygame.Surface((100, 250))
some_surface.fill('blue')
#test_font = pygame.font.Font('font/pixeltype.ttf', 80)

#image_loading = pygame.image.load("folder\imagename") # This is how to load an image in pygame!
#test_font_surface = test_font.render(test_font , False , "gray" )
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if run == False:
            pygame.quit()
            exit()
            
    SCREEN.blit(some_surface, (55,300)) # blit means block image transfer! the blit command takes in two argument(surface and position) A regular surface only gets displayed when connected / placed on the displayed surface!
   #SCREEN.blit(image_loading)
    #SCREEN.blit(test_font_surface, 300, 50)
    pygame.display.update()
    clock.tick(60)
    
    
    
    
    
#There are two surfaces is pygame namely the display surface and a regular surface!
#if __name__ == '__game_over__':
    #game_over()