print("Half mirrored triangle.")
rows=int(input("Enter the no. of rows for the triangle"))
for i in range (1,rows+1):
    print(" "*(rows-i)+"*" *i)