def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
print("Enter 1.Addition, 2.subtraction, 3.multi,4.Div")
try:
    user_input=int(input("Choose the opperation"))
    num_1=float(input("Enter num 1:"))
    num_2=float(input("Enter Num 2:"))
    if user_input==1:
        result=addition(num_1,num_2)
    elif user_input==2:
         result=subtraction(num_1,num_2)
    elif user_input==3:
        result=multiplication(num_1,num_2)
    else:
            result=division(num_1,num_2)
    print("result:",result)
except ValueError:
     print("Enter a number!")

     