import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 10, 1.0)]
    bg_imgs = pg.transform.flip(bg_img, True, False)
    tmr = 0
    bg_x = 0
    kk_x = 300
    kk_y = 200
    kk_speed_x = 1.5
    kk_speed_y = 1.5
    MAX_FPS = 100
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        bg_x -= 1.5
        if bg_x <= -1600:
            bg_x = 0

        screen.blit(bg_img, [bg_x, 0])
        screen.blit(bg_imgs, [bg_x + 1600, 0])
        screen.blit(kk_imgs[0], (int(kk_x), int(kk_y)))
        # screen.blit(kk_imgs[tmr%2], [int(kk_x), int(kk_y)])
        pg.display.update()
        # bg_x += 1        #tmrでも可
        # if(bg_x > 1600):
        target_x = 400.0  # 目標とするx座標
        target_y = 300.0  # 目標とするy座標

        # kk_xとkk_yを滑らかに移動させる
        kk_x += (target_x - kk_x) * 0.05
        kk_y += (target_y - kk_y) * 0.05

        # kk_x += kk_speed_x
        # kk_y += kk_speed_y
        # if kk_x <= 0 or kk_x >= 800 - kk_img.get_width():
        #     kk_speed_x *= -1
        # if kk_y <= 0 or kk_y >= 600 - kk_img.get_height():
        #     kk_speed_y *= -1
        # if kk_y <= 200 or kk_y >= 300:
        #     kk_speed_y *= -1
        clock.tick(MAX_FPS)

        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()