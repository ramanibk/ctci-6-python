# Question:
# Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is
# defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.

# Solution:
# We can simply recurse through the entire tree, and for each node, compute the heights of each subtree.


def dfs_display(node):
    if node is None:
        return
    print("")
    print(str(node.data) + ":"),
    if node.left is not None:
        print(str(node.left.data) + ","),
    else:
        print("NULL"),
    if node.right is not None:
        print(str(node.right.data) + "")
    else:
        print("NULL"),
    dfs_display(node.left)
    dfs_display(node.right)


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root=None):
        self.root = root

    def print_tree(self):
        dfs_display(self.root)
        print("")


def get_height(node):
    if node is None:
        return -1
    return max(get_height(node.left), get_height(node.right)) + 1


def is_balanced(root):
    if root is None:
        return True
    height_diff = get_height(root.left) - get_height(root.right)
    if abs(height_diff) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)


# Although the above algorithm works, it's not very efficient. On each node, we recurse through its entire subtree.
# This means that get_height is called repeatedly on the same nodes. The algorithm is O(N log N) since each node is
# "touched" once per node above it.
# We need to cut out some of the calls to get_height.

# If we inspect this method, we may notice that get_height could actually check if the tree is balanced at the same
# time as it is checking heights. What do we do when we discover that the subtree isn't balanced? Return an error code.

# This improved algorithm works by checking the height of each subtree as we recurse down from the root. On each node,
# we recursively get the heights of the left and the right subtrees through the check_height method. If the subtree
# is balanced, check_height will return the actual height of the subtree. If the subtree is not balanced,
# then check_height will return an error code. We will immediately break and return an error code from the current call.

# What do we use for the error code? The height of a null tree is generally defined to be -1, so that's not a great
# idea for an error code. Instead, we will use -float("Inf").


low_inf = -float("Inf")


def check_height(root):
    if root is None:
        return -1
    left_height = check_height(root.left)
    if left_height == low_inf:
        return low_inf   # pass error up
    right_height = check_height(root.right)
    if right_height == low_inf:
        return -low_inf  # pass error up
    height_diff = left_height - right_height
    if abs(height_diff) > 1:
        return low_inf
    else:
        return max(left_height, right_height) + 1


def is_balanced_efficient(root):
    return check_height(root) != low_inf

# The above code runs in O(N) time and O(H) space, where H is the height of the tree.


# Tree Tests
n6 = Node(6)
n5 = Node(5)
n4 = Node(4, n6)
n3 = Node(3, n4, n5)
n2 = Node(2)
n1 = Node(1, n2, n3)
my_tree_1 = Tree(n1)
my_tree_1.print_tree()

# check_balance test
print("Is it Balanced? (Tree-1) " + str(is_balanced(my_tree_1.root)))
print("Is it Balanced? (Tree-1) " + str(is_balanced_efficient(my_tree_1.root)))

n7 = Node(7)
n8 = Node(8, n7, n5)
n1 = Node(1, n2, n8)
my_tree_2 = Tree(n1)
my_tree_2.print_tree()

# check_balance test
print("Is it Balanced? (Tree-2) " + str(is_balanced(my_tree_2.root)))
print("Is it Balanced? (Tree-2) " + str(is_balanced_efficient(my_tree_2.root)))
