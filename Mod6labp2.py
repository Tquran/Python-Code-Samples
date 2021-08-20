# Function that checks if a number is in range (1,10)
num = int(input('What number would you like to check?'))
def module6(num):
    if num in range(1,10):
        print(str(num) + ' is in range')
    else:
        print(str(num) + ' is not in range')
module6(num)