#Local Variables

# x = 24
# print ("first variable x ", x)
# def hello():
#     x = 25
#     return x
# print(hello())

#global variables

x = 24
print ("first variable x ", x)
def hello():
    global x
    x = 25
    return x
print(hello())
print (x)