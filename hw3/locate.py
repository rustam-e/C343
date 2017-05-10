#The function returns a pair (xi,yi) where (xcoords[xi], ycoords[yi]) is the top-left
# point of the rectangle containing (x,y).

def locate(xcoords, ycoords, (x, y)):
    v1 = bin (xcoords, 0, len(xcoords), x)
    v2 = bin (ycoords, 0, len(ycoords), y)
    return (v1, v2)

def bin (coor, low, high, v):
    if len(coor) == 0:
        return None
    else:
        mid = low + (high - low) // 2
        if v in range(coor[mid - 1], (coor[mid] + 1)):
            return mid - 1
        elif v < coor[mid]:
            return bin(coor, low, mid, v)
        else:
            return bin(coor, mid, high, v)

        ##  color

