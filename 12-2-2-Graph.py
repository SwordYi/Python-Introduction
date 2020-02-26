class Node(object):
    def __init__(self, name):
        """ 假设name是字符串 """
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    
class Edge(object):
    def __init__(self, src, dest):
        """ 假设src和dest是节点 """
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        """ 假设src和dest是节点，weight是个数值 """
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return self.src.getName() + '->(' + str(self.weight) + ')' + self.dest.getName() 
    

class Digraph(object):
    # nodes是图中节点的列表
    # edges是一个字典，将每个节点映射到其子节点列表
    def __init__(self):
        self.nodes = []
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.deges[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'
        return result[:-1]
        
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge):
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)