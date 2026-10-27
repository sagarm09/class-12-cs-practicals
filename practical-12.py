# Find largest and smallest in a list 
nums = [int(x) for x in input("Enter num seprated by spaces :").split()]
if nums:
    print("Largest =" ,max(nums))
    print("smallest =",min(nums))