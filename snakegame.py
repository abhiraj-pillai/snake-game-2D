import pygame,sys,random
from pygame.locals import *



SCREENWIDTH = 350
SCREENHEIGTH = 550
clock = pygame.time.Clock()
pygame.init
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGTH))
info = pygame.display.Info()
ix = (info.current_w/2) - 10
iy = (info.current_h/2) -10

def gameoverf(score):
    while True:
        screen.fill((0,0,0))
        font2 = pygame.font.SysFont("times new roman",30,bold = True) 
        text2 = font2.render(f'Game Over', True, (255,255,255))
        text3 = font2.render(f"Score {score}", True, (255,255,255))
        screen.blit(text2,(110,200))
        screen.blit(text3,(110,250))

        pygame.display.update()
        clock.tick(32)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
               
    

def plot_snake(gameWindow, color, snk_list, swidth,sheigth):
    for x,y in snk_list:
        pygame.draw.rect(screen,(255,0,0),[x,y,swidth,sheigth])

if __name__ == "__main__":
    pygame.init
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGTH))
    info = pygame.display.Info()
    ix = (info.current_w/2) - 10
    iy = (info.current_h/2) -10
    velocityx = 0
    velocityy = 0
    swidth = 20
    sheigth = 20
    score = 0
    snk_list =[]
    food_x = random.randint(20, ix)
    food_y = random.randint(20, iy)
    gameover = False
    snk_length = 1
    eaten = True
    
    while not gameover:
        
        pygame.font.init()
        rectangle_surf = pygame.draw.rect(screen,(255,0,0),[ix,iy,swidth,sheigth])
        font = pygame.font.Font("C:\\Python 3.7.1\\Projects\\fontnew.ttf", 19) 
        text = font.render('Press space to start', True, (255,255,255))
        screen.blit(text,(80,200))
        pygame.display.update()
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == pygame.K_SPACE:
                
                while not gameover:
                
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit() 
                        if event.type == KEYDOWN and event.key == pygame.K_UP:    
                             velocityy = -4  
                             velocityx = 0
                        if event.type == KEYDOWN and event.key == pygame.K_LEFT: 
                            velocityx = -4
                            velocityy = 0
                        if event.type == KEYDOWN and event.key == pygame.K_DOWN: 
                             velocityy = +4
                             velocityx = 0
                        if event.type == KEYDOWN and event.key == pygame.K_RIGHT:  
                             velocityx = +4
                             velocityy = 0

                    ix += velocityx
                    iy += velocityy
                    screen.fill((0,0,0)) 
                    
                    food_rect = pygame.draw.rect(screen, (150,150,200), [food_x -10 , food_y-10 ,15,15])
                    rect_rect = pygame.draw.rect(screen,(255,0,0),[ix ,iy,swidth,sheigth])

                    if rect_rect.colliderect(food_rect.inflate(-15,-15)) and eaten:
                        score = score + 10
                        food_x = random.randint(20, info.current_w)
                        food_y = random.randint(20, info.current_h)
                        # food_rect = pygame.draw.rect(screen, (150,150,200), [food_x, food_y,15,15])
                        snk_length += 5
                        eaten = False
                    if not rect_rect.colliderect(food_rect.inflate(-15,-15)):
                        eaten = True

                    if ix<0 or ix> info.current_w or iy<0 or iy >info.current_h:
                        
                        gameover = True

                    head = []
                    head.append(ix)
                    head.append(iy)
                    snk_list.append(head)

                    if len(snk_list)>snk_length:
                        del snk_list[0]
                    
                    plot_snake(screen, (255,0,0), snk_list, swidth,sheigth)
                    font1 = pygame.font.SysFont("arial",17,bold = True, italic = True) 
                    text1 = font1.render(f'Score {score}', True, (255,255,255))
                    screen.blit(text1,(30,30))
                    pygame.display.update()
                    clock.tick(32)
                    
    gameoverf(score)                