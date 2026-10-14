print("please enter your marks:")
mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())
marks=mark1,mark2,mark3,mark4,mark5
total= sum(marks)
avg=int(total/5)
validrange=range(0,101)
if avg not in validrange:
    print("invalid input!")
    
elif avg in range(91, 101):
    print("Your Grade is A1")

elif avg in range(81, 91):
    print("Your Grade is A2")

elif avg in range(71, 81):
    print("Your Grade is B1")

elif avg in range(61, 71):
    print("Your Grade is B2")

elif avg in range(51, 61):
    print("Your Grade is C1")

elif avg in range(41, 51):
    print("Your Grade is C2")

elif avg in range(33, 41):
    print("Your Grade is D")

elif avg in range(21, 33):
    print("Your Grade is E1")

elif avg in range(0, 21):
    print("Your Grade is E2")