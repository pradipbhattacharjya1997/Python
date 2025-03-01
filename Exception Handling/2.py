#chek password strength
def check_password(password):
    if len(password) <8:
        raise Exception("Error: Password must be >=8 characters")
    print('password is string')
    
try:
    password = input('enter a password = ')
    check_password(password)
except Exception as e:
    print(e)