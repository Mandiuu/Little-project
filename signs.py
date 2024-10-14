aries = 0
aquarius = 0
capricorn = 0
scorpio = 0

print ("===================")

print ("⛎  ♐  ♉ ")

print ("Let me guess your zodiac sign")

print ("(This is basically science)")

print ("♈  ♋  ♉ ")

print ("===================")

print ("Q1) Tell me, what does people say when you tell them your sign?")

print (" 1) OMG your sign is the worst")

print (" 2) Oh, I can see it, you are such a hippie")

print (" 3) My ex had the same sign")

print (" 4) I wish I was born the same day as you")


answer = int(input('Enter answer (1-2-3-4): '))

if answer == 1:
  scorpio += 1
elif answer == 2:
  aquarius += 1
elif answer == 3:
  capricorn += 1
elif answer == 4:
  aries += 1

else:
  print("Wrong input.")

print("Q2) If you could eat one thing for the rest of your life, what would it be?:")
print (" 1) Jasmine rice")
print (" 2) Cheeseburgers")
print (" 3) Steam vegetables")
print (" 4) Mayonnaise")

answer = int(input('Enter answer (1-4): '))
  
if answer == 1:
  scorpio += 1
elif answer == 2:
  aquarius += 1
elif answer == 3:
  capricorn += 1
elif answer == 4:
  aries += 1
else:
  print("Wrong input.")   

print("Q3) I you were a day of the week, which one would you be?")
print (" 1) Friday")
print (" 2) Sunday")
print (" 3) Monday")
print (" 4) Tuesday")

answer = int(input('Enter answer (1-4): '))
  
if answer == 1:
  scorpio += 1
elif answer == 2:
  aquarius += 1
elif answer == 3:
  capricorn += 1
elif answer == 4:
  aries += 1
else:
  print("Wrong input.")

if scorpio >= aquarius and scorpio >= capricorn and scorpio >= aries:
  print('You are such an Scorpio')
  print("If this isn't true, then you should be.")
elif aquarius >= capricorn and aquarius >= aries:
  print('You are such an Aries')
  print("If this isn't true, then you should be.")
elif capricorn >= aries:
  print('You are such a Capricorn')
  print("If this isn't true, then you should be.")
else:
  print('You are such an Aquarius')

  print("If this isn't true, then you should be.")
