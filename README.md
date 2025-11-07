# Band-Protocol-Superman-Chicken-Rescue-Problem
Hi this is your candidate Phobphoomin Siriboon. 
Please kindly find the explanation to the solution in the code.

# Additionally, this is the solution explanation: 

  Basically, We're doing a slidiing window technique here (it's an implementation of two pointers method) 

    IMPORTANT:  window size = chicken saved
    k = superman's carry limit

    Basically we use cur and iteration of i as two pointers and we'll keep expanding the windows only if "the sum of 'distance' of the latest cur and each iteration is less than k"
    If the distance is greater than k we record the highest we've got as "best" then we start over by delcaring new cur as the latest chickens[i] to start a new sliding window
    
    Once the loop is finished we will have the biggest window we can get that does not exceed k 
     which mean: The highest count of chicken saved without exceeding the roof. 

## Time Complexity BigO(n) and Memory Compelxity BigO(1)
