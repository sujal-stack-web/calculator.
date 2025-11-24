#a simple calculator by which we can do various operations
x = int(input("enter a number:- "))
y = int(input("enter a number:- "))
print("1 is addition, 2 is substraction,3 is multiplication, 4 is division , 5 is square, 6 is square root")
r = int(input("enter the operator:- "))
if r == 1:
    print("the sum of x and y is",x+y)
elif r == 2:
     print("the substraction of x and y is",x-y)
elif r == 3:
      print("the multiplication of x and y is",x*y)
elif r == 4:
      print("the division of x and y is",x/y)
elif r == 5:
      print("the square of x  is",x**2)
else:
     print("the square root of x  is",x**0.5)
