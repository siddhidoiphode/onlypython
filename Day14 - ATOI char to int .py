

#User function template for Python

class Solution:
    def myAtoi(self, s):
        # Code here
        s=s.strip()
        i=res=0
        sign=1 
        
        if i<len(s) and (s[i]=='+' or s[i]=='-'):
            if s[i] == '-':
                sign = -1
            i+=1
            
        while i < len(s) and '0'<=s[i]<='9' :
            res=res*10 + (ord(s[i]) - ord('0'))
            i+=1
            
        res*=sign
        
        if res > 2**(31) -1 :
            return 2**(31) -1
        elif res < -2**31 :
            return  -2**31 
        else:
            return res
        
        
    

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends
