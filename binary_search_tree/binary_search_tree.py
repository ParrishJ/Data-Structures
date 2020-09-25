"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class Stack:
    def __init__(self):
        self.storage = list()
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1
        
    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop()

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = list()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.insert(0, value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop()

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
        if self is None:
            return
        

        if self.left != None:
            self.left.in_order_print()
            
        print(self.value)

        if self.right != None:
            self.right.in_order_print()
            
        
       
           

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        q = Queue()

        q.enqueue(self)

        while len(q) > 0:
            current_node = q.dequeue()
            print(current_node)

            if current_node.left:
                q.enqueue(current_node.left)

            if current_node.right:
                q.enqueue(current_node.right)





    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        s = Stack()

        s.push(self)

        while len(s) > 0:
            current_node = s.pop()
            print(current_node)

            if current_node.left:
                s.push(current_node.left)

            if current_node.right:
                s.push(current_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

    def __str__(self):
        return f'(value: {self.value})'


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

#bst.bft_print()
#bst.dft_print()

""" print("elegant methods")
print("pre order")
bst.pre_order_dft() """
print("in order")
bst.in_order_print()
""" print("post order")
bst.post_order_dft()   """
