from utilities import *

def flood(color_of_tile, flooded_list, screen_size):
    flood_ls = {}
    for coord in color_of_tile:
        if coord in flooded_list:
            flood_ls[coord] = False
        else:
            flood_ls[coord] = True
    
    for coord in flood_ls:
        if in_bounds(left(coord), screen_size):
            if flood_ls[left(coord)]:
                if color_of_tile[left(coord)] == color_of_tile[0,0]:
                    flood_ls[left(coord)] = False
                    flooded_list.append(left(coord))
        if in_bounds(right(coord), screen_size):
            if flood_ls[right(coord)]:
                if color_of_tile[right(coord)] == color_of_tile[0,0]:
                    flood_ls[right(coord)] = False
                    flooded_list.append(right(coord))
        if in_bounds(up(coord), screen_size):
            if flood_ls[up(coord)]:
                if color_of_tile[up(coord)] == color_of_tile[0,0]:
                    flood_ls[up(coord)] = False
                    flooded_list.append(up(coord))
        if in_bounds(down(coord), screen_size):
            if flood_ls[down(coord)]:
                if color_of_tile[down(coord)] == color_of_tile[0,0]:
                    flood_ls[down(coord)] = False
                    flooded_list.append(down(coord))
