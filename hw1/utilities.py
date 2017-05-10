SCREEN_SIZE = (608, 448)
TILE_SIZE = (32, 32)
STEP_SIZE = 32
colors = ["pink", "violet", "yellow", "red", "olive", "blue"]
rgb = { "pink": (255, 105, 180),
        "violet": (138, 43, 226),
        "yellow": (255, 255, 0),
        "red": (255, 69, 0),
        "olive": (110, 139, 61),
        "blue": (0, 191, 255) }

def up(coord):
    return (coord[0], coord[1] - STEP_SIZE)

def right(coord):
    return (coord[0] + STEP_SIZE, coord[1])

def down(coord):
    return (coord[0], coord[1] + STEP_SIZE)

def left(coord):
    return (coord[0] - STEP_SIZE, coord[1])

def in_bounds(coord):
    return 0 <= coord[0] and coord[0] < SCREEN_SIZE[1] \
        and 0 <= coord[1] and coord[1] < SCREEN_SIZE[1]
