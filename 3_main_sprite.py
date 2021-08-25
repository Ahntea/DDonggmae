import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Nado Game")

background = pygame.image.load('C:\\Users\\user\\game_pygame\\pygame_basic\\background.png')

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load('C:\\Users\\user\\game_pygame\\pygame_basic\\character.png')
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False

    screen.fill((0,0,255))
    #screen.blit(background, (0,0))

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()

