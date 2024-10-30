# size = 10
# choise_user = input("a, b, c... ")
# if choise_user == "a":
#     for i in range(size):
#         for j in range(size):
#             if i == 0 or i == size - 1 or j == 0 or j == size - 1 or i == j or j > i:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()


size = 4
for k in range(size):
    for i in range(9):
        if i % 2 == 0:
            for j in range(size):
                print("*", end="")
        elif i % 2 == 1:
            for j in range(size):
                print("-", end="")
    print()
for k in range(size):
    for i in range(9):
        if i % 2 == 0:
            for j in range(size):
                print("-", end="")
        elif i % 2 == 1:
            for j in range(size):
                print("*", end="")
    print()