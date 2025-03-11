def hello(name,age=32):
    print("Hello " + name + "you are " + str( age) + " year old")

# hello("krish",35)


def hello(*args,**kwargs):
    print(args)
    print(kwargs)

# hello("krish","Naik", age=32,dob=1989)

lst=list(('krish','Naik'))
dict_val={'age': 32, 'dob':1989}

#hello(*lst,**dict_val)

hello("Krish","Naik","1",2,"1989",age=10,dob=1990)