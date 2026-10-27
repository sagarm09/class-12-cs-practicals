# Search for an item in a list 
items = input("Enter items seprated by spaces").split()
key = input("Enter item to search :")
if key in items:
    print("Items found at  index ", items.index(key))
else:
    print("Item not found")    