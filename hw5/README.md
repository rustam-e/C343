I made a few procedures like rotate left and rotate right. I used them to blanc\
e the trees.

<<<<<<< HEAD
I made a few procedures like rotate left and rotate right. I used them to blance the trees.

Rotate right takes a node, makes it's left subtree point to the node's parent, and then points the original \
node the right subtree of the original left subtree. If the original left subtree has a right subtree, that \
right subtree becomes the left subtree of the original node, otherwise the left subtree of the original node\
=======
Rotate right takes a node, makes it's left subtree point to the node's parent, \
and then points the original \
node the right subtree of the original left subtree. If the original left subtr\
ee has a right subtree, that \
right subtree becomes the left subtree of the original node, otherwise the left\
 subtree of the original node\
>>>>>>> 5828f53d0917a2772d2698410e76edd634e6af1f
 is None.

Rotate left is the same, only in reverse.

<<<<<<< HEAD
I calculate what nodes need to be balanced by calculating the height. If the height of the right and left su\
btrees has a difference greater than one, I would use rotate_left if the right side was heavy (had a greater\
 height), or rotate_right if the left side was heavy.

Finally, I would find the node where imbalance occurs by taking the node that was just inserted (or the node\
 that replaced the deleted node) and work up through the parents and check to see if there is imbalance. The\
 node of imbalance would be passed to rotate_left or rotate_right.

My balancer function would check to see if there was an imbalnce (find_imbalance would return None if there \
was no imbalance, otherwise return the node of imbalance), then calculate using height which side was heavy \
and pass rotate_left or rotate_right.

=======
I calculate what nodes need to be balanced by calculating the height. If the he\
ight of the right and left su\
btrees has a difference greater than one, I would use rotate_left if the right \
side was heavy (had a greater\
 height), or rotate_right if the left side was heavy.

Finally, I would find the node where imbalance occurs by taking the node that w\
as just inserted (or the node\
 that replaced the deleted node) and work up through the parents and check to s\
ee if there is imbalance. The\
 node of imbalance would be passed to rotate_left or rotate_right.

My balancer function would check to see if there was an imbalnce (find_imbalanc\
e would return None if there \
was no imbalance, otherwise return the node of imbalance), then calculate using\
 height which side was heavy \
>>>>>>> 5828f53d0917a2772d2698410e76edd634e6af1f
