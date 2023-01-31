import pygame
import random
import time
import pygame.mixer

def gameover():
    with open("gameover.py", "r") as f:
        code1 = f.read()
    exec(code1)

def lvsound():
    global sound
    sound = pygame.mixer.Sound("supermario/bosssong.mp3")
    sound.play(loops = -1)

def die():
    diesound = pygame.mixer.Sound("supermario/smb_mariodie.wav")
    diesound.play()

# Initialize Pygame and create a window
pygame.init()
mscreen = pygame.display.set_mode((470, 770))

# Load the Mario image
mario_image = pygame.image.load("spirit/8Bit_Mario.png")
mario_image = pygame.transform.scale(mario_image,(50, 60))

# Mario Rect and Spawn
mario_rect = mario_image.get_rect()

mario_rect.x = 470/2
mario_rect.y = 650

meteorsimg = pygame.image.load("marioenem/mariometeor.png")
meteorsimg = pygame.transform.scale(meteorsimg,(60,60))


# Browser Background
browserbg = pygame.image.load("mariobg/browserbg.png")
browserbg = pygame.transform.scale(browserbg, (470,770))
browsergr = pygame.image.load("mariobg/groundimg2.png")
browsergr = pygame.transform.scale(browsergr, (470,40))

# Scoreboard
scoreboard = pygame.image.load("supermario/scoreboard2.png")
scoreboard = pygame.transform.scale(scoreboard, (180,90))

# Logo
logoimg = pygame.image.load('mariobg/smbmariologo2.png')
logoimg = pygame.transform.scale(logoimg,(295,292.78))
# Meteor spawn
meteor_spawn = 275

# Store meteor positions and speeds
meteors = []

# Frame Counter
meteor_frame= 0

# Jumping constant with Physics :(
gravity = 0.5
jump_speed = -7

# text
pixel_font = pygame.font.Font('mariobg/Pixeltype.ttf', 30)
time = 0
global score
score = 0

lvsound()
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
     
    jump_speed += gravity
    mario_rect.y += jump_speed
    # Score incrament
    score += 1
    # Score output
    score_text = pixel_font.render("Score: " + str(score), True, (255,255,255))
        
    # Mario Movements
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mario_rect.x -= 2
    if keys[pygame.K_RIGHT]:
        mario_rect.x += 2
    if keys[pygame.K_UP]:
        jump_speed = -5
    if keys[pygame.K_DOWN]:
        mario_rect.y += 1.5
    
    # Restrict Mario's movement (window)
    if mario_rect.x < 0:
        mario_rect.x = 0
    if mario_rect.x > 470 - 41:
        mario_rect.x = 470 - 41
    if mario_rect.y < 0:
        mario_rect.y = 0
    if mario_rect.y > 670: 
        mario_rect.y = 670
        jump_speed = 0


    # time for meteor
    time += 1/60
    
    # Check if it's time to increase the spawn rate
    if time >= 7:
        meteor_spawn -= 8
        time = 0

    # Meteor Code
    meteor_frame += 1
    if meteor_frame % meteor_spawn == 0:
        x_pos = random.randint(0, 400)
        y_pos = -10
        meteors.append((x_pos, y_pos))
        
    # Update the positions of all meteors
    for i in range(len(meteors)):
        x_pos, y_pos = meteors[i]
        y_pos += 2
        meteors[i] = (x_pos, y_pos)
    
    for x_pos, y_pos in meteors:
        meteors_rect = meteorsimg.get_rect()
        meteors_rect.x = x_pos
        meteors_rect.y = y_pos
        #if meteors_rect >= 770:
            
        if mario_rect.colliderect(meteors_rect):
            sound.stop()
            die()
            pygame.time.wait(3000)
            gameover()
        
 
    # Blit commands
    mscreen.blit(browserbg,(0,0))
    mscreen.blit(mario_image,mario_rect)
    mscreen.blit(browsergr,(0,730))
    

    for x_pos, y_pos in meteors:
        mscreen.blit(meteorsimg,(int(x_pos),int(y_pos)))
    mscreen.blit(scoreboard,(270,0))
    mscreen.blit(score_text,(290,37))
    mscreen.blit(logoimg,(-30,-90))
    
    # Display Update
    pygame.display.update()

# Exit code
pygame.quit()
