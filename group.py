import json
import os
from collections import defaultdict

# Sample data from your database
items = [
    {"sn": 20, "propertyid": 103, "docid": 37, "restaurantname": "ROOM SERVICE", "restcode": "RS103", "kitchen": "NONV103", "printerpath": "\\\\satyamavasthiz\\HPReceipt", "itemsn": 1, "itemname": "BURNT GARLIC CHICKEN", "itemprice": 395.00, "quantity": 1, "created_at": "2024-09-09 17:54:43"},
    {"sn": 21, "propertyid": 103, "docid": 37, "restaurantname": "ROOM SERVICE", "restcode": "RS103", "kitchen": "VEG103", "printerpath": "\\\\CosmicPulse\\HPReceipt", "itemsn": 2, "itemname": "BUTTER NAAN", "itemprice": 110.00, "quantity": 1, "created_at": "2024-09-09 17:54:43"},
    {"sn": 22, "propertyid": 103, "docid": 38, "restaurantname": "ROOM SERVICE", "restcode": "RS103", "kitchen": "VEG103", "printerpath": "\\\\CosmicPulse\\HPReceipt", "itemsn": 3, "itemname": "PANEER TIKKA", "itemprice": 200.00, "quantity": 2, "created_at": "2024-09-09 17:55:43"},
    {"sn": 23, "propertyid": 103, "docid": 39, "restaurantname": "ROOM SERVICE", "restcode": "RS103", "kitchen": "NONV103", "printerpath": "\\\\satyamavasthiz\\HPReceipt", "itemsn": 4, "itemname": "CHICKEN BIRYANI", "itemprice": 450.00, "quantity": 1, "created_at": "2024-09-09 18:00:43"},
    {"sn": 24, "propertyid": 103, "docid": 39, "restaurantname": "ROOM SERVICE", "restcode": "RS103", "kitchen": "VEG103", "printerpath": "\\\\CosmicPulse\\HPReceipt", "itemsn": 5, "itemname": "VEG FRIED RICE", "itemprice": 150.00, "quantity": 1, "created_at": "2024-09-09 18:10:43"},
]

# Create a defaultdict to group items by kitchen
grouped_items = defaultdict(list)

# Loop through the items and group them by kitchen
for item in items:
    kitchen = item['kitchen']
    grouped_items[kitchen].append(item)

# Save each group to a separate .txt file and send to printer
for kitchen, kitchen_items in grouped_items.items():
    filename = f"{kitchen}_items.txt"
    
    # Write the grouped items to the text file
    with open(filename, 'w') as f:
        for item in kitchen_items:
            f.write(f"Item Name: {item['itemname']}, Price: {item['itemprice']}, Quantity: {item['quantity']}\n")
    
    # Send the file to the corresponding printer path
    printer_path = kitchen_items[0]['printerpath']
    
    try:
        os.system(f'copy {filename} {printer_path}')
        print(f"Sent {filename} to printer: {printer_path}")
        os.remove(filename)
    except Exception as e:
        print(f"Failed to send {filename} to printer: {printer_path}, Error: {e}")
