ipfile = open("ubinput1.txt",'r')

class adjacencyList(object):
    def __init__(self,no):
        self.n = no
        self.adjList=[None]*(self.n+1)
        self.degree = [0]*(self.n+1)
        
        
    def createAdjList(self):
        for j in range (1,self.n+1):
            temp=[]
            adjedges = ipfile.readline()
            temp = adjedges.split()
            #print temp
            i = 0
            head=int(temp[0])
            for t in temp:
                if i == 0:
                    xe = adjacencyListNode(int(t))
                    self.adjList[int(t)] = xe 
                else:
                    xe = adjacencyListNode(int(t))
                    temp = self.adjList[head]
                    while temp.nextnode is not None:
                        temp = temp.nextnode
                    temp.nextnode = xe        
                i = i+1                        

                
                
    def __str__(self):
        if self.adjList is None:
            return "<empty graph>"
        else:
            strgraph = ""
            for i in range(1,self.n+1):
                temp = self.adjList[i]
                if temp is not None:    
                    strgraph =strgraph+str(temp.vertex)
                    temp = temp.nextnode
                    while temp is not None:
                        strgraph=strgraph+"-->"+str(temp.vertex)
                        temp = temp.nextnode
                    strgraph = strgraph + "\n"
        return strgraph 
    
class adjacencyListNode(object):
    def __init__(self,key):
        self.vertex = int(key)
        self.nextnode = None
        
        
class depthfirstsearch(object):
    
    def __init__(self):
        self.n = input("enter no of nodes in your graph")
        self.G = adjacencyList(self.n)
        self.G.createAdjList()
        self.color = [None]*(self.n+1)
        self.parent = [None]*(self.n+1)
        self.d = [None]*(self.n+1)
        self.f = [None]*(self.n+1)
        self.low = [1000]*(self.n+1)
        self.backedges=[]
        self.dfs_G = adjacencyList(self.n)
        for y in range(1,self.n+1):
            self.dfs_G.adjList[y] = adjacencyListNode(y)
        
    def dfs(self):
        for u in range(1,self.n+1):
            self.color[self.G.adjList[u].vertex] = 0                                     #0 - white
            self.parent[u] = None
        self.time = 0
        for head in range(1,self.n+1):
            if self.color[self.G.adjList[head].vertex] == 0:
                self.dfs_visit(self.G.adjList[head])
                
    def append_dfs_tree_node(self,u,v):   

        xe = adjacencyListNode(v)
        temp = self.dfs_G.adjList[u]
        self.dfs_G.degree[u] = self.dfs_G.degree[u] + 1  
        while temp.nextnode is not None:
            temp = temp.nextnode
        temp.nextnode = xe
              
    def dfs_visit(self,u):
        self.color[u.vertex] = 1                                                    #1 - gray
        self.time = self.time + 1
        self.d[u.vertex] = self.time
        v = self.G.adjList[u.vertex].nextnode

        while v is not None:
            #print v.vertex
            if self.color[v.vertex] == 0:    
                self.parent[v.vertex]  = u.vertex
                self.append_dfs_tree_node(u.vertex,v.vertex)
                self.dfs_visit(v)
            if self.parent[u.vertex] != int(v.vertex) and self.color[v.vertex] == 1 and u.vertex != v.vertex:
                    self.backedges.append((u.vertex,v.vertex))
            v = v.nextnode
        self.color[u.vertex] = 2                                                     #2 - black
        self.f[u.vertex] = self.time = self.time + 1 
        
       
if __name__ == '__main__':
    dfsearcher = depthfirstsearch()
    dfsearcher.dfs()
    leaves = []
    bridges = []
    print "The following adjacency list of the graph is taken as input"
    print dfsearcher.G
#    for i in range(1,dfsearcher.n+1):
#        print i,
#        print dfsearcher.parent[i],
#        print dfsearcher.d[i]
#        print dfsearcher.f[i]
    
#    print "\nbackedges:"
#    print dfsearcher.backedges 
#    print "\ndfs tree"   
#    print dfsearcher.dfs_G
    
    for i in range(1,dfsearcher.G.n+1):
        if dfsearcher.dfs_G.degree[i] == 0:
            leaves.append(i)  
#    print "leaves"
#    print leaves  
    
                
    for l in leaves:
#        print "climbing the tree from %d" %(l)
        p = l
        all_children_not_known = 0
        while all_children_not_known == 0 and p is not None: 
            temp=[]
            
            v = dfsearcher.dfs_G.adjList[p].nextnode
            
            while v is not None:
                
                if dfsearcher.low[v.vertex] != 1000:
                    temp.append(dfsearcher.low[v.vertex])
                else:
                    all_children_not_known = 1
                    break
                v = v.nextnode
            if all_children_not_known == 1:
#                print "cannot do parent %d and above calcuations" %(p)
                continue    
            for be in dfsearcher.backedges:
                
                if be[0] == p:
                    temp.append(dfsearcher.d[be[1]]) 
            temp.append(dfsearcher.d[p])    
            dfsearcher.low[p] = min(temp)
            p = dfsearcher.parent[p]
            
#    print "low"
#    for i in range(1,dfsearcher.n+1):
#        print "node %d - low %d"%(i,dfsearcher.low[i])             
    
    for v in range(1,dfsearcher.n+1):
        if dfsearcher.d[v] == dfsearcher.low[v] and dfsearcher.parent[v] is not None:
            bridges.append([dfsearcher.parent[v],v])
    print "\nbridges"
    for b in bridges:
        print "%d------>%d"%(b[0],b[1]) 

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        