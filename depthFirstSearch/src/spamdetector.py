'''
Created on 10-Jul-2011

@author: LOK
'''
import time
import threading
from datetime import datetime
ipfile = open("offlinemails.txt",'r')

class TaskThread(threading.Thread):
    def __init__(self,function,interval,args=[]):
        threading.Thread.__init__(self)
        self.finished = threading.Event()
        self.interval = interval 
        self.function = function
        self.args = args
        
    def shutdown(self):
        self._finished.set()
        
    def run(self):
        while 1:
            if self.finished.isSet():return
            self.function(*self.args)
            self.finished.wait(self.interval)
        
        
    
class adjacencyList(object):
    def __init__(self,no):
        self.n = no
        self.adjList=[None]*(self.n+1)
        self.outlinkdegree = [0]*(self.n+1)
        self.markednodes = [None]*(self.n+1)
        self.nodescores = [0]*(self.n+1)
        self.nextround_markednodes = [None]*(self.n+1)
        self.no_m_nodes = 1
        
    def createAdjList(self):
        for j in range (1,self.n+1):
            temp=[]
            adjedges = ipfile.readline()
#            print adjedges
            temp = adjedges.split()
            head=int(temp[0])
            i = 0
            for t in temp:
                if i == 0:
                    xe = adjacencyListNode(int(t))
                    self.adjList[int(t)] = xe 
                else:
#                    tmp = t.split(str=",")
                    xe = adjacencyListNode(int(t))#(int(tmp[0]))#,int(tmp[1]))
                    xe.time = datetime.now()
                    xe.score = 1
                    f = 0
                    for k in range(1,self.n+1):
                     
                        if self.markednodes[k] is not None:
                            
                            if xe.node == self.markednodes[k].node:
                                f = 1
                                break
                    
                          
                    if f == 0:
                        
                        self.markednodes[self.no_m_nodes] = xe
                        self.nextround_markednodes[self.no_m_nodes]=xe
                        self.no_m_nodes = self.no_m_nodes + 1
                        
                        
                    temp = self.adjList[head]
                    self.outlinkdegree[head] = self.outlinkdegree[head] + 1
                    while temp.nextnode is not None:
                        temp = temp.nextnode
                    temp.nextnode = xe        
                i = i+1                        
           
                
                
    def __str__(self):
        if self.adjList is None:
            return "<empty graph>"
        else:
            strgraph = ""
            for i in range(1,self.n+1):
                temp = self.adjList[i]
                if temp is not None:    
                    strgraph =strgraph+str(temp.node)
                    temp = temp.nextnode
                    while temp is not None:
                        strgraph=strgraph+"-->"+str(temp.node)+"( time = "+str(temp.time.second)+")"+"( score = "+str(self.nodescores[temp.node])+")"
                        temp = temp.nextnode
                    strgraph = strgraph + "\n"
        return strgraph
    
    def appendEdgeToAdjList(self,time,sender_node,reciever_nodes):
        self.adjList.append(adjacencyListNode(sender_node))
        for reciever_node in reciever_nodes:
            head = reciever_node
            xe = adjacencyListNode(sender_node,time)                          
            temp = self.adjList[head]
            self.outlinkdegree[head] = self.outlinkdegree[head] + 1
            while temp.nextnode is not None:
                temp = temp.nextnode
            temp.nextnode = xe
            
    
    
    
class adjacencyListNode(object):
    def __init__(self,key=-1,time=None):
        self.node = int(key)
        self.time = time
        self.score = 0
        self.decayscore = 0
        self.nextnode = None

class message(object):
    def __init__(self,time):
        self.time = time
        

