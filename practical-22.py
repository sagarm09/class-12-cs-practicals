f = open("notes.txt", "r")
data = f.read()
f.close()
print("lines =", len(data.splitlines()))
print("words =", len(data.split()))
    
