
#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
		
		if not arr:
		    return 0
		else :
    		max_Product = arr[0]
    		min_Product = arr[0]
    		result = arr[0]
    		
    		for i  in range(1,len(arr)):
    		    
    		    maxp = max( arr[i] , arr[i]*max_Product , arr[i]*min_Product )
    		    minp = min(arr[i] , arr[i]*max_Product , arr[i]*min_Product )
    		    
    		    max_Product = maxp
    		    min_Product = minp
    		    result= max(result , max_Product)
    		    
    		return result
		 
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends
