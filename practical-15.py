# Remove duplicates from a list ,preserving order 
nums = [int(x) for x in input ("Enter num seprated by spaces:").split()]
unique =[]
for n in nums:
    if n not in unique:
        unique.append(n)
print(unique)