x ="Hello World" #string
X = 50   #integer
x = 60.5 #float
x = 3j   #complex
x = ["Geeks", "for", "Geeks"] #list
x = ("Geeks", "for", "Geeks")
x = range(10)
x = {"name": "Suraj", "age": 24}
x = {"Geeks", "for", "Geeks"}
x = frozenset({"Geeks", "for", "Geeks"})   
x = True
x = b"Geeks"
x = bytearray(4)
x = memoryview(bytes(6))
x = None 


my_list = [1, 2, 3, 4, 5]
my_list.insert(1, 5) #list variable and index where we want to add new variable(index and value)
                     # insert 5 at a place(index 1)
print(my_list)    #list and array is same
                  #array is a one data type that can only store one type of data
                  #array are defined as lists in python
my_list.append(5) # in append, the value will alys be added at the end of list, imp in stack,etc
my_list.append(8)
print(my_list)     

print(len(my_list)) #in len function, it doesnt count from array index,it doesnt start frm 0

my_list.remove(2) # it removes the content inside the list
print(my_list) 
my_list.remove(my_list[0]) #this specifically removes the content of the index
print(my_list)

my_list.pop() #
print(my_list)
varpop = my_list.pop()
print(varpop)