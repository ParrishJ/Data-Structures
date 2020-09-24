class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)
       
        if value < self.value:
            if self.left == None:
                self.left = new_node
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = new_node
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        if self.value == None:
            return None
        else:
            if self.right == None:
                return self.value
            else:
                return self.right.get_max()
            

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left != None:
            self.left.for_each(fn)

        if self.right != None:
            self.right.for_each(fn)
            

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        print(self.value)
        
        if self.left:
            self.left.in_order_print()

        if self.right:
            self.right.in_order_print()

        
        
   

    def __str__(self):
        return f'(value: {self.value}, left: {self.left}, right: {self.right})'


bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.in_order_print()