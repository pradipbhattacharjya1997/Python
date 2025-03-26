def add(x,y):
    print(x +y)

add(12,67)
add(12,56)


def rect(length,width):
    print("The area of the rectangle is",length*width)

rect(12,32)


def hello(name):
    print ("hello, my name is",name)

hello("subha")


def hello(*name):
    print ("hello, my name is",name[2])

hello("john","lisa","peter")