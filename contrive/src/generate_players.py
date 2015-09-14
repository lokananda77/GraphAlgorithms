#! /usr/bin/env python

import random
import sys
import pickle

def usage():
    print "Usage \n\t generate_players <number_of_players>"
    sys.exit();

def toInt(string):
    try:
        return int(string)
    except:
        usage();
def main():
    if len(sys.argv)<2:
        usage();
        
    n = toInt(sys.argv[1])
    players = [];
    for i in range(0,n):
        players.append([]);
        for j in range(0,10):
            players[i].append(random.randint(0,10));
            
    with open("player_list","w") as f:
        pickle.dump(players,f);
        
    with open("call_count","w") as f:
        f.write("0");
        
    return
    
if __name__ == '__main__':
    main()
    
