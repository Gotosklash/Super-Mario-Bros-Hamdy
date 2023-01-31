import pygame, sys


pygame.init()

sound = pygame.mixer.Sound('supermario/smbsong.mp3')
sound.play(loops = -1)

def start():
    with open("gameover.py", "r") as f:
        code = f.read()
    exec(code)
mscreen = pygame.display.set_mode((470,770))

tutorialbg= pygame.image.load("mariotutorial/mariotutorialbg.png")
tutorialbg = pygame.transform.scale(tutorialbg,(470,770))

mariotutorial = pygame.image.load("mariotutorial/mariotutorial.png")
mariotutorial = pygame.transform.scale(mariotutorial,(180,264.15))

tutorial_prompt = pygame.image.load("mariotutorial/tutorial.png")
tutorial_prompt = pygame.transform.scale(tutorial_prompt,(450,407.5))

cont = pygame.image.load("mariotutorial/scoreboard15.png")
cont = pygame.transform.scale(cont,(320,68))

pixel_font = pygame.font.Font('mariobg/Pixeltype.ttf', 30)
start_phrase = pixel_font.render("Press Anywhere to Start",True, (0, 0, 0))
start_blink = 700

# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                sound.stop()
                start()
        
    current_time = pygame.time.get_ticks()
    # blink rate check
    if current_time % start_blink < start_blink / 2:
        # render the text to make it blink
        start_phrase = pixel_font.render("Press Anywhere to Start", False, (0, 0, 0))
    else:
        # render the text as blank
        start_phrase = pixel_font.render("", True, (255, 255, 255))

    mscreen.blit(tutorialbg,(0,0))
    mscreen.blit(mariotutorial, (40, 400))
    mscreen.blit(tutorial_prompt,(50,30))
    mscreen.blit(cont,(74,680))
    mscreen.blit(start_phrase,(125,703))
    # Screen Update
    pygame.display.update()

# quit
pygame.quit()