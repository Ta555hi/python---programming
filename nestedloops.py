#nested loop is a loop inside a loop

adj = ["red", "big", "tasty"] # 3 element in the list
fruits = ["apple", "banana", "cherry"] #3 element in the list
for x in adj:
    for y in fruits:
        print(x, y) # print statement is executed 3*3=9

adj = ["red", "big", "tasty"] # 3 element in the list
fruits = ["apple", "banana", "cherry"] #3 element in the list
for x in adj:
    print('fruits')# only print 3 time, it will only run for above list
    for y in fruits:
        print(x, y) # print statement is executed 3*3=9

#for loop cannot be empty
for x in [0, 1, 2]:
    pass