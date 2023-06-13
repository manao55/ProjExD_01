import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 10, 1.0)]
    bg_x = 0
    kk_x = 300.0
    kk_y = 200.0
    kk_speed_x = 1.5
    kk_speed_y = 1.5
    MAX_FPS = 100

    smooth_scroll = 0.0
    target_scroll = 0.0
    scroll_speed = 0.5

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 目標のスクロール位置を設定
        target_scroll -= scroll_speed
        if target_scroll <= -1600:
            target_scroll = 0

        # スクロールを滑らかに移動させる
        smooth_scroll += (target_scroll - smooth_scroll) * 0.1

        # 背景画像を描画
        screen.blit(bg_img, (smooth_scroll, 0))
        screen.blit(bg_img, (smooth_scroll + 1600, 0))

        # キャラクターを描画
        screen.blit(kk_imgs[0], (int(kk_x), int(kk_y)))

        pg.display.update()

        target_x = 400.0  # 目標とするx座標
        target_y = 300.0  # 目標とするy座標

        # kk_xとkk_yを滑らかに移動させる
        kk_x += (target_x - kk_x) * 0.05
        kk_y += (target_y - kk_y) * 0.05

        clock.tick(MAX_FPS)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()





