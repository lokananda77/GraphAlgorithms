import random
import operator
import timeit
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

class queNode(object):
    def __init__(self,key):
        self.vertex = int(key)
        self.mg1 = None
        self.flag = None

        
        
                
class celf(object):
    def randomactivity(self):
        if random.randrange(100) < 50:
            return 1
        else: 
            return 0
        
    def rancas(self,seed_contend):
        self.color = [None]*self.no_nodes
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
    
    def dfs(self,v1):
        for u in range(0,self.no_nodes):
            self.color[self.V.adjList[u].vertex] = 0                                     #0 - white
        self.temp_no = 0
        for i in self.seed:
            self.dfs_visit(self.V.adjList[i],0)
        self.dfs_visit(self.V.adjList[v1.vertex],1)
        return self.temp_no        
              
    def dfs_visit(self,u,control):
        self.color[u.vertex] = 1                                                    #1 - gray
        v = self.V.adjList[u.vertex].nextnode
        while v is not None:
            if self.color[v.vertex] == 0:    
                if v.activity != 0:
                    if int(control) == 1:
                        self.temp_no = self.temp_no + 1 
                    self.dfs_visit(v,control)
            v = v.nextnode
    
    def __init__(self):
        
        
        self.no_nodes = 24
        self.V = adjacencyList(self.no_nodes)
        self.V.createAdjList()
        
    def calculate(self):
        #print self.V
        R = 1000
        self.allnodes = []
        for i in range(0,self.no_nodes):
            queNode(i)
            self.allnodes.append([queNode(i).vertex,queNode(i).mg1,queNode(i).flag])
        #self.k = input("enter the k value")
        self.k = 4
        self.seed = []
       
        for u in self.allnodes:
           # print "updating mg for %d node" %(u[0])
            mg1 =0
            for i in range(0,R):
                mg1 = mg1 + self.rancas(self.V.adjList[u[0]])
            u[1] = float(mg1)/R    
            u[2] = 0 
       
        while len(self.seed) < self.k:
            #print
#            for al in self.allnodes:
#                print al
            u=sorted(self.allnodes, key=operator.itemgetter(1), reverse=True)[0]
            self.allnodes.remove(u)  
            if u[2] == len(self.seed):
#                print "appending %d as its mg is %f its flag is %d" %(u[0],u[1],u[0])
                self.seed.append(u[0])
                continue 
            else:
#                print "picked up %d recalculating its marginal values as" %(u[0]),
                newmg1 = 0
                for i in range(0,R):
                    newmg1 = newmg1 + self.rancas(self.V.adjList[u[0]])   
                u[1] = float(newmg1)/R
#                print "mg1 %f  "%(u[1])            
            u[2] = len(self.seed)
            self.allnodes.append(u)  
#        print "topknodes:"
        for s in self.seed:
            print s

if __name__ == '__main__':
    t=timeit.Timer("cf.calculate()","import celftime;cf = celftime.celf()")
    trials = 5
    runtimes =[]
    #print t.timeit(trials)*1e6/float(trials)
    runtimes.append(t.timeit(trials)*1e6/float(trials))
    print runtimes    
            
             
        
        
            
            
            
        
