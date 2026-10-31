import pygame as py

py.init()
screen = py.display.set_mode((800, 600))
py.display.set_caption("recicling ooo :)))")
greenbin = py.image.load("Assets\\58938e8d8370b70e212f3e3e.webp")
greenbin = py.transform.scale(greenbin, (150, 150))
greenbinsprite = greenbin.get_rect()
greenbinsprite.center = (100, 500)

gb = py.image.load("Assets\\a-glass-bottle-with-a-black-lid-on-a-transparent-background-free-png.webp")
gb = py.transform.scale(gb, (150, 150))
gbs = gb.get_rect()
gbs.center = (50, 100)

pb = py.image.load("Assets\\clear-plastic-water-bottle-isolated-on-a-transparent-background-perfect-for-hydration-fitness-and-travel-themes-in-commercial-photography-png.webp")
pb = py.transform.scale(pb, (150, 150))
pbs = gb.get_rect()
pbs.center = (250, 100)

burg = py.image.load("Assets\\pngtree-cheese-burger-image-without-background-png-image_6728392.webp")
burg = py.transform.scale(burg, (150, 150))
burgsp = burg.get_rect()
burgsp.center = (550, 100)

fries = py.image.load("Assets\\fast-food-of-fries-potatoes-isolated-on-transparent-background-png.webp")
fries = py.transform.scale(fries, (150, 150))
friessp = fries.get_rect()
friessp.center = (750, 100)

redbin = py.image.load("Assets\\modern-red-translucent-recycle-bin-with-silver-lid-for-waste-management-png.webp")
redbin = py.transform.scale(redbin, (100, 100))
redbinsprite = redbin.get_rect()
redbinsprite.center = (700, 500)

score = 0

font1 = py.font.SysFont("Arial", 20)
text1 = font1.render("score: " + str(score), "#000000", True)

running = True
draggingpb = False
dragginggb = False
draggingburg = False
draggingfries = False
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

        if event.type == py.MOUSEBUTTONDOWN:
            if pbs.collidepoint(event.pos):
                draggingpb = True
                draggingburg = False
                draggingfries = False
                dragginggb = False
            if gbs.collidepoint(event.pos):
                dragginggb = True
                draggingpb = False
                draggingburg = False
                draggingfries = False
            if burgsp.collidepoint(event.pos):
                draggingburg = True
                draggingfries = False
                dragginggb = False
                draggingpb = False
            if friessp.collidepoint(event.pos):
                draggingfries = True
                draggingpb = False
                draggingburg = False
                dragginggb = False
                

        if event.type == py.MOUSEMOTION:
            if draggingpb == True:
                pbs.center = event.pos
            if dragginggb == True:
                gbs.center = event.pos
            if draggingburg == True:
                burgsp.center = event.pos
            if draggingfries == True:
                friessp.center = event.pos

        if event.type == py.MOUSEBUTTONUP:
            draggingpb = False
            draggingburg = False
            draggingfries = False
            dragginggb = False

    #+Score
    if pbs.colliderect(greenbinsprite):
        draggingpb = False
        pbs.center = (2000, 2000)
        score = score + 1
        text1 = font1.render("score: " + str(score), "#000000", True)

    if gbs.colliderect(greenbinsprite):
        dragginggb = False
        gbs.center = (2000, 2000)
        score = score + 1
        text1 = font1.render("score: " + str(score), "#000000", True)

    if burgsp.colliderect(redbinsprite):
        draggingburg = False
        burgsp.center = (2000, 2000)
        score = score + 1
        text1 = font1.render("score: " + str(score), "#000000", True)

    if friessp.colliderect(redbinsprite):
        draggingfries = False
        friessp.center = (2000, 2000)
        score = score + 1
        text1 = font1.render("score: " + str(score), "#000000", True)

    #-Score
    if pbs.colliderect(redbinsprite):
        draggingpb = False
        pbs.center = (2000, 2000)
        score = score - 1
        text1 = font1.render("score: " + str(score), "#000000", True)
    
    if gbs.colliderect(redbinsprite):
        dragginggb = False
        gbs.center = (2000, 2000)
        score = score - 1
        text1 = font1.render("score: " + str(score), "#000000", True)
    
    if burgsp.colliderect(greenbinsprite):
        draggingburg = False
        burgsp.center = (2000, 2000)
        score = score - 1
        text1 = font1.render("score: " + str(score), "#000000", True)
    
    if friessp.colliderect(greenbinsprite):
        draggingfries = False
        friessp.center = (2000, 2000)
        score = score - 1
        text1 = font1.render("score: " + str(score), "#000000", True)


    screen.fill("#FFFFFF")
    screen.blit(greenbin ,greenbinsprite)
    screen.blit(redbin ,redbinsprite)
    screen.blit(gb ,gbs)
    screen.blit(pb ,pbs)
    screen.blit(burg ,burgsp)
    screen.blit(fries ,friessp)
    screen.blit(text1, (370 , 50))
    text1 = font1.render("score: " + str(score), "#000000", True)
    py.display.update()

py.quit()