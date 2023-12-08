def prime_checker(num):
  flag=0
  if  num<=0:
    print("Enter natural numbers.")
  else:
    if num==1:
      print("Neither prime nor composite.")
    else:
     for i in range(2,num):
       if num%i==0:
         print("Not a prime number  ")
         flag=1
         break
     if flag==0:
         print("Prime number")
       
num=int(input("Enter any number : "))
prime_checker(num)
