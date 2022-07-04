#2
#def divide(x, y):
#    return x/y

#def add(x, y):
#    return x + y

#def subtract(x, y):
#    return x - y

#def multiply(x, y):
#    return x * y

#print("select operation: \n 1.add \n 2.subtract \n 3.multiply \n 4.divide \n 5.quit")

#while True:
#    choice=input("enter your choice with number: ")

#    if choice in ('1','2','3','4'):
#        x=int(input("enter first number: "))
#        y=int(input("enter second number: "))

#        if choice=='1':
#         print(x, "+", y, "=", add(x, y))

#        elif choice == '2':
#            print(x, "-", y, "=", subtract(x, y))

#        elif choice == '3':
#            print(x, "*", y, "=", multiply(x, y))

#        elif choice == '4':
#            print(x, "/", y, "=", divide(x, y))
#    elif choice== '5':
#        break



#3
#def check(txt):
#    rev=txt[::-1]
#    status=1
#    if(txt!=rev):
#        status=0
#    return status
#txt=input("Enter the string: ")
#print(check(txt))

#4
def change_vales(array, number):
    for i in range(len(array)):
        if array[i] > number:
            array[i] = 0
            
    return array

number=int(input("Number>> "))
print(change_vales([1, 2, 3, 4, 5, 6], number))
