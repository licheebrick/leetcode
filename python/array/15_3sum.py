from collections import defaultdict
from collections import deque
import sys

class Tree(object):
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data

class Vertex(object):

    def __init__(self):
        self.d = 0
        self.e = None
        self.color = 'White'
        self.adjacent = dict()

    def __str__(self):
        return str(self.adjacent) + ", status: " + str(self.color)

    def add_adj(self, adjnode, weight):
        self.adjacent[adjnode] = weight


class Graph(object):
    """ Graph data Structure """

    def __init__(self, directed=False):
        self.vertexs = dict()
        self.vertex_num = 0
        self.directed = directed

    def add_vertex(self, node_name):
        self.vertex_num += 1
        self.vertexs[node_name] = Vertex()

    def add_edge(self, node1_name, node2_name, weight1, weight2=0):
        if not self.vertexs.has_key(node1_name):
            self.vertexs[node1_name] = Vertex()
        if not self.vertexs.has_key(node2_name):
            self.vertexs[node2_name] = Vertex()
        self.vertexs[node1_name].adjacent[node2_name] = weight1
        if not self.directed:
            self.vertexs[node2_name].adjacent[node1_name] = weight2

    def BFS(self, start_node):
        queue = deque()
        deque.append(queue, start_node)
        while queue:
            node = queue.popleft()
            for adjnode in self.vertexs[node].adjacent.keys():
                if self.vertexs[adjnode].color is 'White':
                    self.vertexs[adjnode].color = 'Grey'
                    deque.append(queue, adjnode)
            self.vertexs[node].color = 'Black'
            print node, self.vertexs[node]

    def DFS(self, start_node):
        stack = list()
        stack.append(start_node)
        while stack:
            node = stack.pop()
            for adjnode in self.vertexs[node].adjacent.keys():
                if self.vertexs[adjnode].color is 'White':
                    self.vertexs[adjnode].color = 'Grey'
                    stack.append(adjnode)
            self.vertexs[node].color = 'Black'
            print node, self.vertexs[node]

connections = [('A', 'B', 1), ('B', 'C', 3), ('B', 'D', 4),
               ('C', 'D', 5), ('E', 'F', 5), ('F', 'C', 1)]
g = Graph()
for entry in connections:
    g.add_edge(*entry)
for key, entry in g.vertexs.items():
    print key, entry
print
g.DFS('A')
print
for key, entry in g.vertexs.items():
    print key, entry
