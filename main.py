from collections import deque

class Graph:
    # O(1)
    def __init__(self):
        self.adjList = {}
        
    def __repr__(self):
        return str(self.adjList)
    
    # O(1)
    def addNode(self, value):
        if value not in self.adjList:
            self.adjList[value] = set()
    
    # O(n)
    def removeNode(self, value):
        if value not in self.adjList:
            return
        self.adjList.pop(value)
        for otherNode in self.adjList:
            if value in self.adjList[otherNode]:
                self.adjList[otherNode].remove(value)
    
    # O(1)
    def addEdge(self, fromNode, toNode):
        self.adjList[fromNode].add(toNode)
    
    # O(1)
    def removeEdge(self, fromNode, toNode):
        self.adjList[fromNode].remove(toNode)

    
    # O(1)
    def edgeExists(self, fromNode, toNode):
        if fromNode in self.adjList:
            return toNode in self.adjList[fromNode]
        return False
    
    def dft(self, startingNode):
        stack = deque()
        stack.append(startingNode)
        visited = set()
        traversalList = []
        while len(stack) > 0:
            currNode = stack.pop()
            if currNode not in visited:
                traversalList.append(currNode)
                visited.add(currNode)
                for neighbor in self.adjList[currNode]:
                    stack.append(neighbor)
        print(traversalList)
        
    def recursiveDFT(self, startingNode):
        visited = set()
        self.recursiveDFTHelper(startingNode, visited)
        
    def recursiveDFTHelper(self, currNode, visited):
        visited.add(currNode)
        print(currNode)
        for neighbor in self.adjList[currNode]:
            if neighbor not in visited:
                self.recursiveDFTHelper(neighbor, visited)
                
    def bft(self, startingNode):
        queue = deque()
        queue.append(startingNode)
        visited = set()
        traversalList = []
        while len(queue) > 0:
            currNode = queue.popleft()
            if currNode not in visited:
                traversalList.append(currNode)
                visited.add(currNode)
                for neighbor in self.adjList[currNode]:
                    queue.append(neighbor)
        print(traversalList)
                
    def bfs(self, startingNode, goalNode):
        queue = deque()
        visited = set()
        visited.add(startingNode)
        queue.append([startingNode])
        while len(queue) > 0:
            print(queue)
            currPath = queue.popleft()
            currVertex = currPath[-1]
            if currVertex == goalNode:
                return currPath
            for neighbor in self.adjList[currVertex]:
                if neighbor not in visited:
                    newPath = currPath.copy()
                    newPath.append(neighbor)
                    visited.add(neighbor)
                    queue.append(newPath)
        
    
myGraph = Graph()
myGraph.addNode(1)
myGraph.addNode(2)
myGraph.addNode(3)
myGraph.addNode(4)
myGraph.addEdge(1, 2)
myGraph.addEdge(1, 3)
myGraph.addEdge(2, 4)
myGraph.addEdge(3, 4)
myGraph.addEdge(4, 1)
myGraph.bft(1)
# myGraph.recursiveDFT(1)