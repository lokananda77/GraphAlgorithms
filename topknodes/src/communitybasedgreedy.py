'''
Created on Jul 19, 2011

@author: sony
'''
class community_detection(object):
    j=0
    for v in self.V.adjList:
        label[u.vertex][0] = 0
        j = j +1
        u = v.nextnode
        while v is not None:
            k =0
            if isinfluence(self.V.adjList[v.vertex],self.V.adjList[u.vertex]):
                self.V.H[v.vertex][k] = 1
            else
                self.V.H[v.vertex][k] = 0
            u = v.nextnode
            
    for t in range (1,tau):
        for v in self.V.adjList:
            majority = {}
            temp = v.nextnode
            l = 0
            while temp is not None:
                if self.V.H.[temp.vertex][l] == 1:
                    majority[label[temp.vertex][t-1]] = majority[label[temp.vertex][t-1]] + 1
            label[u.vertex][t] =max(majority,key=majority.get) 
            v =v.nextnode
            l = l + 1
    
    self.L[]
            

               