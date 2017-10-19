import numpy as np;
import matplotlib.pyplot as plt

import sys;
LENGTH = 100;
INTERVAL = 1;
NUM = int(LENGTH / INTERVAL);
REWARDT = 80;
GAMMA = 0.9;

values = np.zeros((NUM));
perr = np.zeros((NUM));
weights = np.zeros((NUM));
rewards = np.zeros((NUM));
cues = np.zeros(NUM);
cues[8] = 1;
rewards[REWARDT] = 1;

def trial():
    for i in range(0,NUM-1):
        perr[i] = (GAMMA * (values[i+1] - values[i]) + rewards[i]);
        if(i > 20):
            weights[i] += 0.9 * perr[i];  
            values[i] = weights[i];
        	
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
             for i in range(0,600):
                 trial();
    plt.plot(np.arange(NUM),values)
    plt.plot(np.arange(NUM),weights)
    plt.plot(np.arange(NUM),perr)
    plt.ylabel('Values')
    plt.show()
run();
print("Program Terminated...Press enter to continue.");
input();
	
