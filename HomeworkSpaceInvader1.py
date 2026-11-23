import math
import random
import pygame


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader - Add More Sprites")


background = pygame.image.load("background.png")
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")


player_x = 370
player_y = 480
player_x_change = 0
player_y_change = 0
player_speed = 5


num_of_enemies = 7
enemy_x = []
enemy_y = []

for i in range(num_of_enemies):
    enemy_x.append(random.randint(0, SCREEN_WIDTH - 64))
    enemy_y.append(random.randint(50, SCREEN_HEIGHT - 150))


score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)


def show_score(x, y):
    score_text = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score_text, (x, y))


def draw_player(x, y):
    screen.blit(player_img, (x, y))


def draw_enemy(x, y):
    screen.blit(enemy_img, (x, y))



def isCollision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt(
        math.pow(enemyX - playerX, 2) + math.pow(enemyY - playerY, 2)
    )
    if distance < 40:  
        return True
    return False



clock = pygame.time.Clock()
running = True

while running:
    
    screen.blit(background, (0, 0))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -player_speed
            if event.key == pygame.K_RIGHT:
                player_x_change = player_speed
            if event.key == pygame.K_UP:
                player_y_change = -player_speed
            if event.key == pygame.K_DOWN:
                player_y_change = player_speed

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_x_change = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                player_y_change = 0

    
    player_x += player_x_change
    player_y += player_y_change

    player_x = max(0, min(player_x, SCREEN_WIDTH - 64))
    player_y = max(0, min(player_y, SCREEN_HEIGHT - 64))

    
    for i in range(num_of_enemies):
        
        collision = isCollision(enemy_x[i], enemy_y[i], player_x, player_y)
        if collision:
            score_value += 1
            
            enemy_x[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemy_y[i] = random.randint(50, SCREEN_HEIGHT - 150)

        draw_enemy(enemy_x[i], enemy_y[i])

    
    draw_player(player_x, player_y)
    show_score(10, 10)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
