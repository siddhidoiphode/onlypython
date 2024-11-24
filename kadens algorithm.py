
class Solution:

    def maxSubArraySum(self, arr):
        # Initialize current sum and maximum sum
        current_sum = 0
        max_sum = float('-inf')
        
        # Traverse through the array
        for num in arr:
            current_sum += num
            # Update maximum sum if current sum is greater
            if current_sum > max_sum:
                max_sum = current_sum
            # Reset current sum to 0 if it becomes negative
            if current_sum < 0:
                current_sum = 0
        
        return max_sum



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
