import pygame,sys
from grid import Grid

pygame.init()
dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Pygame Tetris")


clock = pygame.time.Clock()

game_grid = Grid()

#DESCOMENTAR PARA VER AS GRADES SENDO PREENCHIDAS 
#game_grid.grid[0][0]=1
#game_grid.grid[3][5]=4
#game_grid.grid[17][5]=7

game_grid.print_grid()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Desenhando
    screen.fill(dark_blue)
    game_grid.draw(screen)

    pygame.display.update()
    clock.tick(60)

