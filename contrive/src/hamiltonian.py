import pickle
import sys
count=0
flag=0        
def match(p1,p2):
    p1_score = 0;
    p2_score = 0;
    for i in range(0,len(p1)):
        if (p1[i] > p2[i]):
            p1_score+=1;
        elif (p1[i] < p2[i]):
            p2_score+=1;    
        if(p1_score > p2_score):
            return 1;
        elif p1_score < p2_score:
            return -1;
        else:
            return 0;
        
def fillgraph(n,k):
    global count,flag
    
    with open("player_list","r") as f:
        players = pickle.load(f);

    for i in range(k,len(players)+k):
        count=count+1
        if match(players[i-k],players[i%n])<0:
            path[i%n][i-k]=1
        else:
            path[i-k][i%n]=1
    for i in range(0,n):
        print path[i] 
           
    
class Hamiltonian():
    def __init__(self,path):
        self.n = len(path);
        self.pathSoFar=[]
        self.hp()    
        
        
    def hp(self):
        
        if len(self.pathSoFar) == self.n:
            self.printSolution()
            flag=1
            return 
        
        elif len(self.pathSoFar) == 0:
            for i in range (0,self.n):
                self.pathSoFar.append(i)
                
                self.hp()
                self.pathSoFar.remove(self.pathSoFar[len(self.pathSoFar)-1]);
        else:
            currentNode = self.pathSoFar[len(self.pathSoFar)-1];
            for i in range (0,self.n):
                if i not in self.pathSoFar:
                    if path[currentNode][i] != 0:
                        self.pathSoFar.append(i);
                        self.hp();
                        self.pathSoFar.remove(self.pathSoFar[len(self.pathSoFar)-1]);
        
                 
    
    def printSolution(self):
        ans=""
        for j in self.pathSoFar:
            ans=ans+str(j+1)+"\n"
        result=open('rank_list','w')
        result.write(ans)
        result.close
        
        ct=open('call_count','w')
        ct.write(str(count))
        ct.close

        sys.exit()


    
if __name__ == '__main__':
   
    n=int(sys.argv[1])
    path=[None]*n
    for i in range(0,n):
        path[i]=[0]*n
    i=1
    while(flag!=1):
        fillgraph(n,i)
        Hamiltonian(path)
        i=i+1
    
    
    
        
        
        
        
        
    

