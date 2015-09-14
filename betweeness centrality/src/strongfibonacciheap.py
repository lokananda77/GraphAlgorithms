'''
Created on Jun 23, 2011

@author: lokananda
'''
import math
import sys
#debug = 1
debug = 0
def D(x):
    return math.ceil(math.log(x)/math.log(2.0))

class fiboheapnode(object):
    def __init__(self):
        self.cost = None
        self.child = None
        self.parent = None  
        self.degree = 0      
        self.left =None
        self.right =None
        self.mark = False
        self.vertex = None
        
class fiboheap(object):
    def __init__(self,n):
        self.N = 0
        self.min = None
        self.root = None
        self.vertexlist = [None]*n
        print self.vertexlist
        
    def fibo_heap_min(self):
        return self.min
    
    def remove(self,x):
        z=self.root
        pre = z.left
        #print pre.cost
        while z is not x:
            pre = z
            z = z.right
            
        
        #print "deleted %d from rootlist " % x.cost
        #print "also made %d to point to %d instead of %d" % (pre.cost,z.right.cost,z.cost)
        pre.right=z.right
        z.right.left = pre    
        
        
        
    def fibo_heap_link(self,y,x):

        self.remove(y)
        #y.right=x.child

        if x.child is not None:
            x.child.left = y
            y.right = x.child
            if x.child.right is x.child:
                x.child.right = y
                y.left = x.child
            else:
                #print "h"
                t=x.child
                while t.right is not x.child:
                    #print"l"
                    t = t.right
                t.right = y
                y.left = t 
            #print "fitted %d between its siblings %d and %d" %(y.cost,y.left.cost,y.right.cost)
            x.child = y
        else:
            x.child = y
            x.child.right = y
            x.child.left = y
        y.parent = x
        x.degree = x.degree + 1
        y.mark = False
        #print "and appended %d as child of %d " %(y.cost,x.cost)
        
    def consolidate(self):
        
        A=[None]*(int(D(self.N)))
        #print "number of vertices in heap"+str(self.N)
        #print "A capacity %d" %(int(D(self.N)))
        w = self.min
        if debug == 6:    
            print "%d is curren min and on its left is %d" %(self.min.vertex,self.min.left.vertex)
            print "so this round goes in search of %d and stops after consolidating it" %(self.min.left.vertex)
        g = w.left
        #print "lookk 10 has siblingsa"+str(g.cost)
        f=0
        while w is not g:
            f=1 
            x = w
            if debug == 6:
                print "currently consolidating"+str(x.vertex)
            w = w.right
            d = x.degree
            #print "degree %d"%(d)
#            for li in A:
#                if li is not None:
#                    print str(li.cost) +" "+str(li.vertex)
#                else:   
#                    print "None"
#            print
            while A[d] is not None:
                
                y = A[d]
                if x.cost > y.cost:
                    x,y = y,x
                if debug ==1:
                        print self.min.cost
                        if self.min is None:
                            print "a min not there"
                if y is self.min:
                    if debug ==1:
                        print self.min.cost
                        if self.min is None:
                            print "a min not there"
                    if self.min.right is not None:
                        if debug == 6:
                            print " changing self.min and .root from %d to %d"%(self.min.vertex,self.min.right.vertex)
                        self.min=self.root = self.min.right
                    else:
                        if debug == 6:
                            print "changing self.min n .root from %d to %d"%(self.min.vertex,self.min.left.vertex)
                        self.min=self.root = self.min.left
                        if debug ==1:
                            print self.min.cost
                            if self.min is None:
                                print "haha min not there"
                else:
                    if debug == 6:
                        print "since min which is not goin to be del, root which was %d shall be %d the min" %(self.root.vertex,self.min.vertex )
                    self.root = self.min
                self.fibo_heap_link(y,x)
                A[d] = None
                d = d+1
                #print "degree %d"%(d)
            A[d] = x
        if f is 1:
            x = w
            if debug == 6:
                print "end currently consolidating"+str(x.vertex)
            d = x.degree
