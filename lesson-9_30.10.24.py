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


# size = 4
# for k in range(size):
#     for i in range(9):
#         if i % 2 == 0:
#             for j in range(size):
#                 print("*", end="")
#         elif i % 2 == 1:
#             for j in range(size):
#                 print("-", end="")
#     print()
#     for i in range(9):
#         if i % 2 == 0:
#             for j in range(size):
#                 print("-", end="")
#         elif i % 2 == 1:
#             for j in range(size):
#                 print("*", end="")
#     print()


# size = 3
# for k in range(size):
#     for i in range(9):
#         if i % 2 == 0:
#             for j in range(size):
#                 print("*", end="")
#         elif i % 2 == 1:
#             for j in range(size):
#                 print("-", end="")
#     print()


# size = 4
# for k in range(size):
#     for i in range(size*2):
#         if i % 2 == 0:
#             for j in range(size):
#                 print("*", end="")
#         elif i % 2 == 1:
#             for j in range(size):
#                 print("-", end="")
#     print()
# for k in range(size):
#     for i in range(size*2):
#         if i % 2 == 0:
#             for j in range(size):
#                 print("-", end="")
#         elif i % 2 == 1:
#             for j in range(size):
#                 print("*", end="")
#     print()


# from random import randint
#
# level = input('Level ')
#
# if level == "1":
#     temp = 0
#     for i in range(5):
#         a = randint(1 , 10)
#         b = randint(1 , 10)
#         print(f"{a} {b}")
#         res = int(input("Result "))
#         if a * b == res:
#             print('ok')
#             temp += 1
#         else:
#             print('no')
#     print(f"Grade {int(round(12 * temp / 5, 0))}")
# elif level == "2":
#     temp = 0
#     for i in range(10):
#         a = randint(1 , 10)
#         b = randint(1 , 10)
#         print(f"{a} {b}")
#         res = int(input("Result "))
#         if a * b == res:
#             print('ok')
#             temp += 1
#         else:
#             print('no')
#     print(f"Grade {int(round(12 * temp / 10, 0))}")
# elif level == "3":
#     temp = 0
#     for i in range(15):
#         a = randint(1 , 10)
#         b = randint(1 , 10)
#         print(f"{a} {b}")
#         res = int(input("Result "))
#         if a * b == res:
#             print('ok')
#             temp += 1
#         else:
#             print('no')
#     print(f"Grade {int(round(12 * temp / 15, 0))}")

