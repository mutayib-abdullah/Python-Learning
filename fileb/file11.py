# temp = float(input('enter the temperature: '))
# if (temp == 25):
#  print('normal')
# elif temp > 25:
#     print('hot')
# else:
#     print('cold')
 

# amount = int(input('enter the amount: '))

# if amount<1000:
#     total = amount - amount*0.1
# elif amount>=1000 and amount<5000:
#  total = amount - amount*0.15
# elif amount>=5000 and amount<10000:
#    total = amount - amount*0.20
# else:
#    total = amount - amount*0.25

# print('pay', total)

 
# dayNo = int(input('Enter dayNo: '))

# if dayNo==0:
#     print('Monday')
# elif dayNo==1:
#  print('Tuesday')
# elif dayNo==2:
#  print('Wednesday')
# elif dayNo==3:
#  print('Thurusday')
# elif dayNo==4:
#  print('Friday')
# elif dayNo==5:
#  print('Saturday')
# elif dayNo==6:
#  print('Sunday')
# else:
#   print('invalid dayNO')

year = int(input('enter the year: '))

if year%400==0:
 print('leapYear')
elif year%100==0:
      print('Not a leapYear')
elif year%4==0:
    print('LeapYear')
      
else:
     print('Not a leapYear')
