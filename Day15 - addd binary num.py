#User function Template for python3
class Solution:
	def addBinary(self, s1, s2):
		# code here
		def trimLeadingZero(s):
		    
		    firstOne = s.find('1')
		    
		    if firstOne!=-1 :
		        return s[firstOne : ]
		    else :
		        return '0'
		        
		        
        s1=trimLeadingZero(s1)
        
        s2=trimLeadingZero(s2)
        
        
        # print("s1s2" , s1,s2)
        
        l1 = len(s1)
        l2 = len(s2)
        
        if l2 >l1:
            
            l1,l2 = l2,l1
            s1,s2 = s2,s1
            
            
        j = l2-1
        res = ''
        carry = 0
        
        for i in range(l1-1 , -1 ,-1) :
            
            bit1=int(s1[i])
            bitsum=bit1 + carry
            
            if j>=0 :
                
                bit2=int(s2[j])
                bitsum += bit2
                j-=1
                
            bit = bitsum % 2
            carry = bitsum //2
            
            res += str(bit)
            # print(res)
             
        if carry>0 :
            res += "1"
                
        return res[::-1]
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends
