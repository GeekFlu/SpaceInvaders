import pygame  # load pygame keywords
import sys  # let  python use your file system
import os  # help python identify your OS

'''
Variables
'''

world_x = 800
world_y = 600
fps = 40  # frame rate
ani = 4  # animation cycles
main = True

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)

'''
Objects
'''


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.move_x = 0
        self.sprite_name = name
        self.move_y = 0
        self.frame = 0
        self.images = []
        for i in range(0, 4):
            img = pygame.image.load(os.path.join('assets/sprites', name + str(i) + '.png')).convert()
            img.convert_alpha()  # optimise alpha
            # img.set_colorkey(ALPHA)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def control(self, x, y):
        """
        Control movement
        :param x:
        :param y:
        :return:
        """
        self.move_x += x
        self.move_y += y

    def update(self):
        """
        Update position
        :return:
        """
        self.rect.x = self.rect.x + self.move_x
        self.rect.y = self.rect.y + self.move_y

        # moving left
        if self.move_x < 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        # movinf right
        if self.move_x > 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]





'''
Setup
'''

clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([world_x, world_y])
backdrop = pygame.image.load(os.path.join('assets', 'background-800x600.png'))
pygame.display.set_icon(pygame.image.load(os.path.join('assets', '001-ufo.png')))
pygame.display.set_caption("Invasores del Espacio")
backdropbox = world.get_rect()

player = Player("lightning")  # spawn player
player.rect.x = 400  # go to x
player.rect.y = 50  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10

'''
Main Loop
'''

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps, 0)

    world.blit(backdrop, backdropbox)
    player.update()
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)
