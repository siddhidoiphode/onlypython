#Program to print addtion of digits:
add_of_digits.py
num=int(input("Enter number: "))
ans=0
for i in str(num):
  ans=int(i)+ans
print(ans)
