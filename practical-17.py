#search a name in a dictionary
marks ={"Asha":88,"Ravi":23 ,"menna":67}
name = input("Enter name to search:")
if name in marks:
    print("Marks =",marks[name])
else:
    print("name not found")    