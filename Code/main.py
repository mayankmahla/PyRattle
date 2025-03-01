import pygame
import random

pygame.init()

# Colors
WHITE, YELLOW, BLACK, RED, GREEN, BLUE = (255,255,255), (255,255,102), (0,0,0), (213,50,80), (0,255,0), (50,153,213)

# Screen settings
dis_width, dis_height = 800, 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# Game settings
snake_block, snake_speed = 10, 15
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def display_score(score):
    dis.blit(score_font.render(f"Score: {score}", True, WHITE), (0, 0))

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(dis, WHITE, [x, y, snake_block, snake_block])

def display_message(msg, color):
    dis.blit(font_style.render(msg, True, color), (dis_width / 6, dis_height / 3))

def game_loop():
    x, y = dis_width // 2, dis_height // 2
    dx, dy = 0, 0
    snake_list, snake_length = [], 1
    
    foodx, foody = [random.randrange(0, dis_width - snake_block, 10) for _ in range(2)]
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    dx, dy = (-snake_block, 0) if event.key == pygame.K_LEFT else (snake_block, 0)
                elif event.key in (pygame.K_UP, pygame.K_DOWN):
                    dx, dy = (0, -snake_block) if event.key == pygame.K_UP else (0, snake_block)
        
        x, y = x + dx, y + dy
        if x < 0 or x >= dis_width or y < 0 or y >= dis_height or [x, y] in snake_list[:-1]:
            dis.fill(BLACK)
            display_message("Game Over! Press R to Restart or Esc to Quit", RED)
            display_score(snake_length - 1)
            pygame.display.update()
            
            while True:
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    elif event.key == pygame.K_r:
                        game_loop()
                        return
        
        dis.fill(BLACK)
        pygame.draw.rect(dis, BLUE, [foodx, foody, snake_block, snake_block])
        
        snake_list.append([x, y])
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        draw_snake(snake_list)
        display_score(snake_length - 1)
        pygame.display.update()
        
        if [x, y] == [foodx, foody]:
            foodx, foody = [random.randrange(0, dis_width - snake_block, 10) for _ in range(2)]
            snake_length += 1
        
        clock.tick(snake_speed)
    
    pygame.quit()

game_loop()
