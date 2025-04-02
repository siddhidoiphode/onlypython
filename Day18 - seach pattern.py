# #User function Template for python3
# Search Pattern (KMP-Algorithm)
# Difficulty: HardAccuracy: 45.04%Submissions: 105K+Points: 8
# Given two strings, one is a text string txt and the other is a pattern string pat. The task is to print the indexes of all the occurrences of the pattern string in the text string.


class Solution:
    def search(self, pat, txt):
        # code here
        n,m=len(txt) , len(pat)
        result=[]
     
        for i in range(n-m+1):
            if txt[i:i+m] == pat :
                # print(txt[i:i+m])
                result.append(i)
                
        return result
        # code here

 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()

# } Driver Code Ends
