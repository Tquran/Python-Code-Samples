# multiply [5, 2, 7, -1]
def multiply(l):
    bob = 1
    for i in l:
        bob = bob * i
    return bob
dan = [5, 2, 7, -1]
print(multiply(dan))