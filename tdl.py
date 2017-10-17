import numpy as np;
import sys;
LENGTH = 8;
INTERVAL = 0.5;
NUM = int(LENGTH / INTERVAL);
REWARDT = 12;


values = np.zeros((NUM));
perr = np.zeros((NUM));
weights = np.zeros((NUM));
rewards = np.zeros((NUM));
cues = np.zeros(NUM);
cues[8] = 1;
for i in range(REWARDT,NUM):
    rewards[i] = 1;

def trial():
    for i in range(0,NUM-1):
        perr[i] = (values[i+1] - values[i] + rewards[i]);
        
        	
    print("Values:  ",end='');
    print(values);
    print("PredErr: ",end='');
    print(perr);
    print("Weights: ",end='');
    print(weights);
    print("Rewards: ",end='');
    print(rewards);

def run():
    currVal = "";
    while(currVal != "done"):
        currVal = input("Awaiting Input:").lower();
        if(currVal == "run"):
             print("Ran 1 trial!");
             trial();
run();

	
