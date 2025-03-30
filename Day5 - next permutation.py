#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        # code here
        l=len(arr)
        pivot = -1
        
        for i in range(l-2,-1,-1) :
            if arr[i] < arr[i+1] :
                pivot = i
                break
            
        if pivot == -1 :
            arr.reverse()
            return
        
        for i in range(l-1 , pivot ,-1):
            if arr[i] > arr[pivot]:
                arr[i] ,arr[pivot] = arr[pivot],arr[i]
                break
        
        left,right = pivot+1 , l-1
        
        while left < right :
            
            arr[left] , arr[right] = arr[right] , arr[left]
            
            left +=1
            right -=1
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ob.nextPermutation(arr)
        for i in range(N):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends
