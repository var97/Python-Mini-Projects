import random
chars = 'abcdefghijklmnopqrstuvwxyz0123456789?@#$%^&*()!~}{|\][;.,></?'
noofpass = int(input('Enter no of passwords you want:'))
length = int(input('Enter the length of password:'))
for p in range(noofpass):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
