temperature_today=int(input("enter today's temperature in celsius :"))

if temperature_today < 22 : 
   outfit_should_be ="sweater"
   print("it is gonna be cold today")
   print("wear a",outfit_should_be)
else:
   outfit_should_be = "dress"
   print("it is not cold today")
   print("wear a",outfit_should_be)
rainy_day =input("is it raining today ?")
if rainy_day == "yes" :
   print("bring an umbrella with you")
wind_speed=int(input("enter the wind speed today :"))
if wind_speed > 34:
   needs_a_windbreaker="yes"
   print("it is windy today")
   print("you need to wear",outfit_should_be)
else:
   needs_a_windbreaker="no"
   print("it is not windy today")
   print("you do not need a windbreaker",outfit_should_be)
are_there_puddles =input("are there any puddles on the ground?")
if are_there_puddles =="yes":
   shoes="boots"
   print("there are puddles outside")
   print("you need to wear",shoes)
else:
   shoes= "sneakers"
   print("the ground outside is dry")
   print("wear",shoes)
print("")
print("weather check complete")
print("=== weather outfit picker===")
print("temperature:",temperature_today)
print("outfit chosen:",outfit_should_be)
print("raining:",rainy_day)
print("windbreaker needed ?:",needs_a_windbreaker)
print("shoes that were chosen:",shoes)