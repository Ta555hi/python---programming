#get id of list
a = [1, 2, 3, 4, 5]
print(id(a))


from ctypes import c_int, addressof
#a = 44
print(addressof(c_int(a)))