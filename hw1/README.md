
The flood function adds same-color regions to the flooded_list 
that are adjacent to the tiles in the flooded list.                                                                                                           

Color_of_tile is a dictionary. color_of_tile[(0,0)] will gives the color of the first                                                                       
square, and what should be the color of the entire flooded space. And so the algorithm 
checks the colors of adjacent tiles - if color = x && if x is to the up or down or left                                                                                   
or right, then append the tile to flooded list.                                                                                                                
                                                                                             
Basically I use a while loop in_bounds and the directional functions in the utilities file to                                                                    
check all the tiles that are touching the flooded area. I compare each color the the                                                                            
touching tiles to color_of_tile[0,0] and if it matches, append it to flooded_list.

I believe, my implementation is has a big O = n. For every element it 
checks multiple attributes, and if the conditions are satisfied, it adds them to the list.

