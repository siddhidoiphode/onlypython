class Solution:
    def pushZerosToEnd(self, arr):
        count = 0  # Position to place the next non-zero element
        for i in range(len(arr)):
            if arr[i] != 0:
                # Swap non-zero element with the element at the 'count' index
                arr[i], arr[count] = arr[count], arr[i]
                count += 1

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1



