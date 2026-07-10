num=int(input("Enter a number:"))
temp=num
digits=0
while temp>0:
    temp//=10
    digits=digits+1
print("The number of digits your number contains is",digits)