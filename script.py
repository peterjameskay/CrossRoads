import pygame
pygame.init()

screen_title = 'CrossRoads RPG'
screen_width = 800
screen_height = 800
white_color = (255, 255, 255)
black_color = (0, 0, 0)
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)

class Game:
    
    tick_rate = 60

    
    def __init__(self, image_path, title, width, height):
        self.width = width
        self.height = height
        self.game_window = pygame.display.set_mode((width, height))
        self.game_window.fill(white_color)
        pygame.display.set_caption(title)
        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))
    
    def run_game_loop(self, level):
        is_game_over = False
        did_win = False
        direction = 0
        player_charater = PlayerCharacter('player.png', 375, 700, 50, 50)
        enemy0 = EnemyCharacter('enemy.png', 20, 400, 50, 50)
        enemy0.speed *= level
        enemy1 = EnemyCharacter('enemy.png', 20, 200, 50, 50)
        enemy1.speed *= level
        enemy2 = EnemyCharacter('enemy.png', 20, 600, 50, 50)
        enemy2.speed *= level
        treasure = GameObject('treasure.png', 375, 50, 50, 50)
        
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
            self.game_window.blit(self.image, (0,0))
            treasure.draw(self.game_window)    
            player_charater.move(direction, self.height)
            player_charater.draw(self.game_window)
            enemy0.move(self.width)
            enemy0.draw(self.game_window)
            
            if level > 2.5:
                enemy1.move(self.width)
                enemy1.draw(self.game_window)
            if level > 5:
                enemy2.move(self.width)
                enemy2.draw(self.game_window)
            
            if player_charater.detect_collision(enemy0):
                is_game_over = True
                did_win = False
                text = font.render('You Lose. Try Again.', True, black_color)
                self.game_window.blit(text, (300, 350))
                pygame.display.update()
                clock.tick(1)
                break
            elif player_charater.detect_collision(enemy1):
                is_game_over = True
                did_win = False
                text = font.render('You Lose. Try Again.', True, black_color)
                self.game_window.blit(text, (300, 350))
                pygame.display.update()
                clock.tick(1)
                break
            elif player_charater.detect_collision(enemy2):
                is_game_over = True
                did_win = False
                text = font.render('You Lose. Try Again.', True, black_color)
                self.game_window.blit(text, (300, 350))
                pygame.display.update()
                clock.tick(1)
                break            
            elif player_charater.detect_collision(treasure):
                is_game_over = True
                did_win = True
                text = font.render('You Won!', True, black_color)
                self.game_window.blit(text, (300, 350))
                pygame.display.update()
                clock.tick(1)
                break
            
            
            #game_window.blit(player_image,(375, 375))    
                    
            pygame.display.update()
            clock.tick(self.tick_rate)
        if did_win:
            self.run_game_loop(level + 0.5)
        else:
            return 
            
            
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
        if self.y_pos >= max_height - 40:
            self.y_pos = max_height - 40
        elif self.y_pos <= 20:
            self.y_pos = 20
            
    def detect_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height - 10:
            return False
        elif self.y_pos + self.height - 10 < other_body.y_pos:
            return False
        if self.x_pos > other_body.x_pos + other_body.width - 10:
            return False
        elif self.x_pos + self.width - 10 < other_body.x_pos:
            return False
        return True

class EnemyCharacter(GameObject):
    
    speed = 3
    
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
        
    def move(self, max_width):
        if self.x_pos <= 20:
            self.speed = abs(self.speed)
        elif self.x_pos >= max_width - 40:
            self.speed = -abs(self.speed)
        self.x_pos += self.speed
            
          
            
new_game = Game('background.png', screen_title, screen_width, screen_height)
new_game.run_game_loop(1)           
     
       
    
pygame.quit()
quit()