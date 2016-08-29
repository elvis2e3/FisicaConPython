# -*- coding: utf-8 -*-
import pygame as pg

def circulo(s, xy):
    pg.draw.circle(s, (200, 150, 250), xy, 50, 0)

def linea(s, xy1, xy2):
    pg.draw.line(s, (200, 250, 250), xy1, xy2, 1)

pg.init()
pantalla = pg.display.set_mode([800, 500])
salida = False
tiempo = pg.time.Clock()
xy = {1: [200, 200], 2: [400, 300], 3: [600, 400], 4: [500, 400]}
x1 = 200
y1 = 200
x2 = 400
y2 = 300
isClick = False
xyf = len(xy.keys())
while not salida:
    pantalla.fill((50, 50, 50))
    for e in pg.event.get():
        if e.type == pg.QUIT:
            salida = True
        elif e.type == pg.MOUSEBUTTONDOWN:
            isClick = True
        elif e.type == pg.MOUSEBUTTONUP:
            isClick = False
        elif e.type == pg.MOUSEMOTION and isClick:
            x, y = pg.mouse.get_pos()
            for i in xy.keys():
                if (xy[i][0] - 50) < x < (xy[i][0] + 50) and (xy[i][1] - 50) < y < (xy[i][1] + 50):
                    xy[i][0], xy[i][1] = x, y
    for i in range(1, xyf):
        linea(pantalla, (xy[i][0], xy[i][1]), (xy[i + 1][0], xy[i + 1][1]))
    linea(pantalla, (xy[1][0], xy[1][1]), (xy[xyf][0], xy[xyf][1]))
    for i in xy.keys():
        circulo(pantalla, (xy[i][0], xy[i][1]))
    pg.display.update()
    tiempo.tick(100)
pg.quit()