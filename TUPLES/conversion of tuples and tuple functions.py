a = ("Oneplus","Nokia","Redmi")
print("Befor conversion",type(a))

a = list(a)
print(a)
print(type(a))
a.append("Vivo")
print(a)

print("the index of redmi is", a.index("Redmi"))