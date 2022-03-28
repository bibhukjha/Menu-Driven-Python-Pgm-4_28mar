def Area_rectangle():
    length = int(input("Please enter the length: "))
    breadth = int(input("Please enter the breadth: "))
    return length*breadth
def Peri_rectangle():
    length = int(input("Please enter the length of the rectangle:\n"))
    breadth = int(input("Please enter the breadth of the rectangle:\n"))
    perimeter = 2*(length+breadth)
    return perimeter
def Area_Square():
    length = int(input("Please enter the length of the square:\n"))
    return length*length

print("Menu\n 1.Area of rectangle\n 2.Perimeter of reactangle\n 3.Area of square")
x = int(input("Please enter your choice given:\n"))
if x == 1:
    a = Area_rectangle()
    print("The area of rectangle is: ", a)
elif x == 2:
    b = Peri_rectangle()
    print("The perimeter of rectangle is: ", b)
elif x == 3:
    c = Area_Square()
    print("area of square is: ", c)
else:
    print("wrong input")