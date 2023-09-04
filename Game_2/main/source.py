#Monkey player images by Ekteri
#https://ekteri.itch.io/monkey-ntt-character

#GoldCoin images by morgan3d
#https://opengameart.org/content/spinning-gold-coin

import pygame, os
import engine 
fpsClock = pygame.time.Clock()

# constant variables
display_width = 1280 #1920/1.5
display_height = 720 #1080/1.5 
SCREEN_SIZE = (display_width, display_height)
WIDTH = 14*4
HEIGHT = 17*4
x_player = 0
y_player = ground = 560 
jump_player = 0
gravity = 0.2
FPS = 60
jump = False
speed = 5 
score = 0
live = 3
B_monster_go  = 2
H_monster_go = - 1
game_state = "playing"
player_state = "right"
player_walk = "Stand"
#======================================================================= ANIMATION
# background
background_images = pygame.image.load("main/Background.png")
background_images = pygame.transform.scale(background_images, SCREEN_SIZE)
gameover_image = pygame.image.load("main/gameover.png")
gameover_image = pygame.transform.scale(gameover_image, SCREEN_SIZE)

# player
player_animation = {
    "stand" : engine.Animation([
        pygame.transform.scale(pygame.image.load("main/Monkey_stand-1.png"), (WIDTH, HEIGHT)),
        pygame.transform.scale(pygame.image.load("main/Monkey_stand-2.png"), (WIDTH, HEIGHT)),
        pygame.transform.scale(pygame.image.load("main/Monkey_stand-3.png"), (WIDTH, HEIGHT)),
        pygame.transform.scale(pygame.image.load("main/Monkey_stand-4.png"), (WIDTH, HEIGHT))
    ]),
    "walking" : engine.Animation([
        pygame.transform.scale(pygame.image.load("main/Monkey_walk-1.png"), (WIDTH, HEIGHT)),
        pygame.transform.scale(pygame.image.load("main/Monkey_walk-2.png"), (WIDTH, HEIGHT)),
        pygame.transform.scale(pygame.image.load("main/Monkey_walk-3.png"), (WIDTH, HEIGHT)),
        pygame.transform.scale(pygame.image.load("main/Monkey_walk-4.png"), (WIDTH, HEIGHT)),
        pygame.transform.scale(pygame.image.load("main/Monkey_walk-5.png"), (WIDTH, HEIGHT)),
        pygame.transform.scale(pygame.image.load("main/Monkey_walk-6.png"), (WIDTH, HEIGHT)) 
    ])
}
# coin
coin_animation = engine.Animation([
    pygame.transform.scale(pygame.image.load("main/goldCoin1.png"), (28, 32)),
    pygame.transform.scale(pygame.image.load("main/goldCoin2.png"), (28, 32)),
    pygame.transform.scale(pygame.image.load("main/goldCoin3.png"), (28, 32)),
    pygame.transform.scale(pygame.image.load("main/goldCoin4.png"), (28, 32)),
    pygame.transform.scale(pygame.image.load("main/goldCoin5.png"), (28, 32)),
    pygame.transform.scale(pygame.image.load("main/goldCoin6.png"), (28, 32)),
    pygame.transform.scale(pygame.image.load("main/goldCoin7.png"), (28, 32)),
    pygame.transform.scale(pygame.image.load("main/goldCoin8.png"), (28, 32)),
    pygame.transform.scale(pygame.image.load("main/goldCoin9.png"), (28, 32))
])
coins =[pygame.Rect(800, 580, 28, 32),
        pygame.Rect(460, 390, 28, 32)] # creat frame contain coin (x, y , width, height)
# block
wood_images = pygame.image.load("main/wood.png")
wood_images = pygame.transform.scale(wood_images, (50, 50)) 
woods =[pygame.Rect(600, 560, 50, 45),
        pygame.Rect(200, 510, 50, 45),
        pygame.Rect(450, 430, 50, 45),
        pygame.Rect(1010, 530, 50, 45)] # creat frame contain wood
# heart
heart_image = pygame.image.load("main/heart.png")
heart_images = pygame.transform.scale(heart_image, (30, 30)) 
hearts = [pygame.Rect(150, 0, 30, 30),
          pygame.Rect(180, 0, 30, 30),
          pygame.Rect(210, 0, 30, 30)]
# monster
B_monster_images = pygame.image.load("main/B.png") 
B_monster_images = pygame.transform.scale(B_monster_images, (50, 50)) 
B_monsters = [pygame.Rect(600, 578, 50, 50)]

H_monster_animation =engine.Animation([
    pygame.transform.scale(pygame.image.load("main/H-1.png"), (60, 60)),
    pygame.transform.scale(pygame.image.load("main/H-2.png"), (60, 60)),
    pygame.transform.scale(pygame.image.load("main/H-3.png"), (60, 60)),
    pygame.transform.scale(pygame.image.load("main/H-4.png"), (60, 60))
])
H_monsters = [pygame.Rect(400, 350, 60, 60)]
#======================================================================= INIT
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
font = pygame.font.Font(pygame.font.get_default_font(), 20)
pygame.display.set_caption("Amzing Monkey")
running = True

while running:
    # checking for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            os.system("cls")
            running = False

#======================================================================== MOVING PLAYER
    # Run 
    if game_state == "playing":
        
        new_x_player = x_player 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            new_x_player += speed
            if new_x_player > display_width:
                new_x_player = -1
            player_state = "right"
            player_walk = "walking"
        if keys[pygame.K_LEFT]:
            new_x_player -= speed
            if new_x_player < 0:
                new_x_player = display_width
            player_state = "left"
            player_walk = "walking"
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            player_walk = "stand"

        # print(f"{player_state} ; {player_walk}")

        # horizontal movement

        new_player_rect = pygame.Rect(new_x_player, y_player, WIDTH, HEIGHT)
        x_collision = True

        for w in woods:
            if w.colliderect(new_player_rect): # when the rect touch block
                x_collision = False
                break

        if x_collision:
            x_player = new_x_player
        # Jump 
        new_y_player = y_player
        jump_player += gravity 
        new_y_player += jump_player

        if new_y_player > ground:
            new_y_player = ground
            jump = True

        if keys[pygame.K_SPACE]:
            if jump:
                jump_player = -7
                jump = False

        # vertical movement

        new_y_player_rect = pygame.Rect(x_player, new_y_player, WIDTH, HEIGHT)
        y_collision = True

        # check against woods
        for w in woods:
            if w.colliderect(new_y_player_rect):
                y_collision = False
                jump_player = 0
                if w[1] > new_y_player:
                    y_player = w[1] - HEIGHT 
                    jump = True
                    break

        if y_collision:
            y_player = new_y_player
    #======================================================================== EXTENSION
        # see extension
        player_rect = pygame.Rect(x_player, y_player, WIDTH, HEIGHT)
        for c in coins:
            if c.colliderect(player_rect):
                coins.remove(c)
                score += 1
        for x in B_monsters:
            if x.colliderect(player_rect):
                live -= 1
                x_player = x[0] - 150
                y_player = 100
                jump_player = - 5
        for x in H_monsters:
            if x.colliderect(player_rect):
                live -= 1
                x_player = x[0] - 150
                y_player = 100
                jump_player = - 5
                
    #======================================================================== DRAW 
        # Screen
        screen.blit(background_images,(0,0))

        # information dispkay
            # score
        score_text = font.render("Score: " + str(score), True, (237, 240, 89))
        screen.blit(score_text, (0,0))
            # live
        for l in range(live):
            screen.blit(heart_image, (100 + (l*30) ,0))

        # Extension
        for coin in coins:
            coin_animation.draw(screen, coin.x, coin.y, False, False)
        for wood in woods:
            screen.blit(wood_images, (wood[0], wood[1]))
        # Monster
            # H_monster    
        for monster in H_monsters:
            monster.x += H_monster_go
            if monster.x == 600:
                H_monster_go = -2
            if monster.x == 300:
                H_monster_go = 2
            
            if H_monster_go == 2:
                H_monster_animation.draw(screen, monster.x, monster.y, False, False)
            elif H_monster_go == -2:
                H_monster_animation.draw(screen, monster.x, monster.y, True, False)
            # B_monster
        for monster in B_monsters:
            monster[0] += B_monster_go
            if monster[0] == 1000:
                B_monster_go = -1
            if monster[0] == 650:
                B_monster_go = 1
            
            if B_monster_go == 1:
                screen.blit(pygame.transform.flip(B_monster_images, True, False), (monster[0], monster[1]))
            elif B_monster_go == -1:
                screen.blit(B_monster_images, (monster[0], monster[1]))
            
        # Player
        if player_state == "right":
            player_animation[player_walk].draw(screen, x_player, y_player, False, False)
        elif player_state == "left":
            player_animation[player_walk].draw(screen, x_player, y_player, True, False)
        elif player_state == "stand":
            player_animation[player_walk].draw(screen, x_player, y_player, False, False)
#============================================================================ END GAME
        
        if live == 0:
            game_state = "lose"
            x_player = 500
            screen.blit(gameover_image,(0,0))

        # present screen
        pygame.display.flip()
        pygame.display.update()
        coin_animation.update()
        H_monster_animation.update()
        player_animation[player_walk].update()
        fpsClock.tick(FPS)
    
#quit
pygame.quit()