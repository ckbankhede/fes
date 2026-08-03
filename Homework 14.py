def greeting_the_customer():
    print("Welcome to the art supply shop.")
greeting_the_customer()
price_per_paint_cup=float(input("Enter the price per  paint cup:"))
paint_cup_sold=int(input("Enter the amount of cups sold:"))
def calculate_total(price,cups):
    total=price*cups
    return total
total_cost=calculate_total(price_per_paint_cup,paint_cup_sold)
rounded_total=round(total_cost,2)
print("Total cost:",rounded_total)
amount_paid=float(input("Enter the amount paid by the customer:"))
def calculate_change(paid,total):
    change=paid-total
    return change
change_due=calculate_change(amount_paid,rounded_total)
rounded_change=round(change_due,2)
def thank_you_message(cups):
    if cups>=5:
        return "Wow,big order! Thanks so much for your support!"
    else:
        return "Thanks for stopping by the shop!"
closing_message=thank_you_message(paint_cup_sold)
print("")
print("=====Lemonade Stand Receipt=====")
print("Price Per Cup:",price_per_paint_cup)
print("Cups Sold:",paint_cup_sold)
print("Total Cost",rounded_total)
print("Amount Paid",amount_paid)
print("Change Due:",rounded_change)
print(closing_message)
