import pygame
pygame.init()

screen_title = 'CrossRoads RPG'
screen_width = 800
screen_height = 800
white_color = (255, 255, 255)
black_color = (0, 0, 0)
clock = pygame.time.Clock()

class Game:
    tick_rate = 60
    
    
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.game_window = pygame.display.set_mode((width, height))
        self.game_window.fill(white_color)
        pygame.display.set_caption(title)
    
    def run_game_loop(self):
        is_game_over = False
        while not is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                print(event)
            
            #game_window.blit(player_image,(375, 375))    
                    
            pygame.display.update()
            clock.tick(self.tick_rate)   
            
new_game = Game(screen_title, screen_width, screen_height)
new_game.run_game_loop()           
     
       
#player_image = pygame.image.load('player.png')
#player_image = pygame.transform.scale(player_image, (50, 50))
    
pygame.quit()
quit()