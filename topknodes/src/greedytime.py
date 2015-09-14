'''
Created on 14-Jul-2011

@author: LOK
'''
import timeit
import random
ipfile = open("ubinput1.txt",'r')
class adjacencyList(object):
    def __init__(self,no):
        self.n = no
        self.adjList=[None]*(self.n)
        self.degree = [0]*(self.n)
        
        
    def createAdjList(self):
        for j in range (0,self.n):
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
            for i in range(0,self.n):
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
        self.acivity = None
        self.nextnode = None
            
class GeneralGreedy(object):
    def randomactivity(self):
        if random.randrange(100) < 50:
            return 1
        else: 
            return 0
        
    def rancas(self,seed_contend):
        marked_activity_nodes = {}
        for u in self.V.adjList:
            v  = u 
            while v is not None:
                try:
                    v.activity  = marked_activity_nodes[(v,u)]
                except:
                    v.activity = marked_activity_nodes[(u,v)] = self.randomactivity()
                v = v.nextnode
        n = self.dfs(seed_contend)
        return n 
    
    def dfs(self,v):
        for u in range(0,self.no_nodes):
            self.color[self.V.adjList[u].vertex] = 0                                     #0 - white
        self.temp_no = 0
        for i in self.seed:
            self.dfs_visit(self.V.adjList[i])
        self.dfs_visit(self.V.adjList[v.vertex])
        return self.temp_no        
              
    def dfs_visit(self,u):
        self.color[u.vertex] = 1                                                    #1 - gray
        v = self.V.adjList[u.vertex].nextnode
        while v is not None:
            if self.color[v.vertex] == 0:    
                if v.activity != 0:
                    self.temp_no = self.temp_no + 1 
                    self.dfs_visit(v)
            v = v.nextnode

    def __init__(self):
       
        #self.no_nodes = input("enter the no of nodes in the graph")
        self.no_nodes = 24
        self.V = adjacencyList(self.no_nodes)
        self.V.createAdjList()
        
    def calculate(self):
        #print self.V
        R = 2000
        self.seed = []
        self.k = 4
        #self.k = input("enter the k value")
        for i in range(0,self.k):
#            print "determining %dth seed" %(i)
            s=[0]*self.no_nodes
            for v in self.V.adjList:
                flag = 0
                for topk in self.seed:
                    if v.vertex == topk:
                        flag = 1
                        break
                if flag != 1:
#                    print "calculating s[%d]" %(v.vertex)
                    
                    for i in range(0,R):
                        self.color = [None]*self.no_nodes
                        s[v.vertex] = s[v.vertex] + self.rancas(v)
                    s[v.vertex] = float(s[v.vertex])/R
            #print s
            maxs = max(s)
            #print maxs
            j = 0
            for seedcontenders in s:
                if seedcontenders == maxs:
                    break
                j = j + 1
            #print "appended %d as seed" %(j) 
            self.seed.append(j)
        #print "results"
        for i in range(0,len(self.seed)):
            print self.seed[i]
            
if __name__ =='__main__':
    if __name__ =='__main__':
        t=timeit.Timer("cf.calculate()","import greedytime;cf = greedytime.GeneralGreedy()")
        trials = 5
        print t.timeit(trials)*1e6/float(trials)
        