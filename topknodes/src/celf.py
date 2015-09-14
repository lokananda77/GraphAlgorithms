import random
import operator
                   
import networkx as nx
class adjacencyList(object):
    def __init__(self,no):
        self.n = no
        self.adjList=[None]*(self.n)
        self.degree = [0]*(self.n)
        
    def createAdjList1(self):
        ipfile = open("ubinput1.txt",'r')
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
                    
    def createAdjList2(self):
        self.G = nx.generators.social.karate_club_graph()
        temp=nx.convert.to_dict_of_lists(self.G)
        for i in temp:
            head=int(i)
            xe = adjacencyListNode(int(i))
            self.adjList[int(i)] = xe
            
            for t in temp[i]:
                xe = adjacencyListNode(int(t))
                tmp = self.adjList[head]
                while tmp.nextnode is not None:
                    tmp = tmp.nextnode
                tmp.nextnode = xe        
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
        R = 200
        choice = raw_input("enter 1 for inputting from text file \nenter 2 for inputting karate club graph")
        self.allnodes = []
        
        if choice == "1":
            self.no_nodes = input("enter the no of nodes in the graph")
            self.V = adjacencyList(self.no_nodes)
            self.V.createAdjList1()
        elif choice == "2":
            self.no_nodes = 34
            self.V = adjacencyList(self.no_nodes)
            self.V.createAdjList2()
        print self.V
        for i in range(0,self.no_nodes):
            queNode(i)
            self.allnodes.append([queNode(i).vertex,queNode(i).mg1,queNode(i).flag])
        self.k = input("enter the k value")
        self.seed = []
       
        for u in self.allnodes:
            print "updating mg for %d node" %(u[0])
            mg =0
            for i in range(0,R):
                mg = mg + self.rancas(self.V.adjList[u[0]])
            u[1] = float(mg)/R    
            u[2] = 0 
       
        while len(self.seed) < self.k:
            print
            for al in self.allnodes:
                print al
            u=sorted(self.allnodes, key=operator.itemgetter(1), reverse=True)[0]
            self.allnodes.remove(u)  
            if u[2] == len(self.seed):
                print "appending %d as its mg is %f its flag is %d" %(u[0],u[1],u[0])
                self.seed.append(u[0])
                continue 
            else:
                print "picked up %d recalculating its marginal values as" %(u[0]),
                newmg = 0
                for i in range(0,R):
                    newmg = newmg + self.rancas(self.V.adjList[u[0]])   
                u[1] = float(newmg)/R
                print "mg %f  "%(u[1])            
            u[2] = len(self.seed)
            self.allnodes.append(u)  
        print "topknodes:"
        for s in self.seed:
            print s

if __name__ == '__main__':
    celf()    
            
             
        
        
            
            
            
        
