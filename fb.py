import pygame
import random

font_name = pygame.font.match_font('arial')

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (254, 231, 240))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

from pygame.constants import K_RCTRL, K_r

pygame.init()
#pygame.mixer.init()
screen = pygame.display.set_mode((1700, 600))
pygame.display.set_caption("Flappy Bird")


x = 50; y = 50; width = 30; height = 30; V = 5; a = 0.45; alive = True; counter = 0; player2 = True; y2 = 50; V2 = 5; x2 = 1650; counter2 = 0

tubes = [[random.randint(1,3),600],[random.randint(1,3),1000]]
tubes2 = [[random.randint(1,3),1100],[random.randint(1,3),700]]

run = True

while run == True:
    pygame.time.delay(25)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        V -= 3.5 

    if keys[pygame.K_UP]:
        V2 -= 3.5 

    if keys[K_r]:
        y = 50
        y2 = 60
        alive = True
        player2 = True
        tubes = [[random.randint(1,3),600],[random.randint(1,3),1000]]
        tubes2 = [[random.randint(1,3),1000],[random.randint(1,3),600]]
        counter = 0; counter2 = 0
        #print("+")
    
    V += a
    y += V

    V2 += a
    y2 += V2

    if V <= -10:
        V = -10
    if V >= 10:
        V = 10

    if V2 <= -10:
        V2 = -10
    if V2 >= 10:
        V2 = 10



    #death
    if y <= 0 or y >= 600:
        alive = False
    if tubes[0][0] == 1 and tubes[0][1] >= 50 and tubes[0][1] <= 80 and (y < 120 or y > 240):
        alive = False
    if tubes[0][0] == 2 and tubes[0][1] >= 50 and tubes[0][1] <= 80 and (y < 240 or y > 360):
        alive = False
    if tubes[0][0] == 3 and tubes[0][1] >= 50 and tubes[0][1] <= 80 and (y < 360 or y > 480):
        alive = False

    #death2
    if y2 <= 0 or y2 >= 600:
        player2 = False
    if tubes2[0][0] == 1 and tubes2[0][1] >= 1620 and tubes2[0][1] <= 1650 and (y2 < 120 or y2 > 240):
        player2 = False
    if tubes2[0][0] == 2 and tubes2[0][1] >= 1620 and tubes2[0][1] <= 1650 and (y2 < 240 or y2 > 360):
        player2 = False
    if tubes2[0][0] == 3 and tubes2[0][1] >= 1620 and tubes2[0][1] <= 1650 and (y2 < 360 or y2 > 480):
        player2 = False


    screen.fill((0,0,0))

    for i in range(len(tubes)):
        if alive == True:
            tubes[i][1] -= 10
        if tubes[i][0] == 1:
            pygame.draw.rect(screen, (0,255,0), (tubes[i][1], 0, 50, 120))
            pygame.draw.rect(screen, (0,255,0), (tubes[i][1], 240, 50, 360))
        if tubes[i][0] == 2:
            pygame.draw.rect(screen, (0,255,0), (tubes[i][1], 0, 50, 240))
            pygame.draw.rect(screen, (0,255,0), (tubes[i][1], 360, 50, 240))
        if tubes[i][0] == 3:
            pygame.draw.rect(screen, (0,255,0), (tubes[i][1],0, 50, 360))
            pygame.draw.rect(screen, (0,255,0), (tubes[i][1],480, 50, 120))

    for i in range(len(tubes2)):
        if player2 == True:
            tubes2[i][1] += 10
        if tubes2[i][0] == 1:
            pygame.draw.rect(screen, (255,0,0), (tubes2[i][1], 0, 50, 120))
            pygame.draw.rect(screen, (255,0,0), (tubes2[i][1], 240, 50, 360))
        if tubes2[i][0] == 2:
            pygame.draw.rect(screen, (255,0,0), (tubes2[i][1], 0, 50, 240))
            pygame.draw.rect(screen, (255,0,0), (tubes2[i][1], 360, 50, 240))
        if tubes2[i][0] == 3:
            pygame.draw.rect(screen, (255,0,0), (tubes2[i][1],0, 50, 360))
            pygame.draw.rect(screen, (255,0,0), (tubes2[i][1],480, 50, 120))

    if tubes[0][1] <= 0:
        counter += 1
        #print(counter)
        tubes = [tubes[1], [random.randint(1,3), 800]]

    if tubes2[0][1] >= 1700:
        counter2 += 1
        #print(counter)
        tubes2 = [tubes2[1], [random.randint(1,3), 800]]

    
    if player2 == True:
        pygame.draw.rect(screen, (0,255,0), (x2,y2,width,height))
    else:
        pygame.draw.rect(screen, (255,255,255), (1670,570,width,height))

    if alive == True:
        pygame.draw.rect(screen, (255,0,0), (x,y,width,height))
    else:
        #print("YOU ACHIVE " + str(counter) + " score!")
        #counter = 0
        pygame.draw.rect(screen, (255,255,255), (0,570,width,height))

    draw_text(screen, str(counter), 50, 75, 15)

    draw_text(screen, str(counter2), 50, 1615, 15)

    pygame.draw.rect(screen, (120,125,230), (845,0,10,600))

    pygame.display.update()


pygame.QUIT()