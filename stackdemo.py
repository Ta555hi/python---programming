stack = [] #STACK is just a list, last element is removed, add elemnt is added, last in first out

stack.append("a")
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

stack.pop() #pops out last elemnt
print(stack)