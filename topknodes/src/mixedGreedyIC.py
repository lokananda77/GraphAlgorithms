import random
import operator
import copy
import timeit
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
    
    def remove_edge_from_graph_pb(self,p):
        self.Vg.adjList = [None]*self.no_nodes
        self.Vg.adjList=copy.deepcopy(self.V.adjList)
        temp = None
        prevtemp =None
        for u in self.Vg.adjList:
            v = u
            while v is not None:
                f = 0
                if self.randomactivity1(p) == 1:
                    if v is u:
                        self.Vg.adjList[u.vertex] = v   
                    else:
                        temp.nextnode = v.nextnode
                    f = 1
                prevtemp = temp
                if f == 0 or v is u:  
                    temp = v
                elif f == 1 and v is not u:
                    temp = prevtemp
                v = v.nextnode
        return self.Vg
    
    def randomactivity1(self,p):
        if random.randrange(100) < ((1-p)*100):
            return 1
        else: 
            return 0
    
    
    def computeR(self):
        self.R = [None]*self.no_nodes
        for j in range (0,len(self.R)):
            self.R[j]=[]
        for t in range (0,self.no_nodes):
            self.color = [None]*self.no_nodes
            self.dfs1(adjacencyListNode(t)) 
            
    def dfs1(self,source):
        for u in range(0,self.no_nodes):
            self.color[self.Vg.adjList[u].vertex] = 0                                     #0 - white
#        for head in range(0,self.no_nodes):
#            if self.color[self.Vg.adjList[head].vertex] == 0:
#            self.dfs_visit(self.Vg.adjList[head])
        self.src = source.vertex
        if self.color[source.vertex] == 0:
            self.dfs_visit1(source)
        return self.R      
    
    def append_dfs_tree_node(self,u,v):
        for seeds in self.seed:
            if u == seeds.vertex:
                self.Rs.append(v) 
        self.R[u].append(v)
                  
    def dfs_visit1(self,u):
        self.color[u.vertex] = 1                                                    #1 - gray
        v = self.Vg.adjList[u.vertex].nextnode
        while v is not None:
            if self.color[v.vertex] == 0:
                f = 0   
                for m in self.R[self.src]:
                    if m == v.vertex:
                        f=1
                        break
                if f !=1:
                    self.R[self.src].append(v.vertex)
#                self.append_dfs_tree_node(u.vertex,v.vertex)
                self.dfs_visit1(v)
            v = v.nextnode
        self.color[u.vertex] = 2
        
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
        R = 2000
        self.allnodes = []
        choice = raw_input("enter 1 for inputting from text file \nenter 2 for inputting karate club graph")
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
        #self.k = 4
        self.seed = []
       
        s=[0]*self.no_nodes
        for i in range(0,R):
                self.Vg = adjacencyList(self.no_nodes)
                self.Vg = self.remove_edge_from_graph_pb(0.5)
                self.computeR()
                for v in self.V.adjList:
                    s[v.vertex] = s[v.vertex] + len(self.R[v.vertex])
                        
        for u in self.allnodes:
            #print "updating mg for %d node" %(u[0])
            u[1] = float(s[u[0]])/R 
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
                newmg1 = 0
                for i in range(0,R):
                    newmg1 = newmg1 + self.rancas(self.V.adjList[u[0]])   
                u[1] = float(newmg1)/R
                print "mg1 %f  "%(u[1])            
            u[2] = len(self.seed)
            self.allnodes.append(u)  
        print "topknodes:"
        for s in self.seed:
            print s

if __name__ == '__main__':
    celf()    
            
             
        
        
            
            
            
        
