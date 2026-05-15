# Python Project-1: Build a Simple Calculator

def addition(x,y):
  return x+y

def subtraction(x,y):
  return x-y

def multiplication(x,y):
  return x*y

def division(x,y):
  if y==0 :
    print("Error:Divide by zero not allow")
    return -1
  return x/y


while True :
  t = int(input("Enter 1 for interger and 2 for float input: "))

  if t==1 :
    print("Enter two (integer) numbers to perform operation: ")
    n1 = int(input("Enter first: "))
    n2 = int(input("Enter second: "))
  else :
    print("Enter two (float) numbers to perform operation: ")
    n1 = float(input("Enter first: "))
    n2 = float(input("Enter second: "))

  print("---Choose the Arithmetic operation---")
  print("1. Addition.")
  print("2. Subtraction.")
  print("3. Multiplication.")
  print("4. Division")
  print("5. Exit.")
  choice = int(input("Enter choice: "))

  if choice==1 :
    print(f"The additon of x={n1} and y={n2} is: ",addition(n1,n2))
  elif choice==2 :
    print(f"The Subtraction of x={n1} and y={n2} is: ",subtraction(n1,n2))
  elif choice==3 :
    print(f"The Multiplication of x={n1} and y={n2} is: ",multiplication(n1,n2))
  elif choice==4 :
    print(f"The Division of x={n1} and y={n2} is: ",division(n1,n2))
  elif choice==5 :
    print("Exiting Program...!!!")
    break
  else :
    print("Invalid choice!")
  
