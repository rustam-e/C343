
The graph of my flood1.py is expnential - just as I expected. I can't readily concieve
of an algorithm to change that, however, the runtime can be reduced significantly by changing
flooded_list into an array, due to faster referencing of arrays. The looping through 
the flooded list is the primary cause of the delay. A two-dimensional array would've been
much faster, but due to busy schedule and being unfamiliar with python, I will not be able
to implement changes necessary for that to happen. Instead, I wrote the second algorithm
that looked at the tiles to be changed but that didn't work also it wouldn't have improved
the run time in any important manner.


The for loop going through the flooded_list is the major contributor to the delays in execution.
