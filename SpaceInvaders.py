
import pygame

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Ship(pygame.sprite.Sprite):
    """ This class represents a simple ship class. """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Sprites/spaceship.png").convert()
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 30)

class Game(object):
    """This class represents an instance of the game. If we need to
    reset the game we'd just need to create a new instance of this
    class. """

    def __init__(self, screen, ship):
        self.screen = screen
        self.ship = ship
        self.game_over = False

        # Create a list to add only the spaceship sprite
        self.ship_sprite = pygame.sprite.GroupSingle()

        self.ship_sprite.add(self.ship)

    def process_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
        return False


    def run_logic(self):
        if not self.game_over:
            pass

    def display_frame(self):
        self.screen.fill(BLACK)
        self.ship_sprite.draw(self.screen)
        pygame.display.flip()


def main():

    # Intialize pygame and music
    pygame.init()
    pygame.mixer.init()

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Space Invaders")
    pygame.mouse.set_visible(False)

    done = False
    clock = pygame.time.Clock()
    fps = 120

    ship = Ship()

    game = Game(screen, ship)

    while not done:

        done = game.process_events()

        game.run_logic()

        game.display_frame()

        clock.tick(fps)

    pygame.quit()

if __name__ == '__main__':
    main()