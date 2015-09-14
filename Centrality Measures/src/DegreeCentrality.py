'''
Created on Jun 28, 2011

@author: Lokananda
'''


ipfile = open("fwinput.txt",'r')
import numpy 

class DegreeMeasurer(object):
    def __init__(self,n):
        self.n = n
        self.path = [None]*n
        for i in range(0,self.n):
            self.path[i]=[]
        self.degree = [0]*n
        self.indegree = [0]*n
        self.weight = [0]*n
        self.inweight = [0]*n
            
    def user_input(self):
        for i in range(0,self.n):
            adjedges = ipfile.readline()
            j = 0
            try:    
                while(adjedges[j] != '\n'):
                    if j%2 == 0:
                        self.path[i].append(int(adjedges[j]))  
                    j = j+1
            except:
                pass 
#        for i in range(0,self.n):
#                for j in range (0,self.n):
#                    print self.path[i][j]
#                print   
    def determineDegree (self):
        for i in range(0,self.n):
            for j in range (0,self.n):
                
                if int(self.path[i][j]) != 0 and int(self.path[i][j]) != 9:
                    self.degree[i] = self.degree[i] + 1
    
    def determineInDegree (self):
        for i in range(0,self.n):
            for j in range (0,self.n):
                
                if int(self.path[j][i]) != 0 and int(self.path[j][i]) != 9:
                    self.indegree[i] = self.indegree[i] + 1 
                    
    def determineDegreeForWeightedGraph (self):
        for i in range(0,self.n):
            for j in range (0,self.n):
                if int(self.path[i][j]) != 0 and int(self.path[i][j]) != 9:
                    self.degree[i] = self.degree[i] + 1 
                    self.weight[i] = self.weight[i] + self.path[i][j]
                if int(self.path[j][i]) != 0 and int(self.path[j][i]) != 9:
                    self.indegree[i] = self.indegree[i] + 1 
                    self.inweight[i] = self.inweight[i] + self.path[j][i]
 
    
        
class DegreeCentrality:
    def __init__(self):
        
        self.n = input("enter no of vertices")
   
        fwbc = DegreeMeasurer(self.n)
        fwbc.user_input()
         
        yno=raw_input("Is your graph weighted?")
        if yno == "n":
            fwbc.determineDegree()
            fwbc.determineInDegree()
            for i in range(0,self.n):
                print "degree centrality of %d is %f" %(i,fwbc.degree[i])
        else:
            fwbc.determineDegreeForWeightedGraph()
            for i in range(0,self.n):
                try:
                    print fwbc.weight[i]
                    print "degree(node strength) centrality of %d is %f" %(i,fwbc.degree[i]*float(fwbc.weight[i])/fwbc.degree[i])
                except:
                    print "degree(node strength) centrality of %d is %f" %(i,fwbc.weight[i])
                
        
#        dyno=raw_input("is your graph directed?")
#        if dyno =="y":
        print "\n Activity \n"
        for i in range(0,self.n):
            if yno == "n":
                print "outdegree centrality(activity) of %d node is %f" %(i,fwbc.degree[i])
            else:
                try:
                    print "outdegree centrality(activity) of %d node is %f" %(i,fwbc.degree[i]*float(fwbc.weight[i])/fwbc.degree[i])
                except:
                    print "outdegree centrality(activity) of %d node is %f" %(i,fwbc.weight[i])
                
        print "\n Popularity \n"
        
        for i in range(0,self.n):
            if yno == "n":
                
                print "indegree centrality(populaity) of %d node is %f" %(i,fwbc.indegree[i])
            else:
                try:
                    print "indegree centrality(activity) of %d node is %f" %(i,fwbc.indegree[i]*float(fwbc.inweight[i])/fwbc.indegree[i])
                except:
                    print "indegree centrality(activity) of %d node is %f" %(i,fwbc.inweight[i])
#        else:
#            print "popularity and activity cannot be determined for undirected "
                     
                 
        """could also code for popularity and activity """
        
        
    
if __name__ == '__main__':
    
    f = DegreeCentrality()
    
        