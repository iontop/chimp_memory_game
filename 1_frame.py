import pygame

#초기화
pygame.init()
screen_width = 1280 # 가로
screen_height = 720 # 세로
screen=pygame.display.set_mode((screen_width, screen_height)) # 튜플형태로 넣기 위해 괄호를 하나 더 씀
pygame.display.set_caption("Memory Game")

#게임루프
running=True # 게임이 실행 중인지 확인하는 변수
while running:
    #이벤트 루프
    for event in pygame.event.get(): #어떤 이벤트가 발생했는가?
        if event.type==pygame.QUIT: #창이 닫히는 이벤트인가?
            running=False

#게임종료
pygame.QUIT