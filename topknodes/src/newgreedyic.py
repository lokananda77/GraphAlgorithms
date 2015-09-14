'''
Created on 14-Jul-2011

@author: LOK
'''
import random
import copy
debug = 0
import networkx as nx
ipfile = open("ubinput1.txt",'r')
class adjacencyList(object):
    def __init__(self,no):
        self.n = no
        self.adjList=[None]*(self.n)
        
        
        
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
        self.nextnode = None
            
class GeneralGreedy(object):
    
    def randomactivity(self,p):
        if random.randrange(100) < ((1-p)*100):
            return 1
        else: 
            return 0
    
    
    def computeR(self):
        self.Rs = []
        self.R = [None]*self.no_nodes
        for j in range (0,len(self.R)):
            self.R[j]=[]
        for t in range (0,self.no_nodes):
            self.color = [None]*self.no_nodes
            self.dfs(adjacencyListNode(t))
        for x in self.seed:
            self.Rs.append(x.vertex)
            self.Rs.extend(self.R[x.vertex])
        self.Rs = list(set(self.Rs))
          
    def dfs(self,source):
        for u in range(0,self.no_nodes):
            self.color[self.Vg.adjList[u].vertex] = 0                                     #0 - white
#        for head in range(0,self.no_nodes):
#            if self.color[self.Vg.adjList[head].vertex] == 0:
#            self.dfs_visit(self.Vg.adjList[head])
        self.src = source.vertex
        if self.color[source.vertex] == 0:
            self.dfs_visit(source)
        return self.R      
    
    def append_dfs_tree_node(self,u,v):
        for seeds in self.seed:
            if u == seeds.vertex:
                self.Rs.append(v) 
        self.R[u].append(v)
                  
    def dfs_visit(self,u):
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
                self.dfs_visit(v)
            v = v.nextnode
        self.color[u.vertex] = 2 
        
    def remove_edge_from_graph_pb(self,p):
        self.Vg.adjList = [None]*self.no_nodes
        self.Vg.adjList=copy.deepcopy(self.V.adjList)
        temp = None
        prevtemp =None
        for u in self.Vg.adjList:
            v = u
            while v is not None:
                f = 0
                if self.randomactivity(p) == 1:
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
    
    def __init__(self):
        RT = 1000
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
        self.seed = []
        #p = float(raw_input("enter the propagation probabilty"))
        p=0.5
        print p
        #self.k = input("enter the k value")
        self.k = 4 
        for i in range(0,self.k):
            print "determining %dth seed" %(i+1)
            s=[0]*self.no_nodes
            for i in range(0,RT):
                self.Vg = adjacencyList(self.no_nodes)
                self.Vg = self.remove_edge_from_graph_pb(p)
                if debug == 1:
                    print self.Vg
                       
                self.computeR()  
                           
                if debug == 1:
                    print "these %d nodes will not affect score of seed " %(len(self.Rs))+str(self.seed)
                    print self.Rs
                for rech in self.R:
                    if debug == 1:
                        print rech
                for v in self.V.adjList:
                    flag = 0
                    for reached_from_seeds in self.Rs:
                        if v.vertex == reached_from_seeds:
                            flag = 1
                            break
                    if flag != 1:
                        s[v.vertex] = s[v.vertex] + len(self.R[v.vertex])
            for i in range(0,len(s)):
                s[i] = float(s[i])/RT                    
            print s
            maxs = max(s)
            print maxs
            j = 0
            for seedcontenders in s:
                if seedcontenders == maxs:
                    break
                j = j + 1
            print "appended %d as seed" %(j) 
            self.seed.append(self.V.adjList[j])
        print "results"
        for i in range(0,len(self.seed)):
            print self.seed[i].vertex
            
if __name__ =='__main__':
    GeneralGreedy()
        