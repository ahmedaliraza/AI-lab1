def add(x, y):
   return x + y

def subtract(x, y):
   return x - y
def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

enter = input("Enter Operation (1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if enter == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif enter == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif enter == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif enter == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")


