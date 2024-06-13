import pygame
import random

pygame.init()


BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (100,100,100)


WIDTH,HEIGHT = 1000,1000
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 20

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()





def draw_grid(positions):

    for position in positions:
        col,row = position
        top_left = (col*TILE_SIZE,row*TILE_SIZE)
        pygame.draw.rect(screen, BLACK, (*top_left,TILE_SIZE,TILE_SIZE))



    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen,BLACK,(0,row*TILE_SIZE),(WIDTH,row*TILE_SIZE))

    for column in range(GRID_WIDTH):
        pygame.draw.line(screen,BLACK,(column*TILE_SIZE,0),(column*TILE_SIZE,HEIGHT))


   

def gen(num):
    return set([(random.randrange(0,GRID_HEIGHT),random.randrange(0,GRID_WIDTH)) for _ in range(num)])


def issafe(col,row):
    if (col>=0 and col<GRID_WIDTH and row>=0 and row<GRID_HEIGHT): 
        return True
    else:
        return False

def get_neighbors(pos):
        col,row = pos
        neighbors = []
        for i in range(-1,2):
            for j in range(-1,2):
                if not (i==0 and j==0):
                    if issafe(col+i,row+j):
                        neighbors.append((col+i,row+j))
        return neighbors

   


def update_life(positions):
    new_positions = set()
    all_neighbors = set()

    for position in positions:
        neighbors = get_neighbors(position)
        all_neighbors.update(neighbors)
        neighbors = list(filter(lambda x : x in positions , neighbors))
        if len(neighbors) in [2,3]:
            new_positions.add(position)

    for position in all_neighbors:
        neighbors = get_neighbors(position)
        neighbors = list(filter(lambda x : x in positions , neighbors))
        if len(neighbors) == 3:
            new_positions.add(position)
    return new_positions
        




def main():
    running = True
    positions = set()
    playing = False
    while running:
        clock.tick(FPS)

        pygame.display.set_caption("PLaying" if playing else "Paused")
        
        if playing:
            positions = update_life(positions)  


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                col = x//TILE_SIZE
                row = y//TILE_SIZE

                pos = (col,row)

                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing
                
                if event.key == pygame.K_c:
                    positions = set()
                    playing = False

                if event.key == pygame.K_g:
                    poses = gen(random.randrange(4,10)*GRID_WIDTH)
                    positions = poses
        
        

        screen.fill(WHITE)
        draw_grid(positions)
        pygame.display.update()
        
      

        


    

    pygame.quit()


if __name__== "__main__":
    main()

