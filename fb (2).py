import pygame
import random

from pygame.constants import K_RCTRL, K_r

pygame.init()
#pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappy Bird")


x = 50; y = 50; width = 30; height = 30; V = 5; a = 0.45; alive = True; counter = 0

tubes = [[random.randint(1,3),700],[random.randint(1,3),1100]]

run = True

while run == True:
    pygame.time.delay(30)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        V -= 3.5 
    if keys[K_r]:
        y = 50
        alive = True
        tubes = [[random.randint(1,3),700],[random.randint(1,3),1100]]
        counter = 0
        #print("+")
    
    V += a
    y += V

    if V <= -10:
        V = -10
    if V >= 10:
        V = 10



    #death
    if y <= 0 or y >= 600:
        alive = False
    if tubes[0][0] == 1 and tubes[0][1] >= 50 and tubes[0][1] <= 80 and (y < 120 or y > 240):
        alive = False
    if tubes[0][0] == 2 and tubes[0][1] >= 50 and tubes[0][1] <= 80 and (y < 240 or y > 360):
        alive = False
    if tubes[0][0] == 3 and tubes[0][1] >= 50 and tubes[0][1] <= 80 and (y < 360 or y > 480):
        alive = False


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

    if tubes[0][1] <= 0:
        counter += 1
        print(counter)
        tubes = [tubes[1], [random.randint(1,3), 800]]

    
    if alive == True:
        pygame.draw.rect(screen, (255,0,255), (x,y,width,height))
    else:
        #print("YOU ACHIVE " + str(counter) + " score!")
        #counter = 0
        pygame.draw.rect(screen, (124,55,100), (0,0,width,height))
    pygame.display.update()


pygame.QUIT()