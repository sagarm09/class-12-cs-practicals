#count uppercase and lower case letters
s = input("Enter a string:")
upper = lower = 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Upper case =", upper)
print("lower case =", lower)        