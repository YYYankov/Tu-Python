#1.1
# y=int(input("Input a year "))
# m=int(input("Input a month [1-12]: "))
# d=int(input("Input a day [1-31]: "))

# print("The next date is [yyyy-mm-dd] ",y,"-",m, "-", d+1 )

# # 1.2
# import datetime
 
# from datetime import timedelta 
 
# d=int(input("ENTER THE DAY : "))
 
# m=int(input("ENTER THE MONTH : "))
 
# y=int(input("ENTER THE YEAR : "))
     

# # format given date
# gDate = datetime.datetime(y, m, d) 
# print("Given date is: ", gDate) 
   
# # Yesterday date 
# yesterday = gDate + timedelta(days = 1) 
# print("Next date will be : ", yesterday) 

#1.3
year = int(input("Input a year: "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))

2.1
class Travel:
    def __init__(self, id, dest: str, flight, price: float):
        self.id = id
        self.dest = dest
        self.flight = flight
        self.price = price

    def reduce(self):
        if self.price>200:
            self.price = round(self.price - self.price * 10 / 100, 2)

    def print(self):
        # print("ID: {} \n Destination: {} \n Flight: {} \n Price: {} \n", self.id, self.dest,self.flight, self.price)
        print(str.format(" ID {} \n Destination: {}\n Flight: {}\n Price: {} \n", self.id, self.dest, self.flight, self.price))

tr_list = [Travel("12B31", "Hamburg", "2:33", 176), Travel("41C7V", "Milan", "1:47", 88), Travel("77ZS2D", "New York", "4:18", 215)]

for tr in tr_list:
    tr.reduce()
for tr in tr_list:
    tr.print()
