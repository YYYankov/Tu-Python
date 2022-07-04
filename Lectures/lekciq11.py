try:
    x=int(input("Enter a number"))
    print(10/x)
except ValueError:
    print ("Not a number")
#except ZeroDivisionError:
#    print("Invalid number")
#except:
#    print("Generic Error")
except ZeroDivisionError:
    pass
print("Done")

while True:
    try:
        x=int(input("Enter a number")) #ValueError
    except ValueError:
        print("Invalid number. Try again")
    else:
        break
print("hi")
