# Question:
# Given a sorted (increasing order) array with unique integer elements, create a binary search tree with minimal height.

# Solution:
# A minimal binary tree has about the same number of nodes on the left side of each node as on the right.
# Let's focus on the root for now. How would you ensure that about the same number of nodes are on the left of the root
# as on the right?

# You could implement this by finding the "ideal" next element to add and repeatedly calling insertValue. This will be
# a bit inefficient, as you would have to repeatedly traverse the tree (resulting in total cost of O(N log N).
# Try recursion instead. Can you divide this problem into sub-problems?

# Imagine we had a createMinimalTree method that returns a minimal tree for a given array (but for some strange reason
# doesn't operate on the root of the tree). Could you use this to operate on the root of the tree? Could you write the
# base case for the function? Great! That's basically the entire function.

# We want the root to be the middle of the array, since this would mean that half elements would be less than the root
# and half would be greater than it. The middle of each subsection of the array becomes the root of the node. The left
# half of the array will become the left subtree, and the right half of the array will become the right subtree.

# Algorithm:
# Insert into the tree the middle element of the array
# Insert into the left subtree, the left subarray elements
# Insert into the right subtree, the right subarray elements
# Recurse


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root=None):
        self.root = root

    def print_tree(self):
        def dfs(node):
            if node is None:
                return
            print(str(node.data) + ": ")
            if node.left is not None:
                print("\t(l) " + str(node.left.data))
            if node.right is not None:
                print("\t(r) " + str(node.right.data))
            dfs(node.left)
            dfs(node.right)

        print("Tree looks like:")
        dfs(self.root)


def create_minimal_bst(array, start, end):
    if end < start:
        return None
    mid = (start + end) / 2
    new_node = Node(array[mid])
    new_node.left = create_minimal_bst(array, start, mid - 1)
    new_node.right = create_minimal_bst(array, mid + 1, end)
    return new_node


def create_minimal_bst_wrap(array):
    return create_minimal_bst(array, 0, len(array) - 1)


"""
n4 = Node(4)
n5 = Node(5)
n3 = Node(3, left=n4, right=n5)
n2 = Node(2)
n1 = Node(1, left=n2, right=n3)
myTree = Tree(n1)
myTree.print_tree()
"""

sorted_array = [x for x in range(1, 6)]
resultTreeRoot = create_minimal_bst_wrap(sorted_array)
resultTree = Tree(resultTreeRoot)
resultTree.print_tree()
