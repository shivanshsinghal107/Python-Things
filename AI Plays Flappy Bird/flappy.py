import pygame
import neat
import time
import random
import os
pygame.font.init()

WIN_WIDTH = 500
WIN_HEIGHT = 800

GEN = 0
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
             pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
             pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))]

PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))

SCORE_FONT = pygame.font.SysFont('comicsans', 50)
pygame.display.set_caption("Flappy Bird")

class Bird:
    IMGS = BIRD_IMGS
    # rotation of the bird (in degrees)
    MAX_ROTATION = 25
    # rotation of the bird in each frame (in degrees)
    ROT_VEL = 20
    # how long does each bird animation appears
    # i.e. how fast the bird flaps
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        # for doing the physics for the bird movements
        # basically this measures time
        self.tick_count = 0
        # velocity
        self.vel = 0
        self.height = self.y
        # to keep track which image are we
        # showing currently for the birds
        self.img_count = 0
        # which image to show
        self.img = self.IMGS[0]

    def jump(self):
        # velocity is negative because the system of moving
        # upwards and downwards is opposite for pygame i.e.
        # for moving upwards you have to give negative velocity
        self.vel = -10.5
        # keep track of when we last jumped, it is set to 0 because
        # we need to know when we are changing directions or changing velocities
        # for the physics formulas to work
        self.tick_count = 0
        # keep track of where the bird jump from
        self.height = self.y

    # function to move every single frame of the bird
    def move(self):
        # a frame has passed, basically keeping track of time
        self.tick_count += 1
        # s = ut + 0.5*at^2
        # how many pixels the bird is moving up or down this frame
        d = self.vel * self.tick_count + 1.5 * (self.tick_count ** 2)

        # this condition is so that we do not keep moving down
        # after 16 pixels there will be no acceleration
        # i.e. we reach a point where we don't accelerate anymore
        if d >= 16:
            d = 16

        # if we're moving upwards, move upwards a little bit more
        if d < 0:
            d -= 2

        self.y = self.y + d

        # how much to tilt when we go upwards
        if d < 0 or self.y < self.height + 50:
            # make sure we do not tilt the bird completely backwards
            # or some crazy direction
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        # how much to tilt when we go downwards
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        # how many times the main game loop run
        # or how many times have we already shown one image
        self.img_count += 1

        # what image should be shown based on the current image count
        # basically these whole if else statements are process of making the bird flap
        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        # when the bird is going downwards then just display the image
        # in which the wings are levelled, and make the flapping stop
        # because a falling bird flapping doesn't make any sense
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2

        # rotate an image around its center in pygame
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    # function to run on any collision
    def get_mask(self):
        return pygame.mask.from_surface(self.img)

class Pipe:
    GAP = 200
    VEL = 5

    def __init__(self, x):
        self.x = x
        self.height = 0

        self.top = 0
        self.bottom = 0
        # for the top pipe, image has to be rotated 180 degrees i.e. flip the image
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM = PIPE_IMG

        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        # offset is how far these masks are from each other
        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        # check if these masks have a collision point
        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        if b_point or t_point:
            return True

        return False

class Base:
    VEL = 5
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __init__(self, y):
        self.y = y
        # position of first image
        self.x1 = 0
        # position of second image
        self.x2 = self.WIDTH

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))


def draw_window(win, birds, pipes, base, score, gen):
    win.blit(BG_IMG, (0, 0))

    for pipe in pipes:
        pipe.draw(win)

    text = SCORE_FONT.render(f"Score: {score}", 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    text = SCORE_FONT.render(f"Gen: {gen}", 1, (255, 255, 255))
    win.blit(text, (10, 10))

    base.draw(win)
    for bird in birds:
        bird.draw(win)

    pygame.display.update()

def main(genomes, config):
    global WIN, GEN
    GEN += 1
    win = WIN
    nets = []
    ge = []
    birds = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(230, 350))
        g.fitness = 0
        ge.append(g)

    base = Base(730)
    pipes = [Pipe(700)]
    clock = pygame.time.Clock()

    score = 0

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        pipe_index = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_index = 1
        else:
            run = False
            break

        for i, bird in enumerate(birds):
            bird.move()
            ge[i].fitness += 0.1

            output = nets[i].activate((bird.y, abs(bird.y - pipes[pipe_index].height), abs(bird.y - pipes[pipe_index].bottom)))

            if output[0] > 0.5:
                bird.jump()

        rem = []
        add_pipe = False
        for pipe in pipes:
            for i, bird in enumerate(birds):
                if pipe.collide(bird):
                    #ge[i].fitness -= 1
                    birds.pop(i)
                    nets.pop(i)
                    ge.pop(i)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            pipe.move()

        if add_pipe:
            score += 1
            for g in ge:
                g.fitness += 5
            pipes.append(Pipe(600))

        for r in rem:
            pipes.remove(r)

        for i, bird in enumerate(birds):
            if bird.y + bird.img.get_height() >= 730 or bird.y < 0:
                birds.pop(i)
                nets.pop(i)
                ge.pop(i)

        base.move()
        draw_window(win, birds, pipes, base, score, GEN)

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main, 50)

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)
