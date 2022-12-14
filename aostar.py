class Graph:
    def __init__(self, graph, heuristicNodeList, startNode):
        self.graph = graph
        self.H = heuristicNodeList
        self.start = startNode
        self.parent = {}
        self.status = {}
        self.solnGraph = {}
        
    def applyAOStar(self):
        self.AOStar(self.start, False)
    
    def getNeighbours(self,v):
        return self.graph.get(v,'')
    
    def getStatus(self, v):
        return self.status.get(v,0)
    
    def setStatus(self,v,val):
        self.status[v] = val
        
    def getHeuristicNodeValue(self,n):
        return self.H.get(n,0)
    
    def setHeuristicNodeValue(self,n,value):
        self.H[n] = value
        
    def printSoln(self):
        print("For Graph Solution, Traverse Graph from Start Node: ", self.start)
        print("-"*40,self.solnGraph,"-"*40, sep='\n')
        
    def computeMinCostChildNodes(self, v):
        minCost = 0
        costToChildNodeListDict = {}
        costToChildNodeListDict[minCost] = []
        flag = True
        
        for nodeInfoTupleList in self.getNeighbours(v):
            cost=0
            nodeList = []
            
            for c,weight in nodeInfoTupleList:
                cost += self.getHeuristicNodeValue(c) + weight
                nodeList.append(c)
                
            if flag == True:
                minCost = cost
                costToChildNodeListDict[minCost] = nodeList
                flag = False
                
            else:
                if minCost > cost:
                    minCost = cost
                    costToChildNodeListDict[minCost] = nodeList
        
        return minCost,costToChildNodeListDict[minCost]
    
    def AOStar(self, v, backtracking):
        print("Heuristic Value: ", self.H)
        print("Solution Graph: ", self.solnGraph)
        print("Processing node: ", v)
        print("-"*40)
        
        if self.getStatus(v) >= 0:
            minCost, childNodeList = self.computeMinCostChildNodes(v)
            print(minCost, childNodeList)
            
            self.setHeuristicNodeValue(v, minCost)
            self.setStatus(v,len(childNodeList))
            solved = True
            
            for childNode in childNodeList:
                self.parent[childNode] = v
                if self.getStatus(childNode) != -1:
                    solved = solved & False
                    
            if solved == True:
                self.setStatus(v,-1)
                self.solnGraph[v] = childNodeList
                
            if v!= self.start:
                self.AOStar(self.parent[v], True)
                
            if backtracking == False:
                for childNode in childNodeList:
                    self.setStatus(childNode, 0)
                    self.AOStar(childNode,False)
                        

print("Graph - 1")
h1 = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F': 1, 'G': 5, 'H': 7, 'I': 7, 'J': 1}
graph1 = {'A': [[('B',1), ('C',1)], [('D',1)]],
          'B': [[('G',1)],[('H',1)]],
          'C': [[('J',1)]],
          'D': [[('E',1),('F',1)]],
          'G': [[('I',1)]]
         }

G1 = Graph(graph1, h1, 'A')
G1.applyAOStar()
G1.printSoln()