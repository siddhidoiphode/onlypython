def merge_the_tools(string, k):
    # your code goes here
    l=len(string)
    # print(l)
    # div=l/k
    c=0
    li=[]
    ele=''
    for i in range(l):
        if c<k :
            ele = ele+string[i]
            c+=1
            # print("i if",i)
            # print(ele)

        else:
            li.append(ele)
            ele=''
            ele = ele+string[i]
            # print(ele)
            c=1
            # print("i else",i)
        
        if i==(l-1):
            # print("elif",i)
            li.append(ele)    


    for i in range(len(li)):        
        t=''
        for j in li[i]:
            if j not in t:
                t=t+j
        print(t)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


"""
STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
Sample Output

AB
CA
AD

"""



# str='hello bitches'
# str=str.upper()
# print(str)
