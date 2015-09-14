'''
Created on 14-Jul-2011

@author: LOK
'''
import operator
import timeit
import networkx as nx


class adjacencyList(object):
    def __init__(self,no):
        self.n = no
        self.adjList=[None]*(self.n)
        self.degree = [0]*(self.n)
        
        
    def createAdjList1(self):
        ipfile = open("C:/Users/sony/workspace/topknodes/src/ubinput1.txt",'r')
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
        
class degreediscount(object):
    
    def __init__(self):
        
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
        self.dd = [0]*self.no_nodes
        j = 0
        for i in range(0,len(self.dd)):
            self.dd[i] = [j,0]
            j = j+1
        self.nbor = [0]*self.no_nodes
        self.p = float(raw_input("enter the propagation probability"))
        self.k = input("enter the k value for determining top-k nodes")
        self.k = 4
        for u in self.V.adjList:
            #print u.vertex
            v = u.nextnode
            while v is not None:
                self.V.degree[u.vertex] = self.V.degree[u.vertex] + 1
                self.dd[u.vertex][1] = self.V.degree[u.vertex]  
                v = v.nextnode
        print self.dd
        for i in range(0,self.k):
            print
            print
            print sorted(self.dd, key=operator.itemgetter(1), reverse=True)
            u = sorted(self.dd, key=operator.itemgetter(1), reverse=True)[0]
            self.dd.remove(u)
            print "selected"+str(u)
            self.seed.append(u[0])
            v = self.V.adjList[u[0]].nextnode
            print "neighbours of %d are:" %(u[0]),
            while v is not None:
                
                self.nbor[v.vertex] = self.nbor[v.vertex] + 1
                
                try:
                    self.dd[v.vertex][1] = self.V.degree[v.vertex] - 2*self.nbor[v.vertex] - (self.V.degree[v.vertex]-self.nbor[v.vertex])*self.nbor[v.vertex]*self.p
                except:
                    pass
                v = v.nextnode
        print "\nThe top %d nodes are" %(self.k)    
        for i in range(0,self.k):
            print self.seed[i]

if __name__ == '__main__':
    degreediscount()   
             
            
          
            
        
          
            
        