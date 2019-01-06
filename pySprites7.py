import pygame

class Player(pygame.sprite.Sprite):
    '''This class defines the sprite for the player'''
    def __init__(self, screen):
        '''This initializer takes a screen surface as a
        parameter. It loads the four different player images that will change 
        depending on going left, right, up or down and it positions the 
        player sprite on the bottom of the screen. It also handles the movement 
        when the player uses the arrow keys and when the player is on the lilypads.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
                
        self.image = pygame.image.load("goomba_back.png")
        self.__b_image = pygame.image.load("goomba_back.png")
        self.__f_image = pygame.image.load("goomba_front.png")
        self.__l_image = pygame.image.load("goomba_left.png")
        self.__r_image = pygame.image.load("goomba_right.png")
        self.rect = self.image.get_rect()    

        self.rect.left = screen.get_width()/2

        self.rect.top = 420
        self.__screen = screen
        self.__lilypad = False
        self.__lilypad2 = False
        self.__up = False
        self.__down = False
        self.__left = False
        self.__right = False
    
    def go_up(self):
        self.__up = True
        
    def go_down(self):
        self.__down = True    
    
    def go_left(self):
        self.__left = True    
        
    def go_right(self):
        self.__right = True
        
    def back_image(self): 
        self.image = self.__b_image
    
    def front_image(self): 
        self.image = self.__f_image   
        
    def left_image(self): 
        self.image = self.__l_image 
        
    def right_image(self): 
        self.image = self.__r_image  
    
    def get_bottom(self):
        return self.rect.bottom
    
    def starting_zone(self, screen):
        self.rect.left = screen.get_width()/2
        self.rect.top = 420
    
    def moveon_lilypad(self):
        self.__lilypad = True
        
    def moveon_lilypad2(self):
        self.__lilypad2 = True
        
    def off_lilypad(self):
        self.__lilypad = False

    def off_lilypad2(self):
        self.__lilypad2 = False
        
    def update(self):
        '''This method will be called automatically to reposition the
        player sprite on the screen.'''
        if self.__up == True and self.rect.bottom > 40: 
            self.rect.top -= 15
            self.__up = False
            
        if self.__down == True and self.rect.bottom < 475: 
            self.rect.top += 15
            self.__down = False   
            
        if self.__left == True and self.rect.right > 40: 
            self.rect.left -= 15
            self.__left = False 
        
        if self.__right == True and self.rect.right < 640: 
            self.rect.left += 15
            self.__right = False         

        if self.__lilypad == True and self.rect.right < 640: 
            self.rect.right += 2
            
        if self.__lilypad2 == True and self.rect.left > 0: 
            self.rect.right -= 4        
        
        # Check if we have reached the right of the screen.
        # If not, then keep moving the player in the same x direction.

class Rockets(pygame.sprite.Sprite):
    '''This class defines the sprite for the rockets'''
    def __init__(self, screen, row, column, level):
        '''This initializer takes a screen, row, column and level as a
        parameter. It loads the rocket image, depending on the row and column it 
        will position it in different areas and depending on the level it will 
        decide how many rockets to make. '''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        self.image1 = pygame.image.load("bullet_billv1.png")
        self.image2 = pygame.image.load("bullet_billv2.png")
        self.image3 = pygame.image.load("bullet_billv3.png") 
        self.__level = level
        self.__screen = screen
        self.__dx = -2        
        
        if self.__level == 1:
            self.image = self.image1
            self.rect = self.image.get_rect()             
            self.rect.bottom = 405
            if column == 0:
                self.rect.right = 760
            else:
                self.rect.right = 1150
        if self.__level == 2: 
            self.image = self.image2
            self.rect = self.image.get_rect()             
            if row == 0:
                self.rect.bottom = 400
            elif row == 1:
                self.rect.bottom = 340
            if column == 0:
                self.rect.right = 760		            
            elif column == 1:
                self.rect.right = 1150 
        if self.__level >= 3: 
            self.image = self.image3
            self.rect = self.image.get_rect()             
            if row == 0:
                self.rect.bottom = 405
            elif row == 1:
                self.rect.bottom = 362
            elif row == 2:
                self.rect.bottom = 319                
            if column == 0:
                self.rect.right = 760
            else:
                self.rect.right = 1150 
            
    
        
    def update(self):
        '''This method will be called automatically to reposition the
        rocket sprites on the screen.'''
        # Check if we have reached the the left side of the screen
        # If not, then keep moving the player in the same x direction.
        
        if self.__level == 1:
            if self.rect.right <= 0:
                self.rect.right = 950     
        if self.__level == 2:
            if self.rect.right <= 0  and self.rect.bottom == 400:
                self.rect.right = 760
            elif self.rect.right <= 0 and self.rect.bottom == 340:
                self.rect.right = 1150 
        if self.__level >= 3:
            if self.rect.right <= 0  and self.rect.bottom == 405:
                self.rect.right = 760
            elif self.rect.right <= 0 and self.rect.bottom == 362:
                self.rect.right = 1150    
            elif self.rect.right <= 0 and self.rect.bottom == 319:
                self.rect.right = 1300              
                
        self.rect.right += self.__dx
        
class Lilypads(pygame.sprite.Sprite):
    '''This class defines the sprite for the lilypads'''
    def __init__(self, screen, row, column, level):
        '''This initializer takes a screen, row, column and level as a
        parameter. It loads the lilypads image, depending on the row and column it 
        will position it in different areas and depending on the level it will 
        decide how many lilypads to make. '''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Define the image attributes for a black rectangle.        
        self.image1 = pygame.image.load("lily_padv1.png") 
        self.image2 = pygame.image.load("lily_padv2.png")
        self.image3 = pygame.image.load("lily_padv3.png")
        self.__screen = screen
        self.__dx = 2        
        self.__level = level
        
        if self.__level == 1: 
            self.image = self.image1
            self.rect = self.image.get_rect()   
            self.rect.bottom = 205
            if column == 0:
                self.rect.right = -60
            elif column == 1:
                self.rect.right = -450  
                
        if self.__level == 2: 
            self.image = self.image2
            self.rect = self.image.get_rect()              
            if row == 0:
                self.rect.bottom = 205
            elif row == 1:
                self.rect.bottom = 138
            if column == 0:
                self.rect.right = -60
            elif column == 1:
                self.rect.right = -120  
            elif column == 2:
                self.rect.right = -360
            elif column == 3:
                self.rect.right = -420
                
        if self.__level == 3: 
            self.image = self.image3
            self.rect = self.image.get_rect()              
            if row == 0:
                self.rect.bottom = 205
            if row == 1:  
                self.rect.bottom = 160
            if row == 2:  
                self.rect.bottom = 115            
            if column == 0 and row == 1:
                self.rect.left = 700
            elif column == 0 and not row == 1: 
                self.rect.right = -60
            if column == 1 and row == 1:
                self.rect.left = 745
            elif column == 1 and not row == 1:
                self.rect.right = -105  
            if column == 2 and row == 1:
                self.rect.left = 960
            elif column == 2 and not row == 1:
                self.rect.right = -360
            if column == 3 and row == 1:
                self.rect.left = 1005
            elif column == 3 and not row == 1:
                self.rect.right = -405  
         
                    
    def update(self):
        '''This method will be called automatically to reposition the
        lilypad sprites on the screen.'''
        if self.__level == 1: 
            if self.rect.left >= 640:
                self.rect.right = -60
                
        if self.__level == 2: 
            if self.rect.left >= 640 and self.rect.bottom == 205:
                self.rect.right = -60
            elif self.rect.left >= 640 and self.rect.bottom == 138:
                self.rect.right = -120  
                
        if self.__level >= 3: 
            if self.rect.left >= 640 and self.rect.bottom == 205:
                self.rect.right = -60
            elif self.rect.right <= 0 and self.rect.bottom == 160:
                self.rect.left = 700            
            elif self.rect.left >= 640 and self.rect.bottom == 115:
                self.rect.right = -180                  
                
        
        if self.__level >= 3 and self.rect.bottom == 160:
            self.rect.right -= self.__dx
        else:
            self.rect.right += self.__dx
        
        
class Water(pygame.sprite.Sprite):
    '''This class defines the sprite for the water'''
    def __init__(self, screen):
        '''This initializer takes a screen surface. It uploads an image.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        self.image = pygame.image.load("water22.png")
        self.image = self.image.convert()
        self.__screen = screen
        
        # Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.right = 640
        self.rect.bottom = 210
    def update(self):
        '''This method allows the water sprite to scroll to get the water flow effect'''
        if self.rect.left < 0: 
            self.rect.right += 2
        else:
            self.rect.right = 640
        
