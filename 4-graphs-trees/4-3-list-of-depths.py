# Question:
# Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth.
# That is, if you have a tree with depth D, you'll have D linked lists.

# Solution:
# Try modifying a graph search algorithm to track the depth from the root.
# A hash table or array that maps from the level number to nodes at that level might also be useful.
# You should be able to come up with an algorithm with both DFS and BFS.

# Though at first glance we might think that this problem requires level by level traversal, that isn't necessary.
# We can traverse the graph any way we would like, provided we know which level we're on as we do so.

# We can implement a simple modification of the pre-order traversal algorithm, where we pass in level + 1 to
# the next recursive call.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        return

    def fetch(self, index):
        temp = self.head
        ptr = 0
        if temp is None:
            return
        while temp.next is not None:
            if ptr == index:
                return temp
            ptr += 1
            temp = temp.next

    def count(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def display(self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            print(str(temp.data) + ", "),
            temp = temp.next
        print(str(temp.data))


class TreeNode:
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
                return None
            print(str(node.data) + ":")
            if node.left is not None:
                print("\t(l) " + str(node.left.data))
            if node.right is not None:
                print("\t(r) " + str(node.right.data))
            dfs(node.left)
            dfs(node.right)

        print("Tree:")
        dfs(self.root)


def create_level_linked_list(root, level):
    global lists
    if root is None:  # base case
        return
    if len(lists) == level:
        # levels are always traversed in order. So if this is the first time we are visiting level i, we must have seen
        # levels 0 through i - 1/. We can therefore, safely add the level at the end.
        new_node = Node(root)
        ll = LinkedList(new_node)
        lists.append(ll)
    else:
        ll = lists[level]
        ll.insert(root)
    create_level_linked_list(root.left, level + 1)
    create_level_linked_list(root.right, level + 1)


def create_level_linked_list_wrap(root):
    global lists
    lists = []
    create_level_linked_list(root, 0)


# Tests for Linked Lists
n1 = Node(1)
l1 = LinkedList(n1)
l1.insert(2)
l1.insert(15)

n4 = Node(3)
l2 = LinkedList(n4)
l2.insert(60)

# l1.display()
# l2.display()

# print(l1.count())
# print(l2.count())

"""
lists_global = [l1, l2]
for lst in lists_global:
    lst.display()
"""


# Tests for Tree Class
n5 = TreeNode(5)
n4 = TreeNode(4)
n3 = TreeNode(3, left=n4, right=n5)
n2 = TreeNode(2)
n1 = TreeNode(1, left=n2, right=n3)
tree_global = Tree(n1)
# tree_global.print_tree()


# Solution
lists = []
create_level_linked_list_wrap(tree_global.root)

print("Solution --")
for lvl, lst in enumerate(lists):
    print("level " + str(lvl) + ": "),
    temp = lst.head
    while temp is not None:
        print(str(temp.data.data)),
        temp = temp.next
    print("")