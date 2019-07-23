# -*- coding:utf-8 -*-

class Node(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()


class WeightedEdge(Edge):
    def __init__(self, src, dest, weght=1.0):
        self.src = src
        self.dest = dest
        self.weight = weght

    def getWeight(self):
        return self.weight

    def __str__(self):
        return self.src.getName() + '->(' + str(self.weight) + ')' \
               + self.dest.getName()


class Digraph(object):
    def __init__(self):
        self.nodes = list()
        self.edges = dict()

    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node ')
        else:
            self.nodes.append(node)
            self.edges[node] = list()

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph ')
        self.edges[src].append(dest)

    def chirdrenOf(self, node):
        return self.edges[node]

    def hashNode(self, node):
        return node in self.nodes

    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' \
                         + dest.Getname() + '\n'
        return result[:-1]


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


def printPath(path):
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result


def DFS(garph, start, end, path, shortest, toPrint=False):
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in garph.chirdrenOf(start):
        if node not in path:
            if (shortest == None) or (len(path) < len(shortest)):
                newPath = DFS(garph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
    return shortest


def shortestPath(garph, start, end, toPrint=False):
    return DFS(garph, start, end, [], None, toPrint)


if __name__ == "__main__":
    def testSP():
        nodes = list()
        for name in range(6):
            nodes.append(Node(str(name)))
        g = Digraph()
        for n in nodes:
            g.addNode(n)
        g.addEdge(Edge(nodes[0], nodes[1]))
        g.addEdge(Edge(nodes[1], nodes[2]))
        g.addEdge(Edge(nodes[2], nodes[3]))
        g.addEdge(Edge(nodes[3], nodes[4]))
        g.addEdge(Edge(nodes[3], nodes[5]))
        g.addEdge(Edge(nodes[0], nodes[2]))
        g.addEdge(Edge(nodes[1], nodes[0]))
        g.addEdge(Edge(nodes[3], nodes[1]))
        g.addEdge(Edge(nodes[4], nodes[0]))
        sp = shortestPath(g, nodes[0], nodes[5], toPrint=True)
        print('Shortest path found by DFS:', printPath(sp))


    testSP()
