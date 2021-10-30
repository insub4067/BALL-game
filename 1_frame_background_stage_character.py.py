import pygame
import os

####################################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("BALLOON PANG PANG")

# FPS
clock = pygame.time.Clock()
####################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트 등)

# 현재 파일 위치 
current_path = os.path.dirname(__file__)

# 이미지 폴더 위치 반환
image_path = os.path.join(current_path, "images")

# 배경 이미지
background = pygame.image.load(os.path.join(image_path, "background.jpeg"))

# 스테이지 이미지
stage = pygame.image.load(os.path.join(image_path, "stage.jpeg"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터 이미지 
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = ( screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

# 폰트
game_font = pygame.font.Font(None, 40) # (폰트, 크기)

running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. 캐릭터 위치 조정

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos,character_y_pos))
    
    # 게임 화면 다시 그리기
    pygame.display.update()

pygame.quit()