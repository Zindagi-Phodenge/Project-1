import pygame
import random

pygame.init() # initialization of pygame

# Define colors
BLACK = (0, 0, 0) # the numbers represent the intensity of rgb on a scale of 0 to 255.
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up display
screen_width = 640
screen_height = 480
block_size = 20
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Snake class
class Snake:
    def __init__(self): # init function is the constructor
        self.positions = [(screen_width // 2, screen_height // 2)]
        self.direction = (0, -1)
        self.grow = False

    def update(self):
        cur_x, cur_y = self.positions[0]
        new_x = (cur_x + self.direction[0] * block_size) % screen_width
        new_y = (cur_y + self.direction[1] * block_size) % screen_height

        if self.grow:
            self.positions.insert(0, (new_x, new_y))
            self.grow = False
        else:
            self.positions = [(new_x, new_y)] + self.positions[:-1]

    def change_direction(self, new_direction):
        if (new_direction[0], new_direction[1]) != (-self.direction[0], -self.direction[1]):
            self.direction = new_direction

    def check_collision(self):
        return self.positions[0] in self.positions[1:]

    def render(self):
        for segment in self.positions:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], block_size, block_size))

# Food class
class Food:
    def __init__(self):
        self.position = (random.randint(0, screen_width // block_size - 1) * block_size,
                         random.randint(0, screen_height // block_size - 1) * block_size)

    def update(self):
        self.position = (random.randint(0, screen_width // block_size - 1) * block_size,
                         random.randint(0, screen_height // block_size - 1) * block_size)

    def render(self):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], block_size, block_size))

# Main game loop
def main():
    snake = Snake()
    food = Food()

    clock = pygame.time.Clock()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))

        snake.update()
        if snake.check_collision():
            game_over = True

        if snake.positions[0] == food.position:
            snake.grow = True
            food.update()

        screen.fill(BLACK)
        snake.render()
        food.render()8
        pygame.display.update()

        clock.tick(10) # this is the fps limiter, the fps is limited to 10 frames per second.

    pygame.quit()

if __name__ == "__main__":
    main()
