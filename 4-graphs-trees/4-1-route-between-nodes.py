# Question:
# Given a directed graph, design an algorithm to find out whether there is a route between two nodes

# Solution:
# Two well-known algorithms can do this. What are the trade-offs between them?
# The problem can be solved by a simple graph traversal, such as DFS or BFS.
# We start with one of the two nodes and during traversal, check if the other node is found.
# Should mark any node found in the course of traversal as "already visited" to avoid cycles and repetition of nodes.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def add_to_linked_list(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def pop_from_linked_list(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = temp.next
        return temp.data


state = {"u": "unvisited", "v": "visited", "i": "visiting"}


class GraphNode:
    def __init__(self, data, neighbors=[]):
        self.data = data
        self.state = state["u"]
        self.neighbors = neighbors


class Graph:
    def __init__(self, roots=[]):
        self.roots = roots
        self.all_nodes = self.get_all_nodes()
        self.total = len(self.all_nodes)

    # DFS: GET ALL NODES
    # call dfs on a node
    # call it on its children
    # visit the node
    def get_all_nodes(self):
        all_nodes = []

        def call_dfs(node):
            if node is None:
                return
            all_nodes.append(node)
            for v in node.neighbors:
                if v not in all_nodes:
                    call_dfs(v)

        for root in self.roots:
            call_dfs(root)
        return all_nodes


def search(graph, node_s, node_t):
    if node_s == node_t:
        return True
    # print "entered search: " + str(node_s.data) + "," + str(node_t.data)
    q = LinkedList()

    # set all states freshly to unvisited
    # print "setting to unvisited"

    for node in graph.get_all_nodes():
        node.state = state["u"]
        # print str(node.data) + ":" + node.state

    node_s.state = state["i"]
    q.add_to_linked_list(node_s)

    while q.head is not None:
        u = q.pop_from_linked_list()
        if u is not None:
            for v in u.neighbors:
                if v.state == state["u"]:
                    if v == node_t:
                        return True
                    else:
                        v.state = state["i"]
                        q.add_to_linked_list(v)
            u.state = state["v"]
    return False


gn5 = GraphNode(5)
gn4 = GraphNode(4)
gn3 = GraphNode(3, [gn4, gn5])
gn2 = GraphNode(2)
gn1 = GraphNode(1, [gn2, gn3])
graph = Graph([gn1])

"""
# Print entered graph
all_nodes = graph.get_all_nodes()
for node in all_nodes:
    string = str(node.data) + ": " + ' '.join(str(x.data) for x in node.neighbors)
    print string
"""

# Correctness tests
if search(graph, gn1, gn5):
    print("Correct!")
else:
    print("Wrong.")

if not search(graph, gn2, gn4):
    print("Correct!")
else:
    print("Wrong.")

if search(graph, gn3, gn4):
    print("Correct!")
else:
    print("Wrong.")
