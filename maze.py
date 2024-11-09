import pygame
import sys
#game settings
TILE_SIZE = 50
# Create maze (1 = valid path, 0 = wall)
maze = [
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
ROWS, COLS = len(maze), len(maze[0])
WIDTH, HEIGHT = COLS * TILE_SIZE, ROWS * TILE_SIZE
FPS = 60
# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
# setting Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Maze Game")
clock = pygame.time.Clock()
# setting Player
player_pos = [0, 0]

def draw_maze(screen, maze):
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if maze[row][col] == 1 else BLACK
            pygame.draw.rect(screen, color, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    pygame.draw.rect(screen, GREEN, ((COLS-1) * TILE_SIZE, (ROWS-1)* TILE_SIZE, TILE_SIZE, TILE_SIZE))
def draw_player(screen, position):
     pygame.draw.circle(screen, (0, 0, 255), (position[1] * TILE_SIZE+TILE_SIZE/2,  position[0] * TILE_SIZE+TILE_SIZE/2),  TILE_SIZE/2)
# move Player
def move_player(maze, player_pos, direction):
    x, y = player_pos
    if direction == "up" and x > 0 and maze[x-1][y] == 1:
        player_pos[0] -= 1
    elif direction == "down" and x < ROWS - 1 and maze[x+1][y] == 1:
        player_pos[0] += 1
    elif direction == "left" and y > 0 and maze[x][y-1] == 1:
        player_pos[1] -= 1
    elif direction == "right" and y < COLS - 1 and maze[x][y+1] == 1:
        player_pos[1] += 1

running = True
while running:
    screen.fill(BLACK)
    draw_maze(screen, maze)
    draw_player(screen, player_pos)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_player(maze, player_pos, "up")
            elif event.key == pygame.K_DOWN:
                move_player(maze, player_pos, "down")
            elif event.key == pygame.K_LEFT:
                move_player(maze, player_pos, "left")
            elif event.key == pygame.K_RIGHT:
                move_player(maze, player_pos, "right")
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
