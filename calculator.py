import math
print("Select an operation")
print("1.addition")
print("2.subtract")
print("3.divide")
print("4.multiply")
print("5.square root")
print("6.square")
print("7.sin")
print("8.cos")
print("9.tan")
print("10.log")

operation = int(input())

if operation == 1:
	num1 = int(input("enter the first number ="))
	num2 = int(input("enter the second number ="))
	print(num1+num2)
elif operation == 2:
	num1 = int(input("enter the first number ="))
	num2 = int(input("enter the second number ="))
	print(num1-num2)
elif operation == 3:
	num1 = int(input("enter the first number ="))
	num2 = int(input("enter the second number ="))
	print(num1/num2)
elif operation == 4:
	num1 = int(input("enter the first number ="))
	num2 = int(input("enter the second number ="))
	print(num1*num2)
elif operation == 5:
	num1 = int(input("enter the  number ="))
	print(math.sqrt(num1))
elif operation == 6:
	num1 = int(input("enter the number ="))
	print(num1**2)
elif operation == 7:
	num1 = int(input("enter the number ="))
	print(math.sin(num1))
elif operation == 8:
	num1 = int(input("enter the number ="))
	print(math.cos(num1))
elif operation == 9:
	num1 = int(input("enter the number ="))
	print(math.tan(num1))
elif operation == 10:
	num1 = int(input("enter the number ="))
	num2 = int(input("enter the number for base ="))
	print(math.log(num1, num2))
else:
	print("invalid operation")
