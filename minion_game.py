def minion_game(string):
    s,k=0,0
    v='AEIOU'
    l=len(string)
    for i in range(len(string)):
        if string[i] in v:
            k+= l-i
        else:
            s+=l-i
    if s > k:
        print("Stuart",s)
    elif s < k:
        print("Kevin",k)
    else:
        print("Draw")
            

if __name__ == '__main__':
    s = input()
    minion_game(s)
