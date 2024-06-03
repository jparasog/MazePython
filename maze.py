import time
import pygame

pygame.init()
screen= pygame.display.set_mode((800,600))
done=False

x=30
y=30
z=700
w=30

ts1=time.time()
ts2=time.time()
tol1=0
tol2=0

clock=pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP]:y-=3
    if pressed[pygame.K_DOWN]:y+=3
    if pressed[pygame.K_LEFT]:x-=3
    if pressed[pygame.K_RIGHT]:x+=3

    if pressed[pygame.K_w]:w-=3
    if pressed[pygame.K_s]:w+=3
    if pressed[pygame.K_a]:z-=3
    if pressed[pygame.K_d]:z+=3

    screen.fill((0,0,0))

    pl1 = pygame.draw.rect(screen, (250, 0,0), pygame.Rect(x, y, 60, 60))
    pl2=pygame.draw.rect(screen,(0,0,245),pygame.Rect(z,w,60,60))

    wall1=pygame.draw.rect(screen,(246, 238, 200),pygame.Rect(100,20,40,300))
    wall2=pygame.draw.rect(screen,(246, 238, 200),pygame.Rect(250,150,40,300))

    wall3=pygame.draw.rect(screen,(246, 238, 200),pygame.Rect(630,20,40,300))
    wall4=pygame.draw.rect(screen,(246, 238, 200),pygame.Rect(480,150,40,300))

    wallend=pygame.draw.rect(screen,(136, 83, 228),pygame.Rect(350,300,60,60))

    if pl1.colliderect(wall1) or pl1.colliderect(wall2) or pl1.colliderect(wall3) or pl1.colliderect(wall4):
        if pressed[pygame.K_UP]:y+=5
        if pressed[pygame.K_DOWN]:y-=5
        if pressed[pygame.K_LEFT]:x+=5
        if pressed[pygame.K_RIGHT]:x-=5

    if pl2.colliderect(wall1) or pl2.colliderect(wall2) or pl2.colliderect(wall3) or pl2.colliderect(wall4):
        if pressed[pygame.K_w]:w+=5
        if pressed[pygame.K_s]:w-=5
        if pressed[pygame.K_a]:z+=5
        if pressed[pygame.K_d]:z-=5

    if pl1.colliderect(wallend):
        x=30
        y=30
        te1=time.time()
        tol1=round(te1-ts1,2)
        ts1=time.time()

    if pl2.colliderect(wallend):
        w=30
        z=700
        te2=time.time()
        tol2=round(te2-ts2,2)
        ts2=time.time()

    Font=pygame.font.SysFont("comicsansms",20,True,True)
    Time1=Font.render("Time: "+str(tol1),True,(255,255,255))
    screen.blit(Time1, (20, 65))

    Font=pygame.font.SysFont("comicsansms",20,True,True)
    Time2=Font.render("Time: "+str(tol2),True,(255,255,255))
    screen.blit(Time2, (690, 65))

    Font=pygame.font.SysFont("comicsansms",70,True,True)
    Title=Font.render("Maze Game ",True,(0, 153, 88))
    screen.blit(Title,(200,0))

    Font=pygame.font.SysFont("comicsansms",10,True,True)
    Title=Font.render("Start for player 1",True,(255,255,255))
    screen.blit(Title,(20,45))

    Font=pygame.font.SysFont("comicsansms",10,True,True)
    Title=Font.render("Start for player 2",True,(255,255,255))
    screen.blit(Title,(690,45))

    Font = pygame.font.SysFont("comicsansms", 20, True, True)
    Title = Font.render("Finish", True, (255, 255, 255))
    screen.blit(Title,(350,300))

    pygame.display.flip()
    clock.tick(60)
