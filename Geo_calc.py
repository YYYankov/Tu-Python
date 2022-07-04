import math
def calculate_area(name):\

  name = name.lower()
   

  if name == "rectangle":
    l = int(input("Enter rectangle's a: "))
    b = int(input("Enter rectangle's b: "))
    rect_area = l * b
    print(f"The area of rectangle is{rect_area}.")
   
  elif name == "square":
    s = int(input("Enter square's side length: "))
    sqt_area = s * s
    print(f"The area of square is {sqt_area}.")
 
  elif name == "triangle":
    h = int(input("Enter triangle's h length: "))
    b = int(input("Enter triangle's b length: "))
    tri_area = 0.5 * b * h
    print(f"The area of triangle is {tri_area}.")
         
  elif name == 'parallelogram':
    b = int(input("Enter parallelogram's b length: "))
    h = int(input("Enter parallelogram's h length: "))
    sin = int(input("Enter parallelogram's sina value: "))
    para_area = b * h*math.sin(sin)
    print(f"The area of parallelogram is {para_area}.")
     
  elif name == 'rhombus':
    b = int(input("Enter parallelogram's b length: "))
    h = int(input("Enter parallelogram's h length: "))
    para_area = b * h
    print(f"The area of parallelogram is {para_area}.")
  else:
    print("Sorry! This shape is not available")
 
if __name__ == "__main__" :
   
  print("Calculate Shape Area")
  shape_name = input("Enter the name of shape whose area you want to find: ")
  calculate_area(shape_name)
