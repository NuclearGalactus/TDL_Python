import numpy as np;
import sys;

SIZE = 5;

weights = np.zeroes(SIZE);
predictions = np.zeroes(SIZE);
currentPos = 2;
cues[8] = 1;
for i in range(REWARDT,NUM):
    rewards[i] = 1;

def trial():
    while(currentPos != 6 && currentPos != -1):
        choice = bool(random.getrandbits(1));
        if(choice){
            currentPos++;
        }else{
            currentPos--;
        }
        predictions
        
        	
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

	
