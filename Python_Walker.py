import pygame
import random
pygame.init()
pygame.display.set_caption("Circle Walk")
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
StopGame = False
CX = 400
CY = 400
C = [CX, CY]

def draw(c1, c2, c3, cx, cy, rt):
    for i in range(rt):
        randx = random.randint(1,3)
        if randx == 1:
            cx += random.randint(20,50)
        elif randx == 2:
            cx -= random.randint(20,50) 
        randy = random.randint(1,3)
        if randy == 1:
            cy += random.randint(20,50)
        elif randy == 2:
            cy -= random.randint(20,50)
        if cx > 800:
            cx -= 799
        if cx < 0:
            cx += 799
        if cy > 800:
            cy -= 799
        if cy < 0:
            cy += 799
        pygame.draw.circle(screen, (c1, c2, c3), (cx, cy), 4, 1)
        #pygame.display.flip()
    return [cx, cy]
while not StopGame:   
    clock.tick(60)
    C1 = random.randint(0,255)
    C2 = random.randint(0,255)
    C3 = random.randint(0,255)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            StopGame = True   
    C = draw(C1, C2, C3, C[0], C[1], 50)
    pygame.display.flip()
pygame.quit()