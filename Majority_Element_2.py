class Solution:
    def findMajority(self, arr):   
        l=len(arr)
        n=l//3
        result=[]
        for i in set(arr):
            if arr.count(i) > n:
                result.append(i)

        return sorted(result)

def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()
