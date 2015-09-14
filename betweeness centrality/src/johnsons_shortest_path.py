'''
Created on Jun 22, 2011

@author: lokananda
'''
import fibonacciheap
ipfile = open("input.txt",'r') 

class adjacencyList(object):
    def __init__(self,no):
        self.n = no
        self.adjList=[None]*self.n
    
    def createAdjList(self):
        for j in range (0,self.n):
            #head = input("enter the head node")
            #plan to take the input  inseveral forms one such is this
            adjedges = ipfile.readline()
            countnegedg = 0
            head=int(adjedges[0])
            i = 0
            p = 0            
            while(adjedges[i] != '\n'):
                i = i+1
                
                if (i - 3-countnegedg) % 6 == 0 and p != 1:
                    if adjedges[i+2] != '-':
                        if countnegedg != 0:
                            p=p+1
                        xe = adjacencyListNode(adjedges[i],adjedges[i+2])
                    else:
                        p=p+1
                        countnegedg = countnegedg + 1
                        xe = adjacencyListNode(adjedges[i],-1*int(adjedges[i+3]))
                        
                    if self.adjList[head] is None:
                        self.adjList[head] = xe
                    else:                            
                        temp = self.adjList[head]
                        while temp.nextnode is not None:
                            temp = temp.nextnode
                        temp.nextnode = xe
                        
    def appendAdjList(self,Gm):
        Gm.adjList=[]
        Gm.adjList.extend(self.adjList)
        Gm.adjList.append(None)
        head = self.n
        for i in range(0,self.n):
            xe = adjacencyListNode(i,0)
            if Gm.adjList[head] is None:
                Gm.adjList[head] = xe
            else:                            
                temp = Gm.adjList[head]
                while temp.nextnode is not None:
                    temp = temp.nextnode
                temp.nextnode = xe

        return Gm        
        
    def __str__(self):
        if self.adjList is None:
            return "<empty graph>"
        else:
            strgraph = ""
            for i in range(0,self.n):
                strgraph =strgraph+str(i)
                temp = self.adjList[i]
                while temp is not None:
                    strgraph=strgraph+"-->"+str(temp.vertex)+"("+str(temp.edgecost)+")"
                    temp = temp.nextnode
                strgraph = strgraph + "\n"
        return strgraph 
    
class adjacencyListNode(object):
    def __init__(self,key,cost):
        self.vertex = key
        self.edgecost = cost
        self.nextnode = None

class johnsonsAllPairsShortestPath(object):
    
    def __init__(self,n):
        
        #self.distD = fibonacciheap.fiboheap(n)
        self.distB = fibonacciheap.fiboheap(n+1)
        self.n = n
#        self.shortestpath = [None]*(n-1) 
        self.shortestpath = [None]*(n)
        for i in range (0,n):
            self.shortestpath[i]=[None]*n
        for i in range (0,n):
            for j in range (0,n):
                self.shortestpath[i][j]=[]
                  
                
    def initialise_single_source_dij(self,G,S):
        
        self.distD = fibonacciheap.fiboheap(G.n)
        for i in range(0,G.n):
            if i != int(S):
                #print "dij inserting"+str(i)
                self.distD.fiboHeapInsert(i,2000)        
        self.distD.fiboHeapInsert(int(S),0)
        
    def initialise_single_source_bel(self,G,S):
        for i in range(0,G.n):
            #print "inserting"+str(i)
            if i != int(S):
                #print "bell inserted"+str(i)
                self.distB.fiboHeapInsert(i,2000)        
        self.distB.fiboHeapInsert(int(S),0)
    
    
    def djikstra(self,G,S,V):
        self.initialise_single_source_dij(G,S)
        parent = [None]*G.n
        for i in range(0,G.n):
            u = self.distD.fiboHeapExtractMin()
            #print self.distD
            #print "min vertex "+str(u.vertex)+" its cost "+str(u.cost)
            if int(V) == int(S):
                parent[V]=int(V) 
                
            if int(u.cost) ==  2000:
                #print "breaking"
                self.shortestpath[S][int(V)].append(None)
                print
                return 0
                break
            #code for storing shortest path
