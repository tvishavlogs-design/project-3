field1=200
field2=370
field3=70
field4=98
field5=130
total= field1+field2+field3+field4+field5
average=total/5
print("total harvest :",total,"kg")
print("average per field :"average,"kg")

price_per_kg=70
earnings= total*price_per_kg
print("total earnings :pounds",earnings)
bags = total//70
leftover=total % 70
print("full bags packed :",bags)
print("leftover grain :" leftover,"kg")
last_year=500
print ("better than last year? :",total> last_year)
print("same as last year ?     :", total == last_year)
print("at least good ?         :",total>= last_year)
total +=  40
print("after bonus crop :",total,"kg")
total-= 12
print("after seed reserve :", total ,"kg")
bags= total//70
print("final bags packed :", bags)