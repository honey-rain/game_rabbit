import pygame
import random
import time
import math
import sys

# Ініціалізація Pygame
pygame.init()

# Кольори
WHITE = (255, 255, 255)
BROWN = (165, 42, 42)

# Ініціалізація вікна гри
SCREEN_SIZE = 600  # Розмір квадратного вікна
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Моя гра")

# Завантаження фонового зображення
background_img = pygame.image.load("background_image1.png")  
background_rect = background_img.get_rect()

# Ініціалізація вікна гри з розмірами фото на фоні
screen = pygame.display.set_mode((background_rect.width, background_rect.height))
pygame.display.set_caption("Моя гра")

# Завантаження зображення персонажа
character_img = pygame.image.load("player_image.png")  
character_rect = character_img.get_rect()

# Початкові координати персонажа
character_x = screen.get_width() // 2 - character_rect.width // 2
character_y = screen.get_height() // 2 - character_rect.height // 2

# Швидкість руху персонажа
CHARACTER_SPEED = 5  

# Завантаження музики
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

# Завантаження зображення монетки
coin_img = pygame.image.load('coin.png')
coin_rect = coin_img.get_rect()
coin_rect.center = (random.randint(30, background_rect.width - 30), random.randint(30, background_rect.height - 30))

# Рахунок гравця
score = 0

# Швидкість переміщення монетки (в секундах)
coin_speed = 10

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Головний цикл гри
running = True
start_time = time.time()
level_2_reached = False
level_3_reached = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отримання стану всіх клавіш
    keys = pygame.key.get_pressed()

    # Перевірка натискання клавіш і рух персонажа
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

    # Перевірка зіткнення гравця і монетки
    if character_rect.colliderect(coin_rect):
        score += 1
        coin_rect.center = (random.randint(30, background_rect.width - 30), random.randint(30, background_rect.height - 30))

        # Перевірка рівня
        if score == 15 and not level_2_reached:
            coin_speed = 5
            level_2_reached = True
            draw_text("Level 2", pygame.font.Font(None, 72), WHITE, screen, background_rect.width // 2, background_rect.height // 2)
            pygame.display.update()
            time.sleep(3)  # Змінено час зупинки гри на 3 секунди
        elif score == 25 and not level_3_reached:
            coin_speed = 3
            level_3_reached = True
            draw_text("Level 3", pygame.font.Font(None, 72), WHITE, screen, background_rect.width // 2, background_rect.height // 2)
            pygame.display.update()
            time.sleep(3)  # Змінено час зупинки гри на 3 секунди

        # Перевірка завершення гри
        if score >= 40:
            draw_text("Finish!", pygame.font.Font(None, 72), WHITE, screen, background_rect.width // 2, background_rect.height // 2)
            pygame.display.update()
            time.sleep(5)  # Очікуємо 5 секунд
            pygame.quit()  # Закриваємо вікно гри
            sys.exit()    # Виходимо з програми

    # Перевірка часу для зміни положення монетки
    current_time = time.time()
    if current_time - start_time >= coin_speed:
        start_time = time.time()
        coin_rect.center = (random.randint(30, background_rect.width - 30), random.randint(30, background_rect.height - 30))

    # Оновлення координат гравця та монетки
    character_rect.topleft = (character_x, character_y)

    # Відображення зображень
    screen.blit(background_img, (0, 0))
    screen.blit(character_img, character_rect)
    screen.blit(coin_img, coin_rect)

    # Виведення рахунку
    draw_text(f"Score: {score}", pygame.font.Font(None, 36), WHITE, screen, background_rect.width // 2, 50)

    pygame.display.flip()

# Завершення гри
pygame.quit()