#            for li in A:
#                if li is not None:
#                    print str(li.cost) + " " + str(li.vertex)
#                else:   
#                    print "None"
#            print
            if debug ==1:
                        print self.min.cost
                        if self.min is None:
                            print "a min not there"
            while A[d] is not None:
                y = A[d]
                
                if x.cost > y.cost:
                    x,y = y,x
                
                
                if y is self.min:
                    if self.min.right is not None:
                        if debug == 6:
                            print "changing self.min and .root from %d to %d"%(self.min.vertex,self.min.right.vertex)
                        self.min=self.root = self.min.right
                        if debug ==1:
                            print self.min.cost
                            if self.min is None:
                                print "a min not there"
                    else:
                        if debug == 6:
                            print "changing self.min n .root from %d to %d"%(self.min.vertex,self.min.left.vertex)
                        self.min=self.root = self.min.left
                        if debug ==1:
                            print self.min.cost
                            if self.min is None:
                                print "a min not there"
                else:
                    if debug == 6:
                        print "since min which is not goin to be del root which was %d shall be %d the min" %(self.root.vertex,self.min.vertex )
                    self.root = self.min
                self.fibo_heap_link(y,x)
                #print "huhku"
                A[d] = None
                d = d+1
#                for li in A:
#                    if li is not None:
#                        print li.cost
#                    else:   
#                        print "Nonehfh"
#                print
            A[d] = x
        g=0
        for li in A:
                if li is not None:
                    g=1
                    break    
                else:   
                    g=0
        if g == 1:
            self.min = None
        
#        for li in A:
#                if li is not None:
#                    print li.cost
#                else:   
#                    print "None"
        
        for i in range (0,int(D(self.N))):

            if A[i] is not None:
                if self.min is None:
                    self.min = A[i]
  
                if self.min is None or A[i].cost < self.min.cost:
                    self.min = A[i]
    
        if debug ==1:
                    
                    if self.min is None:
                        print "a min not there"
    def fiboHeapInsert(self,ver,cost):

        x = fiboheapnode()
        x.degree = 0
        x.parent = None
        x.child = None
        x.left = x
        x.right = x
        x.mark = False
        x.cost = cost
        x.vertex = ver
#        concatenate the root list containing x with root list H
        if self.min is None:
            self.min = x
        x.right = self.min
        self.min.left.right = x
        x.left = self.min.left
        self.min.left = x
        
        if self.min is None or x.cost < self.min.cost:
            self.min = x
        self.N = self.N + 1
        print "inserted"+str(ver)
        self.vertexlist[ver] = x
     
    
    def fiboHeapExtractMin(self):
        z = self.min
#        print "self.min %d" %(z.cost)
        f = 0
#        if z.child:
#            print 1
#        else:
#            print 0
        try: 
            g= x = z.child
        except:
            self.fibo_heap_min()
            print "exception"
            sys.exit()
        if z is not None:
            if x is not None:
                x.parent = None
                if self.min.right is not self.min:
#                    print "bringing kids up to rootlist"
#                    print "by connecting %d to %d on right and" %(g.left.cost,self.min.right.cost)
#                    print "by connecting %d to %d on left and" %(self.min.left.cost,g.cost)
                
                    g.left.right = self.min.right
                    self.min.right.left=g.left
                    g.left=self.min.left
                    self.min.left.right=g
                    
                else:
                    f = 1
                    if debug == 3:
                        print "bringing kids up to rootlist and setting child as minimum"
                    self.min=g
                    if debug ==1:
                        if self.min is None:
                            print "a min not there"
                    #print "child"+str(g.cost)
                    return z
            else:
                self.min.left.right=self.min.right 
                self.min.right.left=self.min.left
                if debug ==1:
                        if self.min is None:
                            print "a min not there"
            if f is not 1:
                
                if debug ==1:
                    print self.min.cost
                    if self.min is None:
                        print "a min not there"
                del self.min
               
            
        if z is z.right and z.child is  None:
            
            self.min = None
            if debug ==1:
                if self.min is None:
                    print "a min not there"
        elif f is not 1:
            self.min = z.right
            #print "sgsg"
            if debug ==1:
                print self.min.cost
                if self.min is None:
                    print "b min not there"
            self.consolidate()
        self.N = self.N-1
        if debug ==1:
            if self.min is None:
                print "c min not there"
        return z
    
    def CUT(self,x,y):
        
        z = y.child
        while z is not x:
            z = z.right
        z.left.right = z.right
        z.right.left = z.left
        del z
        
         
        y.degree = y.degree -1
        if debug == 6:
            print "x = %d"%(x.vertex)
            print "resetting x's left point to = %d" %(self.min.left.vertex) 
