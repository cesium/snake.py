import pygame, random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake Game')

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10)

def game_loop():
    game_end = False

    snake_direction = LEFT
    snake = [(200, 200), (210, 200), (220, 200)]
    snake_skin = pygame.Surface((10,10))
    snake_skin.fill((255,255,255))
    snake_head = snake[0]

    apple_pos = on_grid_random()
    apple = pygame.Surface((10,10))
    apple.fill((255,0,0))

    clock = pygame.time.Clock()
    while not game_end:
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == QUIT:
                game_end = True

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    snake_direction = UP
                if event.key == K_DOWN:
                    snake_direction = DOWN
                if event.key == K_LEFT:
                    snake_direction = LEFT
                if event.key == K_RIGHT:
                    snake_direction = RIGHT

        # movimento da cobra
        for i in range(len(snake)-1, 0, -1):
            snake[i] = (snake[i-1][0], snake[i-1][1])

        # mudança de direção da cobra
        if snake_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        elif snake_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        elif snake_direction == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])
        elif snake_direction == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        snake_head = snake[0]

        # colisão com a maçã
        if snake_head[0] == apple_pos[0] and snake_head[1] == apple_pos[1]:
            apple_pos = on_grid_random()
            snake.append(snake[1])


        # condição para determinar se a cobra bateu em si própria
        for i in range(1, len(snake)):
            if snake_head[0] == snake[i][0] and snake_head[1] == snake[i][1]:
                game_end = True
                break

        # condição para determinar se a cobra bateu na parede
        if snake_head[0] < 0 or snake_head[0] > 590 and snake_head[1] < 0 or snake_head[1] > 590:
            game_end = True


        # desenho da maça
        screen.fill((0,0,0))
        screen.blit(apple, apple_pos)

        # desenho da cobra
        for pos in snake:
            screen.blit(snake_skin, pos)

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    game_loop()
