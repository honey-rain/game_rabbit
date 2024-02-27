import pygame
import random
import time
import math
import sys

pygame.init()

WHITE = (255, 255, 255)
BROWN = (165, 42, 42)

SCREEN_SIZE = 600
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Моя гра")

background_img = pygame.image.load("background_image1.png")  
background_rect = background_img.get_rect()

screen = pygame.display.set_mode((background_rect.width, background_rect.height))
pygame.display.set_caption("Моя гра")

character_img = pygame.image.load("player_image.png")  
character_rect = character_img.get_rect()

character_x = screen.get_width() // 2 - character_rect.width // 2
character_y = screen.get_height() // 2 - character_rect.height // 2

CHARACTER_SPEED = 5  

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

coin_img = pygame.image.load('coin.png')
coin_rect = coin_img.get_rect()
coin_rect.center = (random.randint(30, background_rect.width - 30), random.randint(30, background_rect.height - 30))

score = 0

coin_speed = 10

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

running = True
start_time = time.time()
level_2_reached = False
level_3_reached = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        character_x -= CHARACTER_SPEED
    if keys[pygame.K_RIGHT]:
        character_x += CHARACTER_SPEED
    if keys[pygame.K_UP]:
        character_y -= CHARACTER_SPEED
    if keys[pygame.K_DOWN]:
        character_y += CHARACTER_SPEED

    character_x = max(0, min(screen.get_width() - character_rect.width, character_x))
    character_y = max(0, min(screen.get_height() - character_rect.height, character_y))

    if character_rect.colliderect(coin_rect):
        score += 1
        coin_rect.center = (random.randint(30, background_rect.width - 30), random.randint(30, background_rect.height - 30))

        if score == 15 and not level_2_reached:
            coin_speed = 5
            level_2_reached = True
            draw_text("Level 2", pygame.font.Font(None, 72), WHITE, screen, background_rect.width // 2, background_rect.height // 2)
            pygame.display.update()
            time.sleep(3)  
        elif score == 25 and not level_3_reached:
            coin_speed = 3
            level_3_reached = True
            draw_text("Level 3", pygame.font.Font(None, 72), WHITE, screen, background_rect.width // 2, background_rect.height // 2)
            pygame.display.update()
            time.sleep(3)  

        if score >= 40:
            draw_text("Finish!", pygame.font.Font(None, 72), WHITE, screen, background_rect.width // 2, background_rect.height // 2)
            pygame.display.update()
            time.sleep(5)  
            pygame.quit()  
            sys.exit()   

    current_time = time.time()
    if current_time - start_time >= coin_speed:
        start_time = time.time()
        coin_rect.center = (random.randint(30, background_rect.width - 30), random.randint(30, background_rect.height - 30))

    character_rect.topleft = (character_x, character_y)

    screen.blit(background_img, (0, 0))
    screen.blit(character_img, character_rect)
    screen.blit(coin_img, coin_rect)

    draw_text(f"Score: {score}", pygame.font.Font(None, 36), WHITE, screen, background_rect.width // 2, 50)

    pygame.display.flip()

pygame.quit()

