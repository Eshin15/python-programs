x = int(input("enter first number"))
ope = input("enter a operator")
y = int(input("enter second number"))


add = x+y
sub = x-y
mul = x*y
div = x/y

if ope == "+" :
    print("addition of two number is",add)
elif ope == "-":
    print("subtraction of two number is",sub)
elif ope == "*":
    print("multiplication of two number is",mul)
else:
    print("division of two number is",div)


