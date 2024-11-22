#ROTATE ARRAY


class Solution:
    def reverse(self,arr,start,end):
        left=start
        right=end
        while left<right:
            arr[left],arr[right] = arr[right],arr[left]
            left+=1
            right-=1

    def rotateArr(self, arr, d):
        #Your code here
        n=len(arr)
        d=d%n
        self.reverse(arr,0,d-1)
        self.reverse(arr,d,n-1)
        self.reverse(arr,0,n-1)
        

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


