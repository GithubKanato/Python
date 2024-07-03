import pygame
import time
import random

pygame.init()

# ゲームのウィンドウサイズ
window_x = 720
window_y = 480

# 色の定義
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

# ゲームウィンドウの設定
pygame.display.set_caption('スネークゲーム')
game_window = pygame.display.set_mode((window_x,window_y))

# FPSコントローラ
fps = pygame.time.Clock()

# スネークのデフォルトの位置
snake_position = [100,50]

# スネークの体の初期化
snake_body = [[100,50],[90,50],[80,50],[70,50]]

# 食べ物の初期化
food_position = [random.randrange(1,(window_x//10))*10,
                 random.randrange(1,(window_y//10))*10]
food_spawn = True

# デフォルトのスネークの方向
direction = 'RIGHT'
change_to = direction

# スコアの初期化
score = 0

# スコアの表示機能
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font,size)
    score_surface = score_font.render('Score:'+str(score),True,color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (window_x/10,15)
    else:
        score_rect.midtop = (window_x/2,window_y/1.25)
    game_window.blit(score_surface, score_rect)
    pygame.display.flip()

# ゲームオーバーの機能
def game_over():
    my_font = pygame.font.SysFont('Arial',50)
    game_over_surface = my_font.render('GAME OVER',True,red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2,window_y/4)
    game_window.blit(game_over_surface,game_over_rect)
    show_score(0,red,'times',20)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# メイン
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    
    if change_to == 'UP' and direction != 'DOWN':
        direction = change_to
    if change_to == 'DOWN' and direction != 'UP':
        direction = change_to
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = change_to
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = change_to

    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
    
    snake_body.insert(0,list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()
    
    if not food_spawn:
        food_position = [random.randrange(1, (window_x // 10)) * 10,
                         random.randrange(1, (window_y // 10)) * 10]
    food_spawn = True

    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(
            pos[0], pos[1], 10, 10
        ))
    
    pygame.draw.rect(game_window, white, pygame.Rect(
        food_position[0], food_position[1],10,10
    ))

    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
        
    show_score(1,white,'Arial',20)
    pygame.display.update()
    fps.tick(25)