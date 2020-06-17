class Vertex(object):
    """docstring for Vertex"""

    def __init__(self, id):
        self.id = id
        self.connectedTo = {}

    def addNeighbor(self, neighbor, weight=0):
        # Neighbor is the key and weight is the value
        self.connectedTo[neighbor] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getID(self):
        return self.id

    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]

    # To print the connections
    def __str__(self):
        return str(self.id) + ' connected to' + str([x.id for x in self.connectedTo])


class Graph(object):
    """docstring for Graph"""

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, id):
        self.numVertices += 1
        newVertex = Vertex(id)
        self.vertList[id] = newVertex
        return newVertex

    def getVertex(self):
        # self.vertList only checks the keys by default. To check index, do self.vertList.values()
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def addEdge(self, f, t, cost=0):
        # f is from, t is to and cost is weight
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)

        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        # Return just the keys
        return self.vertList.keys()

    def __iter__(self):
        # grab all values in vertList dictionary and make it into an iterable
        return iter(self.vertList.values())

    def __contains__(self, n):
        return n in self.vertList


# if __name__ == '__main__':
#     g = Graph()
#     for i in range(6):
#         g.addVertex(i)

#     g.vertList
#     g.addEdge(0, 1, 2) # add edge from V0 to V1 with weight 2
#     for vertex in g: #Takes advantage of the __iter__ method
#         print(vertex)
#         print(vertex.getConnections())
#         print('\n')
