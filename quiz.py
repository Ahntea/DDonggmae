import pygame
import random

# 기본 초기화
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("DDong Game")
 
# FPS
clock = pygame.time.Clock()
##########################################################

# 캐릭터는 화면 가장아래, 좌우로만 이동가능
# 똥은 화면 가장 위에서 x값 랜덤으로 떨어짐
# 똥을 피하면 다음 똥이 떨어짐
# 똥과 충돌하면 게임 종료

# 1. 사용자 게임 초기화 ( 배경화면, 게임 이미지, 좌표, 폰트 등)

background = pygame.image.load('C:\\Users\\user\\make_game\\pygame_basic\\back.png')
character = pygame.image.load('C:\\Users\\user\\make_game\\pygame_basic\\dog.png')
ddong = pygame.image.load('C:\\Users\\user\\make_game\\pygame_basic\\ddong.png')
ddong2 = pygame.image.load('C:\\Users\\user\\make_game\\pygame_basic\\ddong.png')

character_size = character.get_rect().size
character_size_width = character_size[0]
character_size_height = character_size[1]
character_x_pos = (screen_width - character_size_width)/2
character_y_pos = screen_height - character_size_height

to_x = 0
to_y = 0
character_speed = 1

ddong_size = ddong.get_rect().size
ddong_size_width = ddong_size[0]
ddong_size_height = ddong_size[1]

ddong_x_pos = random.randrange(0,screen_width-ddong_size_width)
ddong_y_pos = 0
ddong_speed = 0.4

ddong2_size = ddong.get_rect().size
ddong2_size_width = ddong_size[0]
ddong2_size_height = ddong_size[1]

ddong2_x_pos = random.randrange(0,screen_width-ddong_size_width)
ddong2_y_pos = -100
ddong2_speed = ddong_speed

game_font = pygame.font.Font(None, 60)
timer_font = pygame.font.Font(None, 60)

score = 0

running = True
while running:
    dt = clock.tick(60)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            #elif event.key == pygame.K_UP:
            #    to_y -= character_speed
            #elif event.key == pygame.K_DOWN:
            #    to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y =0

    # 3. 게임 케릭터 위치 정의
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos <0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_size_width:
        character_x_pos = screen_width - character_size_width
    
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_size_height:
        character_y_pos = screen_height - character_size_height
    
    if ddong_y_pos > screen_height - ddong_size_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randrange(0,screen_width-ddong_size_width)
        score += 100

    ddong_y_pos += ddong_speed * dt 

    if ddong2_y_pos > screen_height - ddong_size_height:
        ddong2_y_pos = random.randint(-200,-100)
        ddong2_x_pos = random.randrange(0,screen_width-ddong_size_width)
        score += 100
    
    ddong2_y_pos += ddong_speed * dt 

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    ddong2_rect = ddong2.get_rect()
    ddong2_rect.left = ddong2_x_pos
    ddong2_rect.top = ddong2_y_pos

    ddong_list = [ddong_rect, ddong2_rect]

    if character_rect.collidelist(ddong_list) != -1:
        print("충돌했어요")
        running = False

    # 5. 화면에 그리기
    
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ddong, (ddong_x_pos,ddong_y_pos))
    screen.blit(ddong2, (ddong2_x_pos,ddong2_y_pos))

    scoring = game_font.render(str(int(score)), True, (0,255,255))
    screen.blit(scoring, (screen_width - (pygame.font.Font.get_linesize(game_font)+100), 10))

    timer = pygame.time.get_ticks()/1000
    timer_act = game_font.render(str(int(timer)), True, (255,255,255))
    screen.blit(timer_act, (10,10))

    pygame.display.update()



pygame.quit()

