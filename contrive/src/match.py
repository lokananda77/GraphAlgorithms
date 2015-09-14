#! /usr/bin/env python

import pickle
import sys

def usage():
    print "Usage \n\tmatch <player1_id> <player2_id>\
            \n\tplayer id is from 1 to n"
    sys.exit();

def toInt(string):
    try:
        return int(string)
    except:
        usage();

def main():
    if len(sys.argv)<3:
        usage();
    
    with open("player_list","r") as f:
        players = pickle.load(f);
        
    try:
        p1 = players[toInt(sys.argv[1])-1]
        p2 = players[toInt(sys.argv[2])-1]
    except IndexError:
        usage();
    print p1
    print p2
    p1_score = 0;
    p2_score = 0;
    for i in range(0,len(p1)):
        if (p1[i] > p2[i]):
            p1_score+=1;
        elif (p1[i] < p2[i]):
            p2_score+=1;
            
    with open("result","w") as f:
        
        if(p1_score > p2_score):
            f.write("won\n");
        elif p1_score < p2_score:
            f.write("lost\n");
        else:
            f.write("drew\n");
            
    with open("call_count","r") as f:
        n = toInt(f.readline().strip('\n'));
        
    n+=1;
    with open("call_count","w") as f:
        f.write(str(n));
        
        
        
    return

if __name__ == '__main__':
    main()