#        x.left = self.min.left
#        x.right = self.min
#        self.min.left.right = x
#        self.min.left = x

        x.right = self.min.right
        x.left = self.min
        self.min.right.left = x
        self.min.right = x
        
        x.parent = None
        x.mark = False
    
     
    
    def CASCADINGCUT(self,y):
        z= y.parent
        if z is not None:
            if y.mark == False:
                y.mark= True
            else:
                self.CUT(y, z)
                self.CASCADINGCUT(z) 
    
    def fiboHeapDecreaseKey(self,x,k):
        if k > self.vertexlist[int(x.vertex)].cost:
            print "new cost is greater than current cost"
        self.vertexlist[int(x.vertex)].cost = k
        y = self.vertexlist[int(x.vertex)].parent
        if y is not None and self.vertexlist[int(x.vertex)].cost < y.cost:
            self.CUT( self.vertexlist[int(x.vertex)], y)
            self.CASCADINGCUT(y)    
        if self.vertexlist[int(x.vertex)].cost < self.min.cost:
            self.min = self.vertexlist[int(x.vertex)]
      
    
    def fiboHeapDelete(self,x):
        self.fiboHeapDecreaseKey(x,-2000)
        self.fiboHeapExtractMin()
        
    def __str__(self):
        y = self.min
        #print "self.min:"+str(y.cost)
        z = y.left
        strl =""
        
        #print "self.min"+str(y.cost)
        while y is not z:
        
            strl = strl + str(y.vertex)+"("+str(y.cost)+") "
            y = y.right
    
        strl=strl+str(y.vertex)+"("+str(y.cost)+") "
    
        return strl
    
#    def printheap(self,prevparent = None,z):
#        if z.child is None or z.child is (u for u in self.childs):
#            if z.parent is not prevparent:
#                s = z     
#            while s is not z.left:
#                if s.parent is not prevparent:
#                    strl ="\n parent(%d)(cost =%d)--->" %(s.parent.vertex,s.parent.cost)
#                else:
#                    strl = strl + "(%d)(cost =%d)--->)" %(s.vertex,s.cost)
#                    s = s.right
#                    self.printheap(s)
#            strl=strl+"(%d)(cost =%d)"%(s.vertex,s.cost)
#            prevparent = s.parent
#            self.childs.append(z.child)
#            return
#        else:
#            self.printheap(prevparent=z,z.child)
#            return
    
#        
#    
#        return strl

#if __name__ == '__main__':
#    H = fiboheap()
##    for i in range (0,10,2):
##        H.fiboHeapInsert(i)
#    
##    H.fiboHeapInsert(18,0)
##    H.fiboHeapInsert(2,0)
##    H.fiboHeapInsert(6,0)
##    H.fiboHeapInsert(13,0)
##    H.fiboHeapInsert(11,0)
##    H.fiboHeapInsert(7,0)
##    H.fiboHeapInsert(8,0)
##    H.fiboHeapInsert(10,0)
##    H.fiboHeapInsert(3,0)
##    H.fiboHeapInsert(12,0)
##    H.fiboHeapInsert(4,0)
##    H.fiboHeapInsert(17,0)
##    H.fiboHeapInsert(16,0)
##    H.fiboHeapInsert(5,0)
##    H.fiboHeapInsert(20,0)
##    H.fiboHeapInsert(30,0)
##    H.fiboHeapInsert(110,0)
##    H.fiboHeapInsert(70,0)
##    H.fiboHeapInsert(81,0)
##    H.fiboHeapInsert(111,0)
##    H.fiboHeapInsert(31,0)
##    H.fiboHeapInsert(120,0)
##    H.fiboHeapInsert(40,0)
##    H.fiboHeapInsert(107,0)
##    H.fiboHeapInsert(160,0)
##    H.fiboHeapInsert(50,0)
##    H.fiboHeapInsert(200,0)
##    H.fiboHeapInsert(300,0)
#    
#    print H
#    z = 1
#    y = 1
#    
#    z = H.fiboHeapExtractMin()
#        #print "end of round of extractmin"
##        try:
##            #print H
##        except:
##            print "exception"
#        #print "z.cost"
#    print "%d = %d" % (y,z.cost)
#    t=z.right
#    print "%d = %d" % (y,t.cost)
#    
#    
#        
#    H.fiboHeapDecreaseKey(t, 1)
#    print H
#    while z is not None:
#        z = H.fiboHeapExtractMin()
#        #print "fibo heap:"+str(H)
#    #print "end of round of extractmin"
##        try:
##            #print H
##        except:
##            print "exception"
#    #print "z.key"
#        print z.cost
#        
##def fiboHeapUnion(H1,H2):
##        H = fiboheap()
##        H.min = min[H1]
##        Concatenate the root list of H2 with the root list of H
##        if (min[H1] = NIL) or (min[H2] is not None NIL and min[H2] < min[H1])
##            min[H] := min[H2]
##        n[H] = n[H1] + n[H2]
##        free the objects H1 and H2
##        return H       
#            
#                    
#                   