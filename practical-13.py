#Count Even and odd values in a list 
nums = [int(x) for x in input("Enter numbers seprated by spaces :").split()]
even = odd = 0 
for n in nums:
    if n % 2 == 0:
        even =+ 1
    else:
        odd += 1
print("Even =",even, "Odd = ",odd)                 