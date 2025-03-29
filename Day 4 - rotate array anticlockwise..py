#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
   
    def Reverse(self,arr,start,end):
        while start< end :
            arr[start],arr[end] = arr[end] ,arr[start]
            start+=1
            end-=1
            
    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        d%=n
        
        self.Reverse(arr,0,d-1)
        self.Reverse(arr,d,n-1)
        self.Reverse(arr,0,n-1)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ob.rotateArr(A, D)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
