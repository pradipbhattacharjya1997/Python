"""
1-10
even numbers
2,4,6,8,10

%2 == 0
"""

for i in range(1,11):
    if i % 2 == 0:
        print('even',i)
    else:
        print('odd',i)