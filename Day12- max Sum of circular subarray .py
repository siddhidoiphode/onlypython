#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.

def circularSubarraySum(arr):
    ##Your code here
    if not arr:
        return 0
    
    minSum = maxSum =arr[0]
    totalSum = currMin = currMax =0
    
    for i in range(len(arr)):
    
        n=arr[i]
        
        currMin = min( n , n+currMin )
        minSum= min(minSum , currMin)
        
        currMax = max(n , n+currMax)
        maxSum = max(maxSum , currMax)
        
        totalSum += n
        
    normalSum = maxSum
    circularSum = totalSum - minSum
    
    if totalSum == minSum :
        return normalSum
    
    return max(circularSum , normalSum)
    
    
    
    
    
    
