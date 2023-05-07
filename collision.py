import pygame

def check_collision(chara1, chara2):
    rect1 = chara1.get_sprite().get_rect(topleft=(chara1.get_x(), chara1.get_y()))
    rect2 = chara2.get_sprite().get_rect(topleft=(chara2.get_x(), chara2.get_y()))
    return pygame.Rect.colliderect(rect1, rect2)