#Write a program to check if a number is a single digit number,
#2-digit number and so on..,up to 5 digits.


num = int(input("enter a number here upyo 5 digits: "))


if num>=0 and num<=9:
    print("it is a single digit number")

elif num>=10 and num <= 99:
   print ("it is a double digit number")

elif num>=100 and num <= 999:
   print ("it is a triple digit number")

elif num>=1000 and num <= 9999:
   print ("it is a four digit number")
else:
   print("it is a five digit number")