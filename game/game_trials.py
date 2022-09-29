import pygame 

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#GREEN_ON = (0, 255, 0)

def game_over():
    #pygame.quit()
    #quit()
# Game Loop

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.display.quit()
                pygame.quit()
                quit()

if __name__ == 'game_over':
    game_over()