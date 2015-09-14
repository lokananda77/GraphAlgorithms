#! /usr/bin/env python

import pickle

score = [];
rank = [];

def toInt(string):
    try:
        return int(string)
    except:
        print "Something evil happened! Check the output files if they conform to the specified format"


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
def compare(x,y):
    x-=1
    y-=1
    if(score[x] > score [y]):
        return -1;
    if(score[x] < score[y]):
        return 1;
    else:
        return 0;

def get_abs_rank():
    global score,rank;
    with open("player_list","r") as f:
        players = pickle.load(f);
    
    #Get the scores of players
    score = [0]*len(players);
    for i in range(0,len(players)):
        for j in range(i,len(players)):
            res = match(players[i],players[j])
            score[i]+=res;
            score[j]-=res;
           
    rank = range(1,len(players)+1)
    rank.sort(compare)
        
def correlation(X,Y):
    sx = sum(X);
    sy = sum(Y);
    sxx = sum([x*x for x in X]) 
    syy = sum([y*y for y in Y])
    sxy = sum([x*y for (x,y) in zip(X,Y)])
    n = len(X);

    
    return float(n*sxy - sx*sy)/(((n*sxx-sx*sx)*(n*syy-sy*sy))**0.5)
  
    
    
def main():    
    global rank,score;
    get_abs_rank();
    #print score;
    print rank;
    n = len(rank);
    in_rank=[];
    with open("rank_list","r") as f:
        for line in f:
            in_rank.append(toInt(line.strip('\n')))
    print in_rank
    with open("call_count","r") as f:
        matches = toInt(f.readline().strip('\n'))
    #compute Pearson Correlation 
    r1 = correlation(rank,in_rank)
    r2 = correlation(rank[:n/2],in_rank[:n/2])
    r3 = correlation(rank[:n/4],in_rank[:n/4])
    
    r = (r1+r2+r3)/3;
    pairs = n*(n+1)/2;
    print r
    print float(pairs-matches)/float(pairs)
    print 100*r*(pairs-matches)/pairs

if __name__ == "__main__":
    main()
