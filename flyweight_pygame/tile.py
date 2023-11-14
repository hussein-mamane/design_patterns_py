import pygame as pg


class Tile(pg.sprite.Sprite):
    def __init__(self, img_path: str, scale: int, pos_x: int, pos_y: int):
        img = pg.image.load(img_path)
        self.image = pg.transform.scale(img, (int(img.get_width() * scale),
                                              int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    # def draw(self, screen):
    #     screen.blit(self.image, self.rect)
