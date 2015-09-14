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
        
        
    def fibo_heap_min(self):
        return self.min
    
    def remove(self,x):
        z=self.root
        pre = z.left
        while z is not x:
            pre = z
            z = z.right
        pre.right=z.right
        z.right.left = pre    
        
        
        
    def fibo_heap_link(self,y,x):

        self.remove(y)
        if x.child is not None:
            x.child.left = y
            y.right = x.child
            if x.child.right is x.child:
                x.child.right = y
                y.left = x.child
            else:
                t=x.child
                while t.right is not x.child:
                    t = t.right
                t.right = y
                y.left = t 
            x.child = y
        else:
            x.child = y
            x.child.right = y
            x.child.left = y
        y.parent = x
        x.degree = x.degree + 1
        y.mark = False
        
        
    def consolidate(self):
        
        A=[None]*(int(D(self.N)))
        w = self.min
        g = w.left
        f=0
        while w is not g:
            f=1 
            x = w
            w = w.right
            d = x.degree
            while A[d] is not None:
                y = A[d]
                if x.cost > y.cost:
                    x,y = y,x
                if y is self.min:
                    if self.min.right is not None:
                        self.min=self.root = self.min.right
                    else:
                        self.min=self.root = self.min.left        
                else: 
                    self.root = self.min
                self.fibo_heap_link(y,x)
                A[d] = None
                d = d+1   
            A[d] = x
        if f is 1:
            x = w
            d = x.degree
            while A[d] is not None:
                y = A[d]
                if x.cost > y.cost:
                    x,y = y,x
                if y is self.min:
                    if self.min.right is not None:
                        
                        self.min=self.root = self.min.right
                        
                    else:
                        
                        self.min=self.root = self.min.left
                        if debug ==1:
                            print self.min.cost
                            if self.min is None:
                                print "a min not there"
                else:
                    
                    self.root = self.min
                self.fibo_heap_link(y,x)
                A[d] = None
                d = d+1
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
  
        for i in range (0,int(D(self.N))):
            if A[i] is not None:
                if self.min is None:
                    self.min = A[i]
                if self.min is None or A[i].cost < self.min.cost:
                    self.min = A[i]
                          
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
#       
        if self.min is None:
            self.min = x
        x.right = self.min
        self.min.left.right = x
        x.left = self.min.left
        self.min.left = x
        
        if self.min is None or x.cost < self.min.cost:
            self.min = x
        self.N = self.N + 1 
        self.vertexlist[ver] = x
      
    def fiboHeapExtractMin(self):
        z = self.min 
        f = 0 
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
                    g.left.right = self.min.right
                    self.min.right.left=g.left
                    g.left=self.min.left
                    self.min.left.right=g
                else:
                    f = 1
                    self.min=g
                    return z
            else:
                self.min.left.right=self.min.right 
                self.min.right.left=self.min.left    
            if f is not 1:
                del self.min
        if z is z.right and z.child is  None:
            self.min = None
        elif f is not 1:
            self.min = z.right
            self.consolidate()
        self.N = self.N-1  
        return z
    
    def CUT(self,x,y):
        z = y.child
        while z is not x:
            z = z.right
        z.left.right = z.right
        z.right.left = z.left
        del z   
        y.degree = y.degree -1
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
        z = y.left
        strl =""
        while y is not z:
            strl = strl + str(y.vertex)+"("+str(y.cost)+") "
            y = y.right
        strl=strl+str(y.vertex)+"("+str(y.cost)+") "
        return strl
    
                