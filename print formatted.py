def print_formatted(number):
    # your code goes here
    width = len(bin(number)) -2
    w=width
    i=0
    count=0
    while count<number :
        count +=1
        i+=1
        
        # if i<=number:
        d=str(i)
        o=oct(i)[2:]
        h=hex(i)[2:].upper()
        b=bin(i)[2:]
        print(d.rjust(w), o.rjust(w) , h.rjust(w) , b.rjust(w))
        
         
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