class Promail(object):
    def __init__(self):
        self.spams = 1
        self.hams =4
        self.tm = 20
        self.ti = 13
        self.pu = 4
        self.new_mail_time= None
        self.new_mail_sender=None
        self.new_mail_recievers=[]
        threads = []

        self.n = input("enter no of nodes in the offline email network")
        self.G = adjacencyList(self.n)
        self.G.createAdjList()
        print self.G
        
        self.RankMail()
        print self.G
        
        self.spam_thresh = self.find_spam_thresh()
        print self.spam_thresh
        thread1 = TaskThread(self.incoming_update,self.ti)
        threads.append(thread1)
        thread2 = TaskThread(self.periodic_update,self.pu)
        threads.append(thread2)
        thread3 = TaskThread(self.check_for_new_mail,2)
        threads.append(thread3)
        for i in range(0,2):
            threads[i].start()
        for i in range(0,2):
            threads[i].join()
            
    def find_spam_thresh(self):
        allnodes =[]
        for smtpnode in self.G.adjList:
            if smtpnode is not None:
                allnodes.append(smtpnode)
        newlist = sorted(allnodes,key=lambda x:self.G.nodescores[int(x.node)],reverse = False)
        for j in newlist:
            print "%d %f" %(j.node,self.G.nodescores[int(j.node)])
        return self.G.nodescores[newlist[self.spams-1].node]
        
    def incoming_update(self):
        time = self.new_mail_time
        if time is not None:
            self.G.appendEdgeToAdjList(time, self.new_mail_sender,self.new_mail_recievers)
            self.RankMail()
            print "appended new messages to mail social network"
            self.new_mail_time = None
        else:
            print "no new mail to append"
        print self.G
        self.find_spam_thresh()
        
    def periodic_update(self):
        print "periodic update carried out"
        self.time = datetime.now()
        print self.time.second
        self.delG()
        self.RankMail()
        print self.G
        
    def check_for_new_mail(self):
        yno = raw_input("activate a new message between nodes?")
        if yno=="y":
            self.new_mail_sender = input("enter the sender node:")
            self.new_mail_time = datetime.now()
            rec=raw_input("enter the recievers:")
            rc=rec.split()
            for r in rc:
                self.new_mail_recievers.append(int(r))
                print self.G.nodescores[self.new_mail_sender]
                print self.spam_thresh
            if self.G.nodescores[self.new_mail_sender]-self.spam_thresh <= 0.0:
                print "spam"
            else:
                print "not_spam"
        
        
    def delG(self):
        for list in self.G.adjList:
            nodes = list
            while nodes is not None:
                tmp = nodes
                nodes = nodes.nextnode
                if nodes is not None:
                    if (datetime.now()-nodes.time).seconds > self.tm:
                        self.delfromadjlist(nodes)
                    else:
                        continue
                    
                
    def delfromadjlist(self,n):
        for l in self.G.adjList:
            nodes = l
            
            if (l is not None and l.node == n.node):
                del l
                continue
            while nodes is not None:
                tmp = nodes
                nodes = nodes.nextnode
                if nodes is not None:
                    if (nodes.node == n.node):
                        tmp.nextnode = nodes.nextnode
                    else:
                        continue
                        
               
    def RankMail(self):
        time.sleep(1)
        d_factor = 0.5
        err_thresh = 0.0005
        tmp_link = adjacencyListNode()
        
        for i in range(1,len(self.G.markednodes)):
            self.G.markednodes[i] = None
        for i in range (1,len(self.G.nextround_markednodes)):
            self.G.markednodes[i] = self.G.nextround_markednodes[i]
            self.G.nextround_markednodes[i] = None
        j = 1
        for h in range(1,len(self.G.markednodes)):
            smtpnode = self.G.markednodes[h]
            if smtpnode is not None:
                tmp_nodescore = self.G.nodescores[int(smtpnode.node)]
                self.G.nodescores[int(smtpnode.node)] = 0
                inlink = self.G.adjList[smtpnode.node].nextnode
                while inlink is not None:
                    tmp_time = datetime.now() - inlink.time  
                    self.G.nodescores[int(smtpnode.node)] = self.G.nodescores[int(smtpnode.node)] + inlink.score * (d_factor**(tmp_time.microseconds/100000))
                    inlink.decayscore = inlink.score * (d_factor**(tmp_time.microseconds/100000))
                    inlink = inlink.nextnode
                try:
                    percent_diff_in_node_score = (self.G.nodescores[int(smtpnode.node)] - tmp_nodescore)/ tmp_nodescore
                except:
                    percent_diff_in_node_score = err_thresh + 1
                    
                if (percent_diff_in_node_score)  > err_thresh:
                        tmp_link.score = self.G.nodescores[int(smtpnode.node)] / self.G.outlinkdegree[smtpnode.node]
                        for i in range(1,len(self.G.adjList)):
    #                        print i
                            list = self.G.adjList[i]
                            link = list.nextnode 
                            while link  is not None:
                                if link.node == smtpnode.node:
                                    fla = 0
    #                                print "link.node "+str(link.node)
    #                                print "smtpnode.node "+str(smtpnode.node)
                                    outlink = link
                                    tmp_time = datetime.now() - outlink.time
                                    tmp_link.score = tmp_link.score * (d_factor**(tmp_time.microseconds/100000))
                                    outlink.score = tmp_link.score
                                    try:
                                        percent_diff_in_link_score = (tmp_link.score - outlink.decayscore)/outlink.decayscore
                                    except:
                                        percent_diff_in_link_score = err_thresh + 1
                                    if (percent_diff_in_link_score) > err_thresh:
                                        #print "j"+str(j)
                                        for k in range(1,len(self.G.markednodes)):
                                            if self.G.nextround_markednodes[k] is not None:
                                                if (self.G.nextround_markednodes[k].node == link.node):
                                                #print self.G.nextround_markednodes[k].node,
                                                    fla = 1
                                                    break
                                        
                                        if fla != 1:
                                            print "ready for marking" 
                                            self.G.nextround_markednodes[j] = link 
                                            print link.node                                 
                                            j = j+1                                
                                        outlink.decayscore = tmp_link.score
                                link = link.nextnode
        print "Nodes marked for nextround"
        for i in range (1,len(self.G.nextround_markednodes)):
            if self.G.nextround_markednodes[i] is not None:
                print self.G.nextround_markednodes[i].node,
        print
        
            
if __name__ == '__main__':
    Promail()
          
    
        
