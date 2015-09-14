'''
Created on Jun 25, 2011

@author: sony
'''
ipfile = open("fwinput.txt",'r')
 

class FloydWarshall(object):
    def __init__(self,n):
        self.n = n
        self.path=[None]*n
        for p in self.path:
            p = []
        
        
    def user_input(self):
        adjedges = ipfile.readline()
        for i in range(0,self.n):
            j = 0
            while(adjedges[j] != '\n'):
                if j%2 == 0:
                    self.path[i][j] = int(adjedges[j])  
                j = j+1 
            
    def FloydWarshallWithPathReconstruction (self):
        for k in range (1,self.n):
            for i in range(1,self.n):
                for j in range (1,self.n):
                    if self.path[i][k] + self.path[k][j] < self.path[i][j]:
                        self.path[i][j] = self.path[i][k] + self.path[k][j]
                        next[i][j] = k
                 
 
    def GetPath (self,i,j):
        if self.path[i][j] == 2000:
            return "no path";
            intermediate = next[i][j];
            if intermediate == None:
                return " ";             # there is an edge from i to j, with no vertices between */
        else:
            return self.GetPath(i,intermediate) + intermediate + self.GetPath(intermediate,j)
        
class BetweenessCentrality:
    def __init__(self):
        n = input("enter no of vertices")
        fwbc = FloydWarshall(n)
        fwbc.user_input()
        fwbc.FloydWarshallWithPathReconstruction()
        for i in range(0,self.n):
            for j in range(0,self.n):
                print fwbc.GetPath(i, j)
                
                
   
