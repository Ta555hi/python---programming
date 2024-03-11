#loop is is set of pogramming that allows a set of instruction to perform repeatedly
#for loop is when no interaction is known or fixed
#while loop is..


#for loop, go through each element
fruits = ["apple", "banana", "cherry"] #x is associated with each fruits
for x in fruits: # for every value in fruits print x that is the apple,banana, cherry
    print(x)   # for loop doesn't require index, it is already prloaded

for x in "banana": #it will iterate through every character in a string
    print(x)

#break statement, stops the loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        continue
    print(x)

#range, start from 0 and ends at specified number, stops before the specified number
for x in range(6):
    print(x)
# i
for x in range(2,6): #in for loop, using range,will start from 2 and stop at 5
    print(x)

#in for loop, we can increment number
for x in range(2, 30, 3): # will add the 2 and 3 until it adds to 30, eg 2+3=5, 5+3=8...
    print(x)

for x in range(6): # the L ststement....
    print(x)
else:
    print("finally finishes")

#