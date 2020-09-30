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
        direction = 0
        player_charater = PlayerCharacter('CrossRoads/player.png', 375, 700, 50, 50)
        enemy0 = EnemyCharacter('CrossRoads/enemy.png', 20, 400, 50, 50)
        
        while not is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                print(event)
             
             
            self.game_window.fill(white_color)    
            player_charater.move(direction, self.width)
            player_charater.draw(self.game_window)
            enemy0.move(self.width)
            enemy0.draw(self.game_window)
            
            
            #game_window.blit(player_image,(375, 375))    
                    
            pygame.display.update()
            clock.tick(self.tick_rate) 
            
class GameObject:
      
      def __init__(self, image_path, x, y, width, height):
          object_image = pygame.image.load(image_path)
          self.image = pygame.transform.scale(object_image, (width, height))
          self.x_pos = x
          self.y_pos = y
          self.width = width
          self.height = height
    
      def draw(self, background):
          background.blit(self.image, (self.x_pos, self.y_pos))
          
class PlayerCharacter(GameObject):
    
    speed = 10
    
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
        
    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.speed
        elif direction < 0:
            self.y_pos += self.speed
        if self.y_pos >= max_height - 20:
            self.y_pos = max_height - 20
        elif self.y_pos <= 20:
            self.y_pos = 20

class EnemyCharacter(GameObject):
    
    speed = 10
    
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
        
    def move(self, max_width):
        if self.x_pos <= 20:
            self.speed = abs(self.speed)
        elif self.x_pos >= max_width - 20:
            self.speed = -abs(self.speed)
        self.x_pos += self.speed
            
          
            
new_game = Game(screen_title, screen_width, screen_height)
new_game.run_game_loop()           
     
       
    
pygame.quit()
quit()