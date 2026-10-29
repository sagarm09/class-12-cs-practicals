#implement stack push and pop
stack =[]
def push(value):
     stack.append(value)

def pop_item():
     if not stack:
         print("stack underflow")
     else:
         print("deleted:", stack.pop())


push(10)
push(20)
print("stack:",stack)
pop_item()
print("stack:",stack)
