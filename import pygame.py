import pygame  
import sys  
import random
#global_vars
score = 0
#Sprite class   
class Sprite(pygame.sprite.Sprite):  
    def __init__(self, pos):  
        pygame.sprite.Sprite.__init__(self)  
        self.image = pygame.Surface([20, 20])  
        self.image.fill((255, 0, 0))  
        self.rect = self.image.get_rect()  
        self.rect.center = pos  

def generate_new_wall():
    first = random.randint(80, 150)
    second = random.randint(80, 150)

    wall = Sprite([first, second])
    return wall

def setup_game():
    pygame.init()
    

def main():  
    wordfont = pygame.font.SysFont("sans",12)
    clock = pygame.time.Clock()  
    global score
    print(score)
    fps = 50  
    bg = [0, 0, 0]  
    size =[300, 300]  
    first   = random.randint(80, 150)
    second  = random.randint(80, 150)
    screen = pygame.display.set_mode(size)  
    print_test = pygame.Surface(size)
    player = Sprite([50, 60])  
    player.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]  
    player.vx = 5  
    player.vy = 5  
    score = str(score)
    wall = generate_new_wall()
    wall_group = pygame.sprite.Group()  
    wall_group.add(wall)  
    
    player_group = pygame.sprite.Group()  
    player_group.add(player)  
  
    while True:  
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                return False  
        key = pygame.key.get_pressed()  
        for i in range(2):  
            if key[player.move[i]]:  
                player.rect.x += player.vx * [-1, 1][i]  
  
        for i in range(2):  
            if key[player.move[2:4][i]]:  
                player.rect.y += player.vy * [-1, 1][i]  
        screen.fill(bg)  
        screen.blit(print_test,  (150, 150))



        # first parameter takes a single sprite  
        # second parameter takes sprite groups  
        # third parameter is a kill command if true  

        hit = pygame.sprite.spritecollide(player, wall_group, True)  
        if hit:  
        # if collision is detected call a function to destroy  
            # rect  
            player.image.fill((255, 255, 255))
            score = int(score)
            score += 1
            main()

        player_group.draw(screen)  
        wall_group.draw(screen)  
        pygame.display.update()  
        clock.tick(fps)  
    pygame.quit()  
    sys.exit  

setup_game()
main()