n,j,z=5,1,0
for i in range(2*n -1):
    if i==0 :
        print(" "*(n-i-1) + "*" )
    elif i==(2*n -2):
        print(" "*j +"*"+ " "*(n+z) )
    elif i<n :
        print(" "*(n-i-1) + "*" + " "*(2*i - 1)+"*") 
    else:
        print(" "*j +"*"+ " "*(n+z)   +"*")
        j +=1
        z -=2
