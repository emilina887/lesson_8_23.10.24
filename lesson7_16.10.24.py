# s = "Hello"
# for symbol in s:
#     print(symbol)

# r = range(1, 5).__iter__() # 1 2 3 4
# print(r.__next__())
# print(r.__next__())
# print(r.__next__())
# print(r.__next__())

# for i in range(1, 5): # 1 2 3 4
#     print(i)

# num = int(input("N "))
# i = 0
# while i <= 10:
#     print(f'{i} * {num} = {i * num}')
#     i += 1

# num = int(input("N "))
# for i in range(1, 11):
#     print(f'{num} * {i} = {i * num}')

#range(start, stop, step)

# num = int(input("N "))
#
# for i in range(5 , 11): #5 6 7 8 9 10
#     print(f'{num} * {i} = {i * num}')

# num = int(input("N "))
#
# for i in range(1 , 11, 2): #1 3 5 7 9
#     print(f'{num} * {i} = {i * num}')

# num = int(input("N "))
#
# for i in range(11 , -1, -1):
#     print(f'{num} * {i} = {i * num}')

# num = int(input("N "))
#
# for i in range(10 , -5, -3):
#     print(f'{num} * {i} = {i * num}')


# for i in range(1, 11):   #вся табличка умножения
#     for j in range(1, 11):
#         print(f'{i} * {j} = {j * i}')
#     print()

# a = int(input("A "))
# b = int(input("B "))
#
# while True:
#     x = int(input("X "))
#     if x > a and x < b:
#         break
# for i in range(a, b+1):
#     if i != x:
#         print(i, end=" ")
#     else:
#         print(f"!{i}!", end=" ")
# s = ""
# for i in range(a, b+1):
#     if i != x:
#         s += str(i) + " "
#     else:
#         s += "!" + str(i) + "! "
# print(s)

# num = int(input("N "))     #квадрат заповнений
#
# for i in range(num):
#     for j in range(num):
#         print("*", end=" ")
#     print()

# num = int(input("N "))
# num1 = int(input("N1 "))
#
# for i in range(num):
#     for j in range(num1):
#         print("*", end=" ")
#     print()

# num = int(input("Number "))     #квадрат незаповнений

# for i in range(num + 1):
#     for j in range(num):
#         if i == 0 or i == num or j == 0 or j == num-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# num1 = int(input("Number1 "))   #прямокутник незаповнений
# for i in range(num + 1):
#     for j in range(num1):
#         if i == 0 or i == num or j == 0 or j == num1-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# a = 1
# b = 100
#
# for i in range(a, b+1):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=" ")