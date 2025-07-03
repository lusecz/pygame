import pygame,sys
from grid import Grid
from tipoblocos import *
from blocos import *
from jogo import Game   

pygame.init()
dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Pygame Tetris")


clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200 )  # Atualiza o jogo a cada 200ms


#DESCOMENTAR PARA VER AS GRADES SENDO PREENCHIDAS 
#game_grid.grid[0][0]=1
#game_grid.grid[3][5]=4
#game_grid.grid[17][5]=7

#game_grid.print_grid()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type ==   pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            if event.key == pygame.K_UP:
                game.current_block.rotation_state = (game.current_block.rotation_state + 1) % 4
        if event.type == GAME_UPDATE:
            game.move_down()
            
                
        #Desenhando
    screen.fill(dark_blue)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)

