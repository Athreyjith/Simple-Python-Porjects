# python calculator


operator = input(" enter a operator (- , + , / , *) ")
a = float(input(" enter the first value "))
b = float(input(" enter the second value "))

if operator == '+':
    result = a + b
   
elif operator == '*':
    result = a * b
    
elif operator == '/':
    result = a/b


elif operator == '-':
    result = a-b

else :
    print("wrong input")

print( round(result,3))