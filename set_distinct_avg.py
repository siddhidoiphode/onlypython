def average(array):
    # your code goes here

    s=set(array)
    l=len(s)
    
    avg= sum(s)/l
    return avg


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
