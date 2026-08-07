def calculate_change(paid, price):
    change = paid - price
    return change
ticket_cost = 15
print("This is the parking ticket counter.")
print("One parking ticket costs 15 units.")
Total_paid = 0
coins_inserted = 0  
while True:
    coin = int(input("Insert a coin (1, 5, 10, or 15): "))
    if coin != 1 and coin != 5 and coin != 10 and coin != 15:
        print("Invalid coin, try again!\n")
        continue
    Total_paid += coin
    coins_inserted += 1
    print(f"Inserted {coin}. Total so far: {Total_paid}\n")
    if Total_paid >= ticket_cost:
        print("Enough money inserted\n")
        break
change_due = calculate_change(Total_paid, ticket_cost)
print("Dispensing your ticket...")
if change_due == 0:
    pass
else:
    print(f"Here is your change: {change_due} units")
print("Here is your ticket.")
