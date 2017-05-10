<<<<<<< HEAD
# AVL Trees
=======
# AVL Trees                                                                                                  
>>>>>>> 5828f53d0917a2772d2698410e76edd634e6af1f

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def less_than(x, y):
    return x < y

class AVLTree:
    def __init__(self, root=None, less=less_than):
        self.node = None
        self.root = None
        self.height = -1
        self.balanace = 0

    def height(self):
        if self.node:
            return self.node.height
        else:
<<<<<<< HEAD
            return 0
=======
         return 0
>>>>>>> 5828f53d0917a2772d2698410e76edd634e6af1f

    def is_leaf(self):
        return (self.height == 0)

    def insert(self, key):
        tree = self.node
        newnode = AVLNode(key)
<<<<<<< HEAD
        if tree == None:
=======
    if tree == None:
>>>>>>> 5828f53d0917a2772d2698410e76edd634e6af1f
            self.node = newnode
            self.node.left = AVLTree()
            self.node.right = AVLTree()
        elif key < tree.key:
            self.node.left.insert(key)
        elif key > tree.key:
            self.node.right.insert(key)
        else:
            self.rebalance()

    def rebalance(self):
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
<<<<<<< HEAD
                if self.node.left.balance < 0:
                    self.node.left.lrotate()
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
=======
        if self.node.left.balance < 0:
                    self.node.left.lrotate()
                    self.update_heights()
                    self.update_balances()
            self.rrotate()
>>>>>>> 5828f53d0917a2772d2698410e76edd634e6af1f
                self.update_heights()
                self.update_balances()
            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate()
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()

    def rrotate(self):
        A = self.node
        B = self.node.left.node
        T = B.right.node
<<<<<<< HEAD
        
=======

>>>>>>> 5828f53d0917a2772d2698410e76edd634e6af1f
        self.node = B
        B.right.node = A
        A.left.node = T

    def lrotate(self):
        A = self.node
        B = self.node.right.node
        T = B.left.node
<<<<<<< HEAD
        
=======

>>>>>>> 5828f53d0917a2772d2698410e76edd634e6af1f
        self.node = B
        B.left.node = A
        A.right.node = T

    def search(self, k):
        node = self.node
        while node is not None:
            if k < node.key:
                node = node.left.node
            elif k > node.key:
                node = node.right.node
            else:
                return node
                break
        return None

    def delete_node(self, n):
        self.delete(n.key)

    def update_heights(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()
<<<<<<< HEAD
            self.height = max(self.node.left.height, self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
    def search(self, k):
        node = self.node
        while node is not None:
            if k < node.key:
                node = node.left.node
            elif k > node.key:
                node = node.right.node
            else:
                return node
                break
        return None

    def delete_node(self, n):
        self.delete(n.key)

    def update_heights(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()
=======
>>>>>>> 5828f53d0917a2772d2698410e76edd634e6af1f
            self.height = max(self.node.left.height, self.node.right.height) + \
1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.node == None:
            if recurse:
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()
            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def delete(self, key):
<<<<<<< HEAD
        if self.node != None:
            if self.node.key == key:
                if self.node.left.node == None and self.node.right.node == None:
=======
    if self.node != None:
            if self.node.key == key:
                if self.node.left.node == None and self.node.right.node == None\
:
>>>>>>> 5828f53d0917a2772d2698410e76edd634e6af1f
                    self.node = None
                elif self.node.left.node == None:
                    self.node = self.node.right.node
                elif self.node.right.node == None:
                    self.node = self.node.left.node
                else:
                    replacement = self.successor(self.node)
                    if replacement != None:
                        self.node.key = replacement.key
<<<<<<< HEAD
                        self.node.right.delete(replacement.key)
=======
            self.node.right.delete(replacement.key)
>>>>>>> 5828f53d0917a2772d2698410e76edd634e6af1f
                self.rebalance()
                return
            elif key < self.node.key:
                self.node.left.delete(key)
            elif key > self.node.key:
                self.node.right.delete(key)

            self.rebalance()
        else:
            return
<<<<<<< HEAD
    
    def predecessor(self, node):
        if node:
            node = node.left.node
        if node != None:
=======

    def predecessor(self, node):
    if node:
            node = node.left.node
    if node != None:
>>>>>>> 5828f53d0917a2772d2698410e76edd634e6af1f
            while node.right != None:
                if node.right.node == None:
                    return node
                else:
                    node = node.right.node
        return node
<<<<<<< HEAD
    
=======

>>>>>>> 5828f53d0917a2772d2698410e76edd634e6af1f
    def successor(self, node):
        if node:
            node = node.right.node
        if node != None:
            while node.left != None:
<<<<<<< HEAD
                if node.left.node == None:
=======
        if node.left.node == None:
>>>>>>> 5828f53d0917a2772d2698410e76edd634e6af1f
                    return node
                else:
                    node = node.left.node
        return node

    def check_balanced(self):
<<<<<<< HEAD
        if self == None or self.node == None:
            return True
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())

    def display(self, level=0, pref=''):
        self.update_heights()
        self.update_balances()
        if self.node != None:
            print '-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(self.balance) + "]", "L" if self.is_leaf() else ' '
=======
    if self == None or self.node == None:
            return True
        self.update_heights()
        self.update_balances()
    return ((abs(self.balance) < 2) and self.node.left.check_balanced() and\
 self.node.right.check_balanced())

    def display(self, level=0, pref=''):
    self.update_heights()
        self.update_balances()
        if self.node != None:
            print '-' * level * 2, pref, self.node.key, "[" + str(self.height) \
+ ":" + str(self.balance) + "]", "L" if self.is_leaf() else ' '
>>>>>>> 5828f53d0917a2772d2698410e76edd634e6af1f
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.left != None:
                self.node.right.display(level + 1, '>')
<<<<<<< HEAD
=======

>>>>>>> 5828f53d0917a2772d2698410e76edd634e6af1f
