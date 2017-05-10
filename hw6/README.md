Set the initial values to 0,0 in the top left.

Update board values based on the equations: loop through every positon and choose the highest score based on the
position to top left + score of the compoarison of a character from each 
string; position to the top + the space penalty; space to the right + the space penalty.

traceback: loop through the strings and grab the characters baised on the board's value. If it is the 
top-left value plus the score of the last characters of the strings, grab both caracters. If it is the 
top or left + the space penalty, grab the character of only that direction and use the space for the other. 
Also, only subtract 1 from the accociated index. If only one of the indexes hits zero, add spaces to that 
string and use letters for the other until both are zero.
