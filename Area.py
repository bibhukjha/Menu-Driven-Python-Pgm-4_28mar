def RectangleArea(x, y):
    return x*y

def RectanglePerimeter(x, y):
    return x+x+y+y

def SquareArea(x):
    return x*x

if __name__=="__main__":
    n1=int(input("Enter value1: "))
    n2=int(input("Enter value2: "))
    print(RectangleArea(n1, n2))
    print(RectanglePerimeter(n1, n2))
    print(SquareArea(n1))

while(True):
    print('''
          1. Area of rectangle
          2. Perimeter of a rectangle
          3. Area of a square
          ''')
    choice = int(input("Select an option: "))

    functions = [RectangleArea, RectanglePerimeter, SquareArea]
    a = functions[choice - 1]()
    ch = input("\n Press enter to continue OR press N to discontinue!")
    if (ch == "n" or ch == "N"):
        break
    else:
        pass