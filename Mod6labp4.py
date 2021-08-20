# Tamer Quran
# 8/12/2021
# [1, 3, 3, 3, 6, 2, 3, 5]
def new(n):
    jim = []
    for i in n:
        if i not in jim:
            jim.append(i)
    return jim
kate = [1, 3, 3, 3, 6, 2, 3, 5]
print(new(kate))