class Road(pygame.sprite.Sprite):
    '''This class defines the sprite for the road'''
    def __init__(self, screen):
        '''This initializer takes a screen surface. It takes an image and then
        it is placed on the screen.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        self.image = pygame.image.load("road.png")
        self.image = self.image.convert()
         
        # Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.bottom = 410
        
class Grass(pygame.sprite.Sprite):
    '''This class defines the sprite for the grass'''
    def __init__(self, screen, y_position, image):
        '''This initializer takes a screen surface, and y position, and the image as
        parameters. It uses a different image and y_position depending on which grass zone.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        grass1 = pygame.image.load("grass1.png")
        grass2 = pygame.image.load("grass2.png")        
         
        # Our endzone sprite will be a 1 pixel wide black line.
        if image == 1:
            self.image = grass1
        else:
            self.image = grass2
            
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.bottom = y_position
        
class ScoreKeeper(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score.'''
    def __init__(self):
        '''This initializer loads the system font "Arial", and
        sets the starting score to 0:0'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        self.__font = pygame.font.SysFont("Font.ttf", 30)
        self.__level = 1
        self.__lives = 3
    
    def death(self):
        '''This method takes a life away from the player'''
        self.__lives -= 1
    
    def level_up(self):
        '''This method adds one to the score for the player'''
        self.__level += 1
        self.__levelup = True 
    
    def get_level(self):
        '''This method returns the level of the player'''
        return self.__level 
    
    def get_lives(self):
        '''This method returns the lives of the player'''
        return self.__lives
 
    def update(self):
        '''This method will be called automatically to display 
        the current score at the top of the game window.'''
        message = "   Level: %d                                              Lives: %d" %\
                (self.__level,self.__lives)
        self.image = self.__font.render(message, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (300, 10)
        
        