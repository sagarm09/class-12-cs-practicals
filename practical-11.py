# Sum and average of list elements
nums = [int(x) for x in input("Enter numbers seprated by spaces : ").split()]
if nums:
    print("Sum =", sum(nums))
    print("Average =", sum(nums)/ len(nums))
else:
    print("List is empty")
