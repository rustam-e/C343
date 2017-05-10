from utilities import *


def flood(color_of_tile, flooded_list, screen_size):
  i = 0
  while i < len(flooded_list):

    usquare = (up(flooded_list[i]))
    if in_bounds(usquare, screen_size):
      if color_of_tile[flooded_list[0]] == color_of_tile[usquare]:
        if usquare not in flooded_list:
          flooded_list.append(usquare)

    dsquare = (down(flooded_list[i]))
    if in_bounds(dsquare, screen_size):
      if color_of_tile[flooded_list[0]] == color_of_tile[dsquare]:
        if dsquare not in flooded_list:
          flooded_list.append(dsquare)

    rsquare = (right(flooded_list[i]))
    if in_bounds(rsquare, screen_size):
      if color_of_tile[flooded_list[0]] == color_of_tile[rsquare]:
        if rsquare not in flooded_list:
          flooded_list.append(rsquare)

    lsquare = (left(flooded_list[i]))
    if in_bounds(lsquare, screen_size):
      if color_of_tile[flooded_list[0]] == color_of_tile[lsquare]:
        if lsquare not in flooded_list:
          flooded_list.append(lsquare)

    i = i + 1
