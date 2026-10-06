homework_time=int(input("enter your homework time in minutes:"))
free_time=int(input("enter your free time in minutes"))
if homework_time > 60:
    print("plan:focus heavily on studies first")
elif homework_time >0 and free_time>30:
    print("plan for the day is finish your homework first andthen enjoy")
else:
    print("plan: relax and work on your hobbies")
if homework_time > 0:
    print("do not forget to do your homework")