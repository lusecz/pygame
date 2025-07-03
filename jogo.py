from grid import Grid
from blocos import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBLock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.currenc_block = self.get_rangom_block()
        self.next_block = self.get_random_block()

    def get_random_block(self):
        if len(self.blocks) == 0
            self.blocks = [IBlock(), JBlock(), LBLock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)