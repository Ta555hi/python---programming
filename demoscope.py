#local variable
def myfunc():  #calling function inside function
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()

#global variable
x = 300
def myfunc():
    print("inside function", x) # statement before variable

myfunc()

print("outside function", x)
print(24, x) #defining integer

def global_func():
    global x
    x= 300
global_func()
print(x)
