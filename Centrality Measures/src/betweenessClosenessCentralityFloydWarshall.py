
'''
Created on Jun 25, 2011

@author: Lokananda
'''
ipfile = open("fwinput.txt",'r')
 

class FloydWarshall(object):
    def __init__(self,n):
        self.n = n
        self.path = [None]*n
        for i in range(0,self.n):
            self.path[i]=[]
        self.next = [None]*n
        for i in range(0,self.n):
            self.next[i]=[None]*n
        
        
        
    def user_input(self):
        print "Adjacency matrix of input Graph:"
        for i in range(0,self.n):
            adjedges = ipfile.readline()
            j = 0
            try:    
                while(adjedges[j] != '\n'):
                    if j%2 == 0:
                        print int(adjedges[j]),
                        self.path[i].append(int(adjedges[j]))  
                    j = j+1
            except:
                pass 
            print 
#        for i in range(0,self.n):
#                for j in range (0,self.n):
#                    print self.path[i][j]
#                print   
    def FloydWarshallWithPathReconstruction (self):
        for k in range (0,self.n):
            for i in range(0,self.n):
                for j in range (0,self.n):
                    if int(self.path[i][k]) + int(self.path[k][j]) < int(self.path[i][j]):
                        
                        self.path[i][j] = int(self.path[i][k]) + int(self.path[k][j])
                        self.next[i][j] = k
            
 
    def GetPath (self,i,j):
        if self.path[i][j] == 2000:
            return "no path";
        
        intermediate = self.next[int(i)][int(j)]

        if intermediate == None:
            return "";             # there is an edge from i to j, with no vertices between */
        else:
            return self.GetPath(i,intermediate) + str(intermediate) + self.GetPath(intermediate,j)
        
class BetweenessCentrality:
    def __init__(self):
        
        self.n = input("enter no of vertices")
        self.shortestpath = [None]*self.n
        for i in range(0,self.n):
            self.shortestpath[i]=[None]*self.n
        for i in range(0,self.n):
            for j in range(0,self.n):
                self.shortestpath[i][j]=[]
        
        self.geodesiclengths = [0]*self.n
        
            
        fwbc = FloydWarshall(self.n)
        fwbc.user_input()
        fwbc.FloydWarshallWithPathReconstruction()
        j=0
        print
        for i in range(0,self.n):
            for j in range(0,self.n):
                print "shortest pat between %d and %d :" %(i,j),
                print fwbc.GetPath(i, j)
                if  fwbc.GetPath(i,j) != "":
                    x = int(fwbc.GetPath(i,j))
                    while x%10 != 0:
                        self.shortestpath[i][j].append(x%10)
                        x=x/10
        else:
            self.shortestpath[i][j].append(None)
        print "\ncalculated path matrix of given graph:\n"         
        for i in range(0,self.n):
                for j in range (0,self.n):
                    print fwbc.path[i][j],
                    if fwbc.path[i][j] != 9:
                        self.geodesiclengths[i] = self.geodesiclengths[i] + int(fwbc.path[i][j])
                    elif fwbc.path[i][j] == 9:
                        self.geodesiclengths[i] = self.geodesiclengths[i] 
                print
        
        
        
    
if __name__ == '__main__':
    
    f = BetweenessCentrality()
    bc = [0]*f.n
    for k in range(0,f.n):
        for i in f.shortestpath:
            for j in i:
                for u in j:
                    if u is None:             
                        break
                    if int(u) == k:
                        bc[k] = bc[k]+1
    print
    print "betweeness centrality measures:\n"
    for i in range(0,len(bc)):
        print "%d occurs in %d shortest paths" %(i,int(bc[i]))
    print 
    
    for i in range(0,len(bc)):
        print "betweeness centrality of %d is %d " %(i,int(bc[i]))
    print
    
    print "closeness centrality measure:\n"    
    for i in range(0,len(f.geodesiclengths)):
        print "closeness centrality of %d is %f" %(i,float(1)/f.geodesiclengths[i])
        
    print "\ncloseness centrality measure without inverse:\n"    
    for i in range(0,len(f.geodesiclengths)):
        print "closeness centrality of %d is %f" %(i,f.geodesiclengths[i])