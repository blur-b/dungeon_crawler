import pygame
import time
import random
from character import *
from collision import *
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Dungeon Crawler")

PLAYER_WIDTH, PLAYER_HEIGHT = 80, 120
SLIME_WIDTH = 80
HP_WIDTH, HP_HEIGHT = 100, 20
ST_WIDTH, ST_HEIGHT = 100, 20

# load images
BG = pygame.image.load("./assets/bkg.png")
HP_BKG = pygame.image.load("./assets/player/hp_bkg.png")
HP = pygame.image.load("./assets/player/hp.png")
ST_BKG = pygame.image.load("./assets/player/st_bkg.png")
ST = pygame.image.load("./assets/player/st.png")
PLAYER_L = pygame.image.load("./assets/player/left.png")
PLAYER_R = pygame.image.load("./assets/player/right.png")
SLIME_L = pygame.image.load("./assets/slime/left.png")
SLIME_R = pygame.image.load("./assets/slime/right.png")

# text fonts
STAT_FONT = pygame.font.SysFont("comicsans", 15, bold=True)
GG_FONT = pygame.font.SysFont("comicsans", 50)

def draw_stats(player):
    hp_text = STAT_FONT.render(f"HP: {player.get_hp()}", 1, "white")
    st_text = STAT_FONT.render(f"ST: {player.get_stamina()}", 1, "white")

    hp = pygame.transform.scale(HP, (player.get_hp(), HP_HEIGHT))
    st = pygame.transform.scale(ST, (player.get_stamina(), HP_HEIGHT))
    
    WIN.blit(HP_BKG, (10, 10))
    WIN.blit(hp, (10, 10))
    WIN.blit(ST_BKG, (10, 40))
    WIN.blit(st, (10, 40))

    WIN.blit(hp_text, (11, 9))
    WIN.blit(st_text, (11, 39))

def draw(player, slime):
    WIN.blit(BG, (0, 0))
    WIN.blit(player.get_sprite(), (player.get_x(), player.get_y()))
    WIN.blit(slime.get_sprite(), (slime.get_x(), slime.get_y()))
    draw_stats(player)

    pygame.display.update()

def check_player_moved(keys):
    return keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]

def move_player(keys, player):
    # sprint
    if keys[pygame.K_LSHIFT] and player.get_stamina() > 0:
        player.set_speed(player.get_base_speed() + player.get_sprint())
    else:
        player.set_speed(player.get_base_speed())

    # basic wasd movement
    if keys[pygame.K_a] and player.get_x() - player.get_speed() >= 0:
        player_x = player.get_x() - player.get_speed()
        player.set_x(player_x)
        player.set_sprite(PLAYER_L)
    if keys[pygame.K_d] and player.get_x() + player.get_speed() + player.get_width() <= WIDTH:
        player_x = player.get_x() + player.get_speed()
        player.set_x(player_x)
        player.set_sprite(PLAYER_R)
    if keys[pygame.K_w] and player.get_y() - player.get_speed() >= 0:
        player_y = player.get_y() - player.get_speed()
        player.set_y(player_y)
    if keys[pygame.K_s] and player.get_y() + player.get_speed() + player.get_height() <= HEIGHT:
        player_y = player.get_y() + player.get_speed()
        player.set_y(player_y)

def main():
    run = True

    # player initialization
    player = Player(sprite = PLAYER_R, width=PLAYER_WIDTH, height=PLAYER_HEIGHT, 
                    x=WIDTH/2 - PLAYER_WIDTH/2, y=HEIGHT/2 - PLAYER_HEIGHT/2)

    # slime initialization
    slime = Slime(sprite = SLIME_R, width=SLIME_WIDTH, height=SLIME_WIDTH)

    clock = pygame.time.Clock()

    # slime attack delay
    slime_delay = 1500
    slime_attack_event = pygame.USEREVENT + 1
    pygame.time.set_timer(slime_attack_event, slime_delay)

    # sprint stamina drain
    stamina_delay = 100
    stamina_event = pygame.USEREVENT + 2
    pygame.time.set_timer(stamina_event, stamina_delay)

    while run:
        clock.tick(60)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            # slime attack
            if event.type == slime_attack_event and check_collision(player, slime):
                player_hp = player.get_hp() - slime.get_damage()
                player.set_hp(player_hp)
                pygame.time.set_timer(slime_attack_event, slime_delay)

            # stamina drain
            if event.type == stamina_event and keys[pygame.K_LSHIFT] and check_player_moved(keys):
                player_st = player.get_stamina() - 5
                player.set_stamina(player_st)
                pygame.time.set_timer(stamina_event, stamina_delay)
            # stamina regen
            elif event.type == stamina_event and not check_player_moved(keys):
                player_st = player.get_stamina() + 2
                player.set_stamina(player_st)
                pygame.time.set_timer(stamina_event, stamina_delay)

        # player movement
        move_player(keys, player)

        # slime movement
        if slime.get_x() < player.get_x():
            slime_x = slime.get_x() + slime.get_speed()
            slime.set_x(slime_x)
            slime.set_sprite(SLIME_R)
        if slime.get_x() > player.get_x():
            slime_x = slime.get_x() - slime.get_speed()
            slime.set_x(slime_x)
            slime.set_sprite(SLIME_L)
        if slime.get_y() < player.get_y():
            slime_y = slime.get_y() + slime.get_speed()
            slime.set_y(slime_y)
        if slime.get_y() > player.get_y():
            slime_y = slime.get_y() - slime.get_speed()
            slime.set_y(slime_y)

        draw(player, slime)

        # check hp, game over
        if player.get_hp() == 0:
            lost_text = GG_FONT.render("YOU DIED", 1, "red")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

    pygame.quit()

if __name__ == "__main__":
    main()