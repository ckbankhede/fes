total_stock = int(input("Enter Total stock <=50:"))
packed_box_data = []
box_number = 1
while total_stock > 0:
    items_in_box = 0
    while items_in_box < 10 and total_stock > 0:
        total_stock -= 1         
        items_in_box += 1        
    
    packed_box_data.append(items_in_box)
    box_number += 1
store = {
    "Aisle 1": ["Shelf A", "Shelf B"],
    "Aisle 2": ["Shelf A", "Shelf B", "Shelf C"]
}

print("=== FINALE STOCK REPORT ===")
box_index = 0

for aisle, shelves in store.items():
    for shelf in shelves:
        if box_index < len(packed_box_data):
            items = packed_box_data[box_index]
            print(f"{aisle} -> {shelf}: Box {box_index + 1} ({items} items)")
            box_index += 1
