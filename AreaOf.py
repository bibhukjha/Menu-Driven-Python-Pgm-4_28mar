def Area_rectangle(x,y):
    return x*y
def Peri_rectangle(x,y):
    perimeter = 2 * (x + y)
    return perimeter
def Area_Square(x):
    return x*x


if __name__ == "__main__":
    while(True):
        print("Menu\n 1.Area of Rectangle\n 2.Perimeter of Reactangle\n 3.Area of Square")
        x = int(input("Please Enter your Choice Given:\n"))
        if x==1:
            print("You choose to calculate the area of the rectangle\n")
            lenght = int(input("Please Enter the lenght of the rectangle:\n"))
            breadth = int(input("Please Enter the breadth of the rectangle:\n"))
            a = Area_rectangle(lenght,breadth)
            print("The area of rectangle is",a)
            break
        elif x==2:
            print("You choose to calculate the perimeter of reactangle\n")
            lenght = int(input("Please Enter the lenght of the rectangle:\n"))
            breadth = int(input("Please Enter the breadth of the rectangle:\n"))
            b= Peri_rectangle(lenght,breadth)
            print("The perimeter of rectangle is",b)
            break
        elif x==3:
            print("You choose to calculate the area of the Square\n")
            lenght = int(input("Please Enter the lenght of the square:\n"))
            c = Area_Square(lenght)
            print("The area of square is",c)
            break
        else:
            print("Its the wrong input")
            continue