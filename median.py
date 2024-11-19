n=int(input())
arr = list(map(int, input().rstrip().split()))
def median(n,arr):
    l=n
    arr.sort()
    mid=l//2
    if l%2 !=0:
        print(arr[mid])
    else:
        ans=(arr[mid]+ arr[mid-1])/2
        print(ans)
median(n,arr)
