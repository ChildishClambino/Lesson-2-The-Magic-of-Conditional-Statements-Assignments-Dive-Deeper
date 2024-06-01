year = int(input())

if year % 4 == 0:                      #first step ti check if it is a leap year
 if year % 100 == 0:                   #second requirement needed to make sure that it is a leap year
  if year % 400 == 0:                  #third requirement needed to check for leap year
   print("leap year")
  else:
   print("not a leap year")
 else:
  print("leap year")
else:
 print("not a leap year")    