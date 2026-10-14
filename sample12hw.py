age= int(input("age:"))
can_swim=input("can you swim? yes/no")=="yes"
if not can_swim:
    pool="shallow pool"
elif age<12:
    pool="middle pool"
else:
    pool="deep end"
print("assigned pool:{pool}")