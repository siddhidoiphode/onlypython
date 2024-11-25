class Solution:
    
    def maxProduct(self, arr):
        n = len(arr)
        
        
        max_product = arr[0]
        min_product = arr[0]
        result = arr[0]
        
        for i in range(1, n):
            if arr[i] < 0:
                max_product, min_product = min_product, max_product
            
            max_product = max(arr[i], max_product * arr[i])
            min_product = min(arr[i], min_product * arr[i])
            
            result = max(result, max_product)
        
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
