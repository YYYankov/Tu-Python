def square():
    a=int(input("Input value for a: "))
    print(f" Area is {a**2}")

def rectangle():
    a=int(input("Input value for a: "))
    b=int(input("Input value for b: "))
    print(f" Area is {a*b}")

def triangle():
    a=int(input("Input value for a: "))
    b=int(input("Input value for b: "))
    print(f" Area is {(a*b)/2}")

def parallelogram():
    a=int(input("Input value for a: "))
    ha=int(input("Input value for ha: "))
    print(f" Area is {(a*ha)}")
    
def rhomb():
    a=int(input("Input value for a: "))
    ha=int(input("Input value for ha: "))
    print(f" Area is {(a*ha)}")


dictionary={
    1:square,
    2:rectangle,
    3:triangle,
    4:parallelogram,
    5:rhomb,
   
    }

figure= int(input("Pick a figure from the list:\n 1-square\n 2-rectangle\n 3:triangle\n 4:parallelogram\n 5:rhomb \n >"))
dictionary[figure]()
