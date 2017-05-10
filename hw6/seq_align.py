# Rustam Eynaliyev

import sys, time, random
import pygame

e_aplh = "abcdefghijklmnopqrstuvwxyz"
dna_alph = "ACGT"

# generate random string drawn from the given alphabet and of a given length
def gen_random_string(alphabet, length):
    a_len = len(alphabet)
    ret = ""
    for n in range(length):
        ret += alphabet[random.randint(0, a_len-1)]
    return ret

# print gen_random_string(e_aplh, 5)

SPACE_CHAR = '_'
SPACE_PENALTY = -1

# the scoring function
def s(x, y):
    if x == SPACE_CHAR or y == SPACE_CHAR:
        return SPACE_PENALTY
    elif x == y:
        return 1
    else:
        return -1

TILE_SIZE = 40
tile_color = (255, 255, 255)
highlight_color = (120, 129, 250)

# pygame stuff
def init_board(m, n):
    screen = pygame.display.set_mode(((m+2)*TILE_SIZE, (n+2)*TILE_SIZE))
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Dot Board')
    pygame.font.init()
    font = pygame.font.Font(None, 15)
    return screen, font

def create_tile(font, text, color):
    tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
    tile.fill(color)
    b1 = font.render(text, 1, (0, 0, 0))
    tile.blit(b1, (TILE_SIZE/2, TILE_SIZE/2))
    return tile

def render_board(board, font, s1, s2, F):
    for i in range(len(s1)):
        tile = create_tile(font, s1[i], tile_color)
        board.blit(tile, ((i+2)*TILE_SIZE, 0))
    tile = create_tile(font, '', tile_color); board.blit(tile, (0, 0))
    tile = create_tile(font, '', tile_color); board.blit(tile, (TILE_SIZE, 0))
    for j in range(len(s2)):
        tile = create_tile(font, s2[j], tile_color)
        board.blit(tile, (0, (j+2)*TILE_SIZE))
    tile = create_tile(font, '', tile_color); board.blit(tile, (0, TILE_SIZE))
    for (x,y) in sorted(F.keys()):
        tile = create_tile(font, str(F[(x,y)]), tile_color)
        board.blit(tile, ((x+1)*TILE_SIZE, (y+1)*TILE_SIZE))
# pygame stuff end

# the function takes two sequences and returns a pair that represents the alignment
# this should be a dynamic programming solution    
def seq_align(s1, s2, enable_graphics=True):
    
    m = len(s1); n = len(s2)
    
    screen = None; font = None
    if enable_graphics:
        screen, font = init_board(m, n)
    
    # this dictionary represents the board that keeps track of the alignment scores
    # its keys are of the form (i, j) where i and j are indexes from 0-to-m and 0-to-n respectively 
    F = {}
    ########################################################################################    
    for i in range(1,m+1):
        F[(i,0)] = SPACE_PENALTY * i
    
    for j in range(1,n+1):
        F[(0,j)] = SPACE_PENALTY * j
            ########################################################################################    

    # setup initial values for the recursion -- Student Code
    pass
    
    if enable_graphics:
        render_board(screen, font, s1, s2, F)
        pygame.display.flip()
        time.sleep(2)
    
    # update the board based on the recursion equations -- Student Code
            ########################################################################################    
    for i in range(0, m + 1):
        F[(i, 0)] = [i * SPACE_PENALTY, "delete"]

    for i in range(0, n + 1):
        F[(0, i)] = [i * SPACE_PENALTY, "insert"]
        ########################################################################################    

    pass
    if enable_graphics:
        render_board(screen, font, s1, s2, F)
        pygame.display.flip()

        for i in range(1, m + 1):
        for j in range (1, n + 1):
            match = F[(i - 1, j - 1)][0] + s(s1[i - 1], s2[j - 1])
            deletion = F[(i - 1, j)][0] + SPACE_PENALTY
            insertion = F[(i, j - 1)][0] + SPACE_PENALTY

            if insertion > deletion:
                if insertion > match:
                    F[(i, j)] = [ insertion, "insert" ]
                else:
                    F[(i, j)] = [ match, "match" ]
            else:
                if deletion > match:
                    F[(i, j)] = [ deletion, "delete" ]
                else:
                    F[(i, j)] = [ match, "match" ]

                       i = m
    
    # traceback -- Student Code
            ########################################################################################    

    j = n
    r1 = ""
    r2 = ""
    while j != 0 or i != 0:
        move = F[(i, j)][1]

        if move == "match":
            r1 = s1[i - 1] + r1
            r2 = s2[j - 1] + r2
            i -= 1
            j -= 1
        elif move == "delete":
            r1 = s1[i - 1] + r1
            r2 = SPACE_CHAR + r2
            i -= 1
        else:
            r1 = SPACE_CHAR + r1
            r2 = s2[j - 1] + r2
            j -= 1

    pass
    return None, None
            ########################################################################################    

# if __name__ == "__main__":
    # my unit tests

if len(sys.argv) == 2 and sys.argv[1] == 'test':
    # test mode - run the test cases
    f=open('tests.txt', 'r');tests= eval(f.read());f.close()
    cnt = 0; passed = True
    for ((s1, s2), (a1, a2)) in tests:
        (ret_a1, ret_a2) = seq_align(s1, s2, False)
        if (ret_a1 != a1) or (ret_a2 != a2):
            print("test#" + str(cnt) + " failed...")
            passed = False
        cnt += 1
    if passed: print("All tests passed!")
elif len(sys.argv) == 2 and sys.argv[1] == 'gentests':
    # generate test cases here using the correct seq_align function
    tests = []
    for n in range(25):
        m = random.randint(8, 70); n = random.randint(8, 70)
        (s1, s2) = (gen_random_string(dna_alph, m), gen_random_string(dna_alph, n))
        (a1, a2) = seq_align(s1, s2, False)
        tests.append(((s1, s2), (a1, a2)))
    f=open('tests.txt', 'w');f.write(str(tests));f.close()
else:
    # interactive mode
    l = [('ACACACTA', 'AGCACACA'), ('IMISSMISSISSIPI', 'MYMISSISAHIPPIE')]
    enable_graphics = True
    if enable_graphics: pygame.init()
    for (s1, s2) in l:
        print 'sequences:'
        print (s1, s2)
        
        m = len(s1)
        n = len(s2)
        
        print 'alignment: '
        print seq_align(s1, s2, enable_graphics)
    
    if enable_graphics: pygame.quit()

