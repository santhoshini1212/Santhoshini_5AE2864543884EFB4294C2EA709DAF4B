year=int(input("enter the year to be checked:"))
if(year%4==0 and year%100!=9 or year%400==0):
  print("the year is a leap year!")
else:
  print("the year isn't a leap year!")