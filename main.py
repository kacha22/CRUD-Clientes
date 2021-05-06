import pygame
import random
import time
from pygame.locals import *

size = 40
background_color = (110,110,5)

class Virus:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.virus = pygame.image.load("Virus.png")
        self.virus = pygame.transform.scale(self.virus, (50,50))
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.virus, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 24) * size
        self.y = random.randint(1, 19) * size

class Snake:
    def __init__(self, parent_screen):
        self.snake = pygame.image.load("Cabeça.png")
        self.parent_screen = parent_screen
        self.direction = 'left'

        self.length = 1
        self.x = [500]
        self.y = [500]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'up':
            self.y[0] -= size
        if self.direction == 'down':
            self.y[0] += size
        if self.direction == 'left':
            self.x[0] -= size
        if self.direction == 'right':
            self.x[0] += size

        self.draw()

    def draw(self):
        self.parent_screen.fill(background_color)

        for i in range(self.length):
            self.parent_screen.blit(self.snake, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Kill the Covid")

        pygame.mixer.init()

        self.surface = pygame.display.set_mode((1280,720))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.virus = Virus(self.surface)
        self.virus.draw()

    def reset(self):
        self.snake = Snake(self.surface)
        self.virus = Virus(self.surface)

    def collision(self, x1, y1, x2 ,y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True
        return False

    def play(self):
        self.snake.walk()
        self.virus.draw()
        self.display_score()
        pygame.display.flip()

        if self.collision(self.snake.x[0], self.snake.y[0], self.virus.x, self.virus.y):
            som = pygame.mixer.Sound("Mordida.mp3")
            pygame.mixer.Sound.play(som)
            self.snake.increase_length()
            self.virus.move()

        for i in range(3, self.snake.length):
            if self.collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Collision Ocurred"

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(score, (1170, 20))

    def show_game_over(self):
        self.surface.fill(background_color)
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! You score is {self.snake.length}", True, (0,0,0))
        self.surface.blit(line1, (500,300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (200,200,200))
        self.surface.blit(line2, (400, 600))
        pygame.display.flip()

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:
                            self.snake.move_right()

                elif event.type == pygame.QUIT:
                    running = False
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.25)
if __name__ == "__main__":
    game = Game()
    game.run()
