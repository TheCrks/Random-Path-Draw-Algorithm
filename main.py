import pygame
from random import randint

width = 600
height = 730
red = (255, 0, 0)
pathColour = (100, 100, 100)
coordX = width / 2
coordY = 0
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
coordLists = [[250, 0, 0], [250, 30, 1], [250, 60, 2]]


def drawBackGround():
    window.fill((255, 255, 255))
    pygame.display.update()


def drawFirstThree():
    global coordX, coordY
    for i in range(0, 90, 30):
        pygame.draw.rect(window, pathColour, pygame.Rect(coordX, coordY, 30, 30))
        coordY += 30
    coordY-=30
    pygame.display.update()


def indexof(List, index):
    out = False
    for i in range(0, len(List)):
        if index == List[i]:
            out = True
    return out


def drawPathDown():
    global coordX, coordY, coordLists
    coordY += 30
    pygame.draw.rect(window, pathColour, pygame.Rect(coordX, coordY, 30, 30))
    coordLists.append([coordX, coordY, 3])
    pygame.display.update()


def drawPathRight():
    global coordX, coordY, coordLists
    coordX += 30
    pygame.draw.rect(window, pathColour, pygame.Rect(coordX, coordY, 30, 30))
    coordLists.append([coordX, coordY, 3])
    pygame.display.update()


def drawPathLeft():
    global coordX, coordY, coordLists
    coordX -= 30
    pygame.draw.rect(window, pathColour, pygame.Rect(coordX, coordY, 30, 30))
    coordLists.append([coordX, coordY, 3])
    pygame.display.update()


def turnChance(percent):
    number = randint(0, 100)
    randomList = []
    for i in range(0, percent):
        randomList.append(randint(0, 100))
    if indexof(randomList, number):
        return True
    else:
        return False


def turnDown():
    turn = False
    global coordLists, coordY, coordX
    if coordLists[len(coordLists)-1][0] <= 120 or coordLists[len(coordLists)-1][0] >= width-120:
        turn = True
    if coordLists[len(coordLists)-1][1] == coordLists[len(coordLists) - 2][1] == coordLists[len(coordLists) - 3][1]:
        turn = turnChance(60)
    elif coordLists[len(coordLists)-1][1] == coordLists[len(coordLists) - 2][1] != coordLists[len(coordLists) - 3][1]:
        turn = turnChance(30)
    else:
        turn = False
    return turn


def turnRL():
    turn = False
    global coordLists, coordY, coordX
    if coordLists[len(coordLists) - 1][0] == coordLists[len(coordLists) - 2][0] == coordLists[len(coordLists) - 3][0] == coordLists[len(coordLists) - 4][0]:
        turn = turnChance(50)
    elif coordLists[len(coordLists) - 1][0] == coordLists[len(coordLists) - 2][0] == coordLists[len(coordLists) - 3][0] != coordLists[len(coordLists) - 4][0]:
        turn = turnChance(20)
    else:
        turn = False
    return turn


def direction():
    if coordLists[len(coordLists)-1][0] == coordLists[len(coordLists) - 2][0]:
        return "Down"
    else:
        if coordLists[len(coordLists)-1][0] > coordLists[len(coordLists) - 2][0]:
            return "Right"
        else:
            return "Left"


def drawPath():
    counter = 3
    run = True
    drawPathDown()
    while run:
        if direction() == "Down":
            if turnRL():
                if coordLists[len(coordLists)-1][0]>=width-240:
                    if turnChance(60):
                        print(direction())
                        drawPathLeft()
                    else:
                        print(direction())
                        drawPathRight()
                elif coordLists[len(coordLists)-1][0]>=width-120:
                    if turnChance(80):
                        print(direction())
                        drawPathLeft()
                    else:
                        print(direction())
                        drawPathRight()
                elif coordLists[len(coordLists)-1][0]>=width-90:
                    if turnChance(90):
                        print(direction())
                        drawPathLeft()
                    else:
                        print(direction())
                        drawPathRight()
                elif coordLists[len(coordLists)-1][0]<=240:
                    if turnChance(60):
                        print(direction())
                        drawPathLeft()
                    else:
                        print(direction())
                        drawPathRight()
                elif coordLists[len(coordLists)-1][0]<=120:
                    if turnChance(80):
                        print(direction())
                        drawPathLeft()
                    else:
                        print(direction())
                        drawPathRight()
                elif coordLists[len(coordLists)-1][0]<=90:
                    if turnChance(90):
                        print(direction())
                        drawPathLeft()
                    else:
                        print(direction())
                        drawPathRight()
                else:
                    if turnChance(50):
                        print(direction())
                        drawPathLeft()
                    else:
                        print(direction())
                        drawPathRight()
            else:
                print(direction())
                drawPathDown()
        elif direction() == "Left":
            if coordLists[len(coordLists)-1][0]<=90:
                print(direction())
                drawPathDown()
            else:
                if turnDown():
                    print(direction())
                    drawPathDown()
                else:
                    print(direction())
                    drawPathLeft()

        else:
            if coordLists[len(coordLists)-1][0]>=width-90:
                drawPathDown()
            else:
                if turnDown():
                    print(direction())
                    drawPathDown()
                else:
                    print(direction())
                    drawPathRight()
        counter += 1
        if coordLists[counter][1] >= height:
            run = False


def mainLoop():
    loop = True
    clock = pygame.time.Clock()
    drawBackGround()
    drawFirstThree()
    drawPath()
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                pygame.quit()
        clock.tick(400)
        pygame.display.update()


mainLoop()
