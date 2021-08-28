# Tamer Quran
# 8/24/2021
# This program tells the player if they are able to do a task with the items they have and if the debuff they have will
# prevent them from doing the task
items = ['pan', 'paper', 'idea', 'rope', 'groceries']
debuffs = ['slow']


def task(items, debuffs):
    # All of the items and debuffs were included in one if statement due to an error that wouldn't give an answer
    if 'coat' in items and 'first aid kit' in items and 'rope' in items and 'slow' not in debuffs:
        print("You can climb this mountain")
    # The else statement is used here to tell the player if they cannot do a task.
    else:
        print('You cannot climb this mountain')
    if 'pan' in items and 'groceries' in items and 'small' not in debuffs:
        print("You can cook a meal")
    else:
        print('You cannot cook a meal')
    if 'pen' in items and 'paper' in items and 'idea' in items and 'confusion' not in debuffs:
        print("You can write a book")
    else:
        print('You cannot write a book')


task(items, debuffs)
