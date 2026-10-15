print("enter a number u want tu use as a numerator")
num1=int(input())
print("enter a number u want to use as a denominator")
num2=int(input())
if num1%num2==0:
    print("\n"+str(num1)+ " is divisable by " +str(num2))
else:
    print("\n"+str(num1)+ " is not divisable by " +str(num2))