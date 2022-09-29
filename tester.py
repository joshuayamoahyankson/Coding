import pygame 
pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GREEN_ON = (0, 255, 0)

def game_over():
    #pygame.quit()
    #quit()
# Game Loop

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()

if __name__ == '__main__':
    game_over()