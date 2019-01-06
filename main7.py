"""
Author: Daniel Cho

Date: May 31, 2017

Description: This program is Frogger, the player must cross to the other side
of the screen by dodging all of the rockets and then going on the lilypads to 
prevent sinking in the water.
"""
# I - IMPORT AND INITIALIZE
import pygame, pySprites7
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((640, 480))

def introduction():
    '''This function shows the title screen before the game starts and waits for 
    the player to hit a key before starting.'''  
    introduction = pygame.image.load("goomba_cross.png")
    introduction = introduction.convert()
    screen.blit(introduction, (0,0))
    pygame.display.flip()
    
    game = False
    while game == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = True
            elif event.type == pygame.KEYDOWN:
                game = True
 
def main():
    '''This function defines the 'mainline logic' for the Goomba-Cross game. 
    It loads all the entites and handles all the events that happen in the game'''
      
    # DISPLAY
    pygame.display.set_caption("Goomba-Cross")
    
    # ENTITIES
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    
    grass1 = pygame.image.load("grass1.png")
    grass2 = pygame.image.load("grass2.png")
    rocketGroup1 = []
    rocketGroup2 = []
    rocketGroup2 = []
    lilypadGroup1 = []
    lilypadGroup2 = []
    lilypadGroup3 = []
    
    # Sprites for: ScoreKeeper label, End Zones, Ball, and Player
    startzone = pySprites7.Grass(screen, 480, 1)
    midzone = pySprites7.Grass(screen, 270, 2)
    endzone = pySprites7.Grass(screen, 70, 1)
    water = pySprites7.Water(screen)
    road = pySprites7.Road(screen)
    player = pySprites7.Player(screen)
    scorekeeper = pySprites7.ScoreKeeper()
    allSprites = pygame.sprite.OrderedUpdates(startzone, road, midzone, water, endzone,  \
                                         player, scorekeeper)   
    
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    win_sound = pygame.mixer.Sound("music.wav")
    win_sound.set_volume(0.3)
    die_sound = pygame.mixer.Sound("music.wav")
    die_sound.set_volume(0.3)
    
   
    #creates the rockets for level 1
    rockets1 = []
    for row in range(1):
        for column in range(2):
            rocket1 = pySprites7.Rockets(screen, row, column, 1)
            rockets1.append(rocket1) 
            rocketGroup1 = pygame.sprite.Group(rockets1)
            
    #creates the lilypads for level 1        
    lilypads1 = []
    for row in range(1):
        for column in range(2):
            lilypad1 = pySprites7.Lilypads(screen, row, column, 1)
            lilypads1.append(lilypad1)  
            lilypadGroup1 = pygame.sprite.Group(lilypads1)
            
    #creates the rockets for level 2         
    rockets2 = []
    for row in range(2):
        for column in range(2):
            rocket2 = pySprites7.Rockets(screen, row, column, 2)
            rockets2.append(rocket2) 
            rocketGroup2 = pygame.sprite.Group(rockets2)      
            
    #creates the lilypads for level 2        
    lilypads2 = []
    for row in range(2):
        for column in range(4):
            lilypad2 = pySprites7.Lilypads(screen, row, column, 2)
            lilypads2.append(lilypad2)  
            lilypadGroup2 = pygame.sprite.Group(lilypads2)  
            
    #creates the rockets for level 3        
    rockets3 = []
    for row in range(3):
        for column in range(2):
            rocket3 = pySprites7.Rockets(screen, row, column, 3)
            rockets3.append(rocket3) 
            rocketGroup3 = pygame.sprite.Group(rockets3)
            
    #creates the lilypads for level 3        
    lilypads3 = []
    for row in range(3):
        for column in range(4):
            lilypad3 = pySprites7.Lilypads(screen, row, column, 3)
            lilypads3.append(lilypad3)  
            lilypadGroup3 = pygame.sprite.Group(lilypads3)  
                        

    # ASSIGN 
    clock = pygame.time.Clock()
    keepGoing = True
    
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)
     
    # LOOP
    while keepGoing:
         
        # TIME
        clock.tick(45)
         
        # EVENT HANDLING: The player uses left and right to change the direction of the player
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.left_image() 
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.right_image() 
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.back_image() 
                    player.go_up()
                if event.key == pygame.K_DOWN:
                    player.front_image() 
                    player.go_down()     
        
        #checks for level 1 and spawns the level 1 rocket and lilypads
        if scorekeeper.get_level() == 1:
            allSprites = pygame.sprite.OrderedUpdates(startzone, road, midzone, water, endzone, lilypadGroup1, rocketGroup1, \
        
                                                      player, scorekeeper)
        #checks for level 2 and spawns the level 2 rocket and lilypads
        if scorekeeper.get_level() == 2:
            rocketGroup1 = []
            lilypadGroup1 = []
            allSprites = pygame.sprite.OrderedUpdates(startzone, road, midzone, water, endzone, lilypadGroup2, rocketGroup2, \
                                                      player, scorekeeper) 
        #checks for level 3 and spawns the level 3 rocket and lilypads    
        if scorekeeper.get_level() == 3:
            rocketGroup2 = []
            lilypadGroup2 = []
            allSprites = pygame.sprite.OrderedUpdates(startzone, road, midzone, water, endzone, lilypadGroup3, rocketGroup3, \
                                                      player, scorekeeper)  
        
        #checks if the rocket kills the player    
        if pygame.sprite.spritecollide(player, rocketGroup1, False) or pygame.sprite.spritecollide(player, rocketGroup2, False)\
           or pygame.sprite.spritecollide(player, rocketGroup3, False):
            scorekeeper.death()
            player.starting_zone(screen)
            die_sound.play()
        
        #checks if the player sinks in the water     
        if water.rect.colliderect(player.rect) \
           and not pygame.sprite.spritecollide(player, lilypadGroup1, False) and not pygame.sprite.spritecollide(player, lilypadGroup2, False)\
           and not pygame.sprite.spritecollide(player, lilypadGroup3, False) and not midzone.rect.colliderect(player.rect) and\
           (not endzone.rect.colliderect(player.rect) or player.get_bottom() == 100):
            scorekeeper.death()
            player.starting_zone(screen) 
            die_sound.play()
            
        #checks if the player is on a lilypad, makes sure that the player is within the water before getting on the lilypad and moves the player on the lilypad until the player is off
        if (pygame.sprite.spritecollide(player, lilypadGroup1, False) or pygame.sprite.spritecollide(player, lilypadGroup2, False) \
           or pygame.sprite.spritecollide(player, lilypadGroup3, False)) and (player.get_bottom() < 220 and player.get_bottom() > 85):
            player.moveon_lilypad()
        else: 
            player.off_lilypad()
    
        #checks if the player has reached the endzone and then levels the player up and puts the player back in the beginning of the game.
        if player.get_bottom() <= 55:   
            if endzone.rect.colliderect(player.rect):
                scorekeeper.level_up()            
                player.starting_zone(screen)
                win_sound.play()
                
        #checks if the player is on the reverse lilypad and moves the player until it is off the lilypad        
        if scorekeeper.get_level() >= 3 and pygame.sprite.spritecollide(player, lilypadGroup3, False) and (player.get_bottom() == 160 or player.get_bottom() == 145):
            player.moveon_lilypad2()
        else:
            player.off_lilypad2()
        
        #makes sure that the player does not move when it is inbetween the reverse lilypad and regular lilypad
        if scorekeeper.get_level() >= 3 and (player.get_bottom() == 130 or player.get_bottom() == 175):
            player.off_lilypad()
            player.off_lilypad2()
                
            
        # REFRESH SCREEN
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)       
        pygame.display.flip()
        
        #displays a gameover screen before closing
        if scorekeeper.get_lives() <= 0:
            allSprites.clear(screen, background) 
            gameover = pygame.image.load("gameover.png")
            gameover = gameover.convert()
            screen.blit(gameover, (0, 0))
            pygame.display.flip()
            keepGoing = False   
            
    # Unhide the mouse pointer
    pygame.mouse.set_visible(True)
     
    # Close the game window
    pygame.time.delay(1000)
    pygame.quit()     
         
# Call the main function
introduction()
main()        
