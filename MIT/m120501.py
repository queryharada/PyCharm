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
            self.nodes.append()
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


if __name__ == "__main__":
    pass
