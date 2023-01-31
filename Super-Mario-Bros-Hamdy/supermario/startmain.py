import pygame, sys
import time
from pygame.locals import QUIT
import pygame.mixer


# Next Page
def game():
	with open("tutorial.py", "r") as f:
		code = f.read()
	exec(code)

pygame.init()
pygame.mixer.init()
mscreen= pygame.display.set_mode((470, 770))
clock = pygame.time.Clock()

fps = clock.get_fps()
pygame.display.set_caption(f' Super Mario Bros (Hamdy Edition) {fps} FPS')
icon = pygame.image.load('mariobg/marioicon.png')
pygame.display.set_icon(icon)

#mario song
def mariosong():
	global sound
	sound = pygame.mixer.Sound('supermario/smbsong.mp3')
	sound.play(loops = -1)

#bg img
groundimg = pygame.image.load('mariobg/marioground.png')
groundimg = pygame.transform.scale(groundimg, (470, 40))

skyimg = pygame.image.load('mariobg/mariobg3.png')
skyimg = pygame.transform.scale(skyimg,(470,770))

logoimg = pygame.image.load('mariobg/smbmariologo2.png')
logoimg = pygame.transform.scale(logoimg,(590,585.56))

pygame.font.get_fonts()
pixel_font = pygame.font.Font('mariobg/Pixeltype.ttf', 30)
start_phrase = pixel_font.render("Press Anywhere to Continue",True, (0, 0, 0))

start_blink = 700

mariosong()

# Main Game Loop
running = True
while running:
	for event in pygame.event.get():
			if event.type == QUIT:
					running = False
					pygame.quit()
					sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					sound.stop()
					game()

    
	current_time = pygame.time.get_ticks()
    # blink rate check
	if current_time % start_blink < start_blink / 2:
		# render the text to make it blink
		start_phrase = pixel_font.render("Press Anywhere to Start", False, (0, 0, 0))
	else:
		# render the text as blank
		start_phrase = pixel_font.render("", True, (255, 255, 255))
	
	mscreen.blit(skyimg,(0,0))
	mscreen.blit(groundimg,(0,730))
	mscreen.blit(logoimg,(-60,-50))
	mscreen.blit(start_phrase, (124, 20))
	
	# Display update
	pygame.display.update()
	clock.tick(fps)

# Quit
pygame.quit()