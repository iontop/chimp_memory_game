import pygame

# 시작화면을 보여주는 함수
def display_start_screen():
    # 스크린안에 흰색으로 반지름 60, 두께 5짜리 원을 start_button_center에서 그린다.
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

# 게임화면을 보여주는 함수
def display_game_screen():
    print("Game Start")


# pos에 해당하는 버튼 확인
def check_buttons(pos):
    global start
    if start_button.collidepoint(pos): #사용자가 클릭한 위치가 start_button 내에 위치하면
        start=True

#초기화
pygame.init()
screen_width = 1280 # 가로
screen_height = 720 # 세로
screen=pygame.display.set_mode((screen_width, screen_height)) # 튜플형태로 넣기 위해 괄호를 하나 더 씀
pygame.display.set_caption("Memory Game")

#시작버튼
start_button=pygame.Rect(0, 0, 120, 120)
start_button.center=(120, screen_height-120)

#색깔
BLACK=(0,0,0) #RGB
WHITE=(255,255,255)

# 게임시작여부 판단
start=False

#게임루프
running=True # 게임이 실행 중인지 확인하는 변수
while running:
    click_pos=None
    
    #이벤트 루프
    for event in pygame.event.get(): #어떤 이벤트가 발생했는가?
        if event.type==pygame.QUIT: #창이 닫히는 이벤트인가?
            running=False
        elif event.type==pygame.MOUSEBUTTONUP: # 사용자가 마우스를 클릭했을 때
            click_pos=pygame.mouse.get_pos()
            print(click_pos)
        
    # 화면전체를 검게 칠하기
    screen.fill(BLACK)
    
    if start: 
        display_game_screen() #게임화면 표시
    else:
        display_start_screen() # 시작화면표시
    
    # 사용자가 클릭한 좌표값이 있다면 (어딘가 클릭했다면)
    if click_pos:
        check_buttons(click_pos)
    
    
    # 화면 업데이트
    pygame.display.update()
    
#게임종료
pygame.QUIT