#            self.shortestpathcost[V.vertex] = self.shortestpathcost[V.vertex] + u.cost
#            if int(u.vertex) == int(V.vertex):
            
            if int(u.vertex) == int(V):
                spath = int(V)
                print spath,
                while parent[spath] != int(S):
                    spath = parent[spath] 
                    print spath,
                    self.shortestpath[S][int(V)].append(spath)
                print parent[spath]
                return 1
                break
            v = G.adjList[u.vertex]
            while v is not None :
                new_cost = u.cost + int(v.edgecost)
                if self.distD.vertexlist[int(v.vertex)].cost > new_cost:
                    self.distD.fiboHeapDecreaseKey(v, new_cost)
                    parent[int(v.vertex)] = int(u.vertex) 
                    #print "after decrease key"
                    #print self.distD
                      
                v = v.nextnode
                
        self.shortestpath[S][int(V)].append(None)
        return 0
                
    def bellman_ford(self,Gm,S):
        self.initialise_single_source_bel(Gm,S)
        for u in range(0,Gm.n):
            print u
        #parent = [None]*(Gm.n-1)
        for i in range(0,Gm.n-1):
            for u in range(0,Gm.n):
                v = Gm.adjList[u]
                while v is not None:
                    new_cost =  self.distB.vertexlist[u].cost + int(v.edgecost)
                    print "self.distB.vertexlist[int(%d.vertex)].cost (= %d) > new_cost(self.distB.vertexlist[%d].cost (=%d) + int(%d.edgecost)(%d) ?" %(int(v.vertex),self.distB.vertexlist[int(v.vertex)].cost,u,self.distB.vertexlist[u].cost,int(v.vertex),int(new_cost))
                    if self.distB.vertexlist[int(v.vertex)].cost > new_cost:
                        self.distB.fiboHeapDecreaseKey(v, new_cost)
                        print "True"
                        #parent[v] = u
                        print "Now self.distB.vertexlist[int(v.vertex)].cost = "+str(self.distB.vertexlist[int(v.vertex)].cost)   
                    v=v.nextnode
        for i in range (0,Gm.n-1):
            try:
                self.delta[i] = self.distB.vertexlist[i].cost
            except:
                print "exception"
                print i
        print self.delta
        for u in range(0,Gm.n):
                v = Gm.adjList[u]
                while v is not None:
                    new_cost =  self.distB.vertexlist[u].cost + int(v.edgecost)
                    if self.distB.vertexlist[int(v.vertex)].cost > new_cost:  
                        return False   
                    v=v.nextnode 
        return True
                    
    
    
    
    def johnsons(self):
        #noofvertices = input("enter no of vertices")
        G = adjacencyList(self.n)
        G.createAdjList()
        print G
        self.delta = [None]*G.n
        self.h = [None]*G.n
        apsps = [None]*G.n
        Gm = adjacencyList(G.n+1)
        Gm = G.appendAdjList(Gm)
        for i in range(0,G.n):
            apsps[i]= []  
        S=Gm.n-1
        print "source of Bellman" +str(S)
        if self.bellman_ford(Gm,S) == False:
            print "Input graph has a negative cycle"
        else:
            for i in range(0,G.n):
                self.h[i] = self.delta[i]
            for u in range(0,G.n):
                v = G.adjList[u]
                while v is not None:
                    print "early"+str(int(v.edgecost))
                    v.edgecost = int(v.edgecost) + self.h[u] - self.h[int(v.vertex)]
                    print "after"+str(int(v.edgecost))
                    v = v.nextnode
            for u in range(0,G.n):
                
#                v = G.adjList[u]
#                
#                while v is not None:
                for v in range(0,G.n):                
                    print "finding the shortest path from%d to %d: " %(u,int(v)),        
                    path_existence=self.djikstra(G,u,v)
    #                while v is not None: 
    #                    apsps[u.vertex].append(self.shortestpathcost[v.vertex] + self.h(v.vertex) - self.h(u.vertex))
    #                for i in range (0,len(self.shortestpath)):
    #                    self.shortestpathcost[i] = None 
                
    #                while v is not None:
                    #if path_existence == 1:
                        #print "path exists between %d and %d \n"%(u,int(v))
#                        apsps[u].append(self.shortestpath[int(v.vertex)])
                        #print self.shortestpath
                    #else:
                        #print "no path exists between %d and %d \n"%(u,int(v))
#                        apsps[u].append(self.shortestpath[int(v.vertex)])
                        
#                    for i in range (0,len(self.shortestpath)):
#                        self.shortestpath[i] = None
                    #v = v.nextnode
        
       
#    def betweeness_centrality(self):
        
if __name__ == '__main__':
    noofvertices = input("enter no of vertices")
    sp = johnsonsAllPairsShortestPath(noofvertices)
    sp.johnsons()
    bc = [0]*noofvertices
    for k in range(0,noofvertices):
        for i in sp.shortestpath:
            for j in i:
                for u in j:
                    if u is None:             
                        break
                    if int(u) == k:
                        bc[k] = bc[k]+1
    print 
    for i in range(0,len(bc)):
        print "%d occurs in %d shortest paths" %(i,int(bc[i]))

            
    
#    for i in noofvertices:
#        for i in data:
#            for u in i:
#                for j in u:
#                    if j.vertex == i:
#                        bc[i] = bc[i]+1
#    for i in bc:
#        j = 0
#        print "%d occurs in %d shortest paths" %(j,bc)
#    G = adjacencyList(noofvertices)
#    G.createAdjList()
#    
#    print G
#    Gm = adjacencyList(noofvertices+1)
#    Gm = G.appendAdjList(Gm)
#    print Gm
    
         
        
    
