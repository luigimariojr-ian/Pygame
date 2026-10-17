import pygame as py

py.init()
screen = py.display.set_mode((800, 600))
py.display.set_caption(("pygaming :)))"))

bee = py.image.load("Assets\\bee_minecraft_floating_by_transparentjigglypt2_dhckttg-fullview.png")
bee = py.transform.scale(bee, (70, 70))
beesprite = bee.get_rect()
beesprite.center = (400, 300)

poppy = py.image.load("Assets\\minecraft-poppy.png")
poppy = py.transform.scale(poppy, (70, 70))
poppysprite = poppy.get_rect()
poppysprite.center = (600, 300)

running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    keys = py.key.get_pressed()
    if keys[py.K_LEFT]:
        beesprite.x = beesprite.x - 5
    if keys[py.K_RIGHT]:
        beesprite.x = beesprite.x + 5
    if keys[py.K_UP]:
        beesprite.y = beesprite.y - 5
    if keys[py.K_DOWN]:
        beesprite.y = beesprite.y + 5

    screen.fill("#ADEFFF")
    screen.blit(bee, beesprite)
    screen.blit(poppy, poppysprite)
    py.display.update()


py.quit()