import pygame
 
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Nado Game")
 
# FPS
clock = pygame.time.Clock()

background = pygame.image.load('C:\\Users\\user\\game_pygame\\pygame_basic\\background.png')

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load('C:\\Users\\user\\game_pygame\\pygame_basic\\character.png')
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.3

# 적 enemy 캐릭터
enemy = pygame.image.load('C:\\Users\\user\\game_pygame\\pygame_basic\\enemy.png')
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width - enemy_width) / 2
enemy_y_pos = screen_height/2 - enemy_height/2

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks()

# 이벤트 루프
running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y =0
    
    character_x_pos += to_x * dt 
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos <0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos <0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    screen.fill((0,0,255))
    #screen.blit(background, (0,0))

    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))

    # 타이머 집어 넣기
    # 경과시간 계산
    elasped_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시

    timer = game_font.render(str(int(total_time - elasped_time)), True, (255,255,255))
    screen.blit(timer, (10,10))

    # 시간 조건 생성
    if total_time - elasped_time <=0:
        print("타임아웃")
        running = False

# 잠시 대기

    pygame.display.update()

pygame.time.delay(2000)

pygame.quit()

