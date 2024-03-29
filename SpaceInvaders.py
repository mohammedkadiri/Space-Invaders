
import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


class Ship(pygame.sprite.Sprite):
    """ This class represents a simple ship class. """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Sprites/ship.png").convert()
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 30)
        self.image.set_colorkey(BLACK)
        self.dx = 0

    def update(self):
        self.dx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_d]:
            self.dx = -3
        if keystate[pygame.K_a]:
            self.dx = 3
        self.rect.x += self.dx

        # Constraints
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

class Enemy(pygame.sprite.Sprite):
    """ This class represents a simple enemy class. """

    def __init__(self):
        super().__init__()
        self.invadersList = []
        self.image = pygame.image.load("Sprites/enemies.png").convert()
        self.rect = self.image.get_rect()
        #self.rect.center = (200, 150)
        self.image.set_colorkey(BLACK)

    # def setUpInvaders(self):
    #    y = 50
    #    num_rows = 2
    #    num_invaders_per_row = 5
    #
    #    # while y <= 50 * num_rows:
    #    #      x = 50
    #    #      while x <= 50 * num_invaders_per_row:
    #    #          self.invadersList.append(pygame.Rect(x, y, 50, 50))
    #    #          x = x + 50
    #    #      y += 50
    #    # return self.invadersList






class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet. """
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([2, 8])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3

class Game(object):
    """This class represents an instance of the game. If we need to
    reset the game we'd just need to create a new instance of this
    class. """

    def __init__(self, screen, ship, enemy):
        self.screen = screen
        self.ship = ship
        self.enemy = enemy
        self.game_over = False
        self.background_image = pygame.image.load("Sprites/space.png").convert()
        # Create a list to add all sprites
        self.all_sprites = pygame.sprite.Group()


        # Create a list to add only the spaceship sprite
        self.ship_sprite = pygame.sprite.GroupSingle()
        self.bullet_list = pygame.sprite.Group()
        self.all_sprites.add(self.enemy)
        self.ship_sprite.add(self.ship)


    def process_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Fire a bullet if the user clicks
                bullet = Bullet()
                bullet.rect.x = self.ship.rect.x + 22
                bullet.rect.y = self.ship.rect.y
                self.all_sprites.add(bullet)
                self.bullet_list.add(bullet)
                if self.game_over:
                    self.__init__()
        return False


    def run_logic(self):
        if not self.game_over:
            self.ship_sprite.update()
            self.all_sprites.update()

    def display_frame(self):
        self.screen.blit(self.background_image, [0, 0])
        self.ship_sprite.draw(self.screen)
        self.all_sprites.draw(self.screen)
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
    enemy = Enemy(screen)


    game = Game(screen, ship, enemy)

    while not done:

        done = game.process_events()

        game.run_logic()

        game.display_frame()

        clock.tick(fps)

    pygame.quit()

if __name__ == '__main__':
    main()