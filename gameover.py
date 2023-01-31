import pygame
import atma
pygame.init()

def gameover():
    with open("atma.py", "r") as f:
        code1 = f.read()
    exec(code1)

# Window size
mscreen = pygame.display.set_mode((470, 770))

pixel_font = pygame.font.Font('mariobg/Pixeltype.ttf', 50)
gameover_text = pixel_font.render("GAME OVER", True, (255,255,255))

pixel_font2 = pygame.font.Font('mariobg/Pixeltype.ttf', 30)
score_text = pixel_font2.render("Score: " + str(atma.score), True, (255,255,255))


start_phrase = pixel_font2.render("Press Anywhere to Restart",True, (255, 255, 255))

sound = pygame.mixer.Sound("supermario/smb_gameover.wav")
sound.play()


# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.time.wait(2000)
            if event.button == 1:
                sound.stop()
                gameover()


    
    mscreen.fill((0,0,0))
    mscreen.blit(gameover_text,(157,335))
    mscreen.blit(score_text,(187,370))
    mscreen.blit(start_phrase,(115,700))

    # Screen Update
    pygame.display.update()

# quit
pygame.quit()
