import pygame
# import pygame._view
from pygame import *
import random
from flood import flood
from utilities import *
from drought import create_drought

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
display.set_caption('Flood-it!')

#declare global variables
flooded_list = None
color_of_tile = None
is_done = False
update = False
for_restart = False
movecount = None
btncol = None


keycolors = { K_a: "pink", K_s: "violet", K_d: "yellow",
              K_z: "red", K_x: "olive", K_c: "blue" }

def button_rect(btn):
    coord = btn['position']
    return pygame.Rect(coord[0], coord[1], 32, 32)

def game_over(png_file):
    shade = pygame.Surface(SCREEN_SIZE)
    shade.fill([0, 0, 0])
    shade.set_alpha(200)
    screen.blit(shade, [0, 0])
    imggameover = pygame.image.load(png_file)
    picture_size = (320,240)
    picture_tiles = [pygame.Rect((0,0), picture_size),
                     pygame.Rect((320,0), picture_size),
                     pygame.Rect((0,240), picture_size),
                     pygame.Rect((320,240), picture_size)]
    rectangle = picture_tiles[random.randint(0, 3)]
    screen.blit(imggameover, [64, 104], rectangle)
    pygame.display.update()

def initialize():
    global flooded_list
    global color_of_tile
    global movecount
    global for_restart
    global btncol
    flooded_list = list()
    color_of_tile = dict()
    movecount = 0
    for_restart = False

    screen.fill(0) #color screen black

    #fills the grid with randomly colored tiles
    for i in range(14):
        for j in range(14):
            X = STEP_SIZE*i
            Y = STEP_SIZE*j
            tile = pygame.Surface(TILE_SIZE)
            color = colors[random.randint(0, 5)]
            tile.fill(rgb[color])
            color_of_tile[(X,Y)] = color
            screen.blit(tile, [X, Y])

    flooded_list.append((0,0))

    # This is the function the students will write. -Jeremy
    flood(color_of_tile, flooded_list)

    tile = pygame.Surface(TILE_SIZE)
    tile.fill(rgb[color_of_tile[(0,0)]])
    for i in range(len(flooded_list)):
        screen.blit(tile, flooded_list[i])
    pygame.display.update()

    # render controls
    # button initialization
    btncol = [dict(), dict(), dict(), dict(), dict(), dict()]

    # button initialization, color and position
    btncol[0] = { 'color': rgb["pink"], 'position': (512, 21) }
    btncol[1] = { 'color': rgb["violet"], 'position': (512, 95) }
    btncol[2] = { 'color': rgb["yellow"], 'position': (512, 169) }
    btncol[3] = { 'color': rgb["red"], 'position': (512, 243) }
    btncol[4] = { 'color': rgb["olive"], 'position': (512, 317) }
    btncol[5] = { 'color': rgb["blue"], 'position': (512, 391) }

    for i in range(len(btncol)):
        pygame.draw.circle(screen, btncol[i]['color'],
                           (btncol[i]['position'][0]+16,
                            btncol[i]['position'][1]+16),
                           16)
    pygame.display.update()


initialize()

while is_done == False:

    for e in event.get():
        color = None

        if e.type == MOUSEBUTTONDOWN:
            for i in range(len(btncol)):
                if button_rect(btncol[i]).collidepoint(e.pos):
                    color = colors[i]
        elif e.type == QUIT:
            is_done = True
        elif e.type == KEYUP:
            update = True
            if e.key == K_ESCAPE:
                is_done = True
            elif e.key == K_r:
                initialize()
            elif e.key in keycolors:
                color = keycolors[e.key]

        if color != None and movecount < 25:
            if not for_restart:
                movecount += 1
                tile = pygame.Surface(TILE_SIZE)
                tile.fill(rgb[color])
                for coord in flooded_list:
                    color_of_tile[coord] = color

                # This is the function the students will write. -Jeremy
                flood(color_of_tile, flooded_list)

                for i in range(len(flooded_list)):
                    screen.blit(tile, flooded_list[i])

                # drought (new feature, disabled for now) -Jeremy
                if False and len(flooded_list) > 1 and random.randint(1,5) == 1:
                    display.set_caption('Flood-it! Drought in progress!')
                    movecount -= 1
                    num_remove = len(flooded_list) / 10
                    drought_tiles = create_drought(flooded_list, color_of_tile)
                    for coord in drought_tiles:
                        tile.fill(rgb[color_of_tile[coord]])
                        screen.blit(tile, coord)
                else:
                    display.set_caption('Flood-it! '+str(movecount)+'/25')

                pygame.display.update()
                

        if len(flooded_list) == 196:
            if not for_restart:
                game_over('win.png')
                for_restart = True
            display.set_caption('Flood-it! Congratulations. You won!')

        if movecount == 25 and len(flooded_list) != 196:
            if not for_restart:
                game_over('gameover.png')
                for_restart = True
            display.set_caption('Flood-it! GAME OVER!')

    if update == True:
        #TODO: call update function
        update = False
