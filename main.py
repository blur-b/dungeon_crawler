import pygame
import time
import random
from character import Player 
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Crawlers")

PLAYER_WIDTH, PLAYER_HEIGHT = 80, 120
HP_WIDTH, HP_HEIGHT = 100, 20

BG = pygame.image.load("./assets/bkg.png")

FONT = pygame.font.SysFont("comicsans", 25)

def draw_stats(player):
    time_text = FONT.render(f"HP: {player.get_hp()}", 1, "white")
    WIN.blit(time_text, (10, 10))

    hp_bkg = pygame.image.load("./assets/player/hp_bkg.png")
    hp = pygame.transform.scale(pygame.image.load("./assets/player/hp.png"), (player.get_hp(), HP_HEIGHT))
    
    WIN.blit(hp_bkg, (10, 50))
    WIN.blit(hp, (10, 50))

def draw_player(player, sprite):
    WIN.blit(BG, (0, 0))
    WIN.blit(sprite, (player.get_x(), player.get_y()))
    draw_stats(player)

    pygame.display.update()

def main():
    run = True

    # player initialization
    player = Player(width=PLAYER_WIDTH, height=PLAYER_HEIGHT, x=WIDTH/2 - PLAYER_WIDTH/2, y=HEIGHT/2 - PLAYER_HEIGHT/2)
    player_sprite = pygame.image.load("./assets/player/right.png")

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        # player movement
        if keys[pygame.K_LEFT] and player.get_x() - player.get_speed() >= 0:
            player_x = player.get_x() - player.get_speed()
            player.set_x(player_x)
            player_sprite = pygame.image.load("./assets/player/left.png")
        if keys[pygame.K_RIGHT] and player.get_x() + player.get_speed() + player.get_width() <= WIDTH:
            player_x = player.get_x() + player.get_speed()
            player.set_x(player_x)
            player_sprite = pygame.image.load("./assets/player/right.png")
        if keys[pygame.K_UP] and player.get_y() - player.get_speed() >= 0:
            player_y = player.get_y() - player.get_speed()
            player.set_y(player_y)
        if keys[pygame.K_DOWN] and player.get_y() + player.get_speed() + player.get_height() <= HEIGHT:
            player_y = player.get_y() + player.get_speed()
            player.set_y(player_y)

        draw_player(player, player_sprite)

    pygame.quit()

if __name__ == "__main__":
    main()