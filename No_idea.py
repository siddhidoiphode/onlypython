# Enter your code here. Read input from STDIN. Print output to STDOUT

n,m = map(int,input().split())

arr=list(map(int,input().split()))

a=set(map(int,input().split()))

b=set(map(int,input().split()))


score =0
for i in arr:
    if i in a:
        score+=1
    elif i in b:
        score-=1
    
    

    
print(score)
