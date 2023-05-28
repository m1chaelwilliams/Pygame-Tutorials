import pygame
import sys
from events import EventHandler
from ui import UI, Menu

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        UI.init(self)
        self.clock = pygame.time.Clock()
        EventHandler()


        self.menu = Menu(self)
    def run(self):
        self.running = True
        while self.running:
            EventHandler.run()
            for e in EventHandler.events:
                if e.type == pygame.QUIT:
                    self.running = False

            self.menu.run()

            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()