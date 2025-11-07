#Time Complexity of BigO(n) and Memory Complexity of BigO(1)


def superman_chicken_rescue(n,k,chickens): 
  
    #Basically, We're doing a slidiing window technique here (it's an implementation of two pointers method) 

    #IMPORTANT:  window size = chicken saved
    # k = superman's carry limit

    #Basically we use cur and iteration of i as two pointers and we'll keep expanding the windows only if "the sum of 'distance' of the latest cur and each iteration is less than k"
    #If the distance is greater than k we record the highest we've got as "best" then we start over by delcaring new cur as the latest chickens[i] to start a new sliding window



    #Once the loop is finished we will have the biggest window we can get that does not exceed k 
    # which mean: The highest count of chicken saved without exceeding the roof. 

    #Initliazing cur as the first pointer
    #count as the current window size
    #best as the highest window size

    cur = chickens[0] 
    count = 1
    best = 1

    #loop starts at 1 instead of 0 because cur is already the index of 0 
    #iteration i is the second pointer
    for i in range(1,n): 
       
        #if the window size is equal or less than k (superman's limit) we can save more chicken
        if (chickens[i] - cur + 1 <= k): 
            count += 1
            #compare the number of chicken saved with the highest number of chicken saved
            best = max(best,count)
        else: 
            #if the window size (number of chicken saved) exceeds k we start counting again from 1 with the latest iteration as the chicken's position
            cur = chickens[i]
            count = 1
     
        
    #return the highest record of window size (chicken saved)
    return best

print(superman_chicken_rescue(5, 5, [2, 5, 10, 12, 15]))

print(superman_chicken_rescue(5,5,[2,5,10,12,15]))
