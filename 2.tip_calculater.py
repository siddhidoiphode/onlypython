# tip_calculater
total=float(input("Enter total amount of bill: "))
no=int(input("Enter number of members: "))
tip=int(input("Enter tip percentage: "))
ans=(total+(total*tip/100))/no
ans=round(ans,2)
print("\nYour tip per person is: ",ans)
