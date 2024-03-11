#call by value
#when you pass a varible  to a function, you are essentially handing over the 
#actual value of the variable itself, not the reference to the object pointing to.

string = "Geeks"

def test(string):
    string = "GeeksforGeeks"
    print("Inside Function:", string)

test(string)
print("outside Function:", string)