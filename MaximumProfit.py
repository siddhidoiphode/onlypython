from typing import List
class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
    
            profit = 0
        
            for i in range(1, len(prices)):
        
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
        
            return profit
            
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.maximumProfit(arr)
        print(res)
