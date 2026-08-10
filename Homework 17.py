try:
    Total_Shopping = float(input("Enter total shopping: "))
    discount = float(input("Enter discount: "))
    Discounted_Shopping = Total_Shopping / discount
except ValueError:
    print("Please enter a number.")
except ZeroDivisionError as ex:
    print("Exception:", ex)
else:
    print("Discounted shopping:", Discounted_Shopping)
