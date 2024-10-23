# x = int(input("X "))
# y = int(input("Y "))
#
# res = 1
# for i in range(y):
#     res *= x
# print(res)

# count = 0
# for i in range(100, 120):
#     a = i // 100
#     b = i // 10 % 10
#     c = i % 10
#     if a == b:
#         print(i)
#         count += 1
#     elif b == c:
#         print(i)
#         count += 1
#     elif a == c:
#         print(i)
#         count += 1
#
# print(count)


# count = 0
# for i in range(100, 1000):
#     a = i // 100
#     b = i // 10 % 10
#     c = i % 10
#     if a == b:
#         print(i)
#         count += 1
#     elif b == c:
#         print(i)
#         count += 1
#     elif a == c:
#         print(i)
#         count += 1
#
# print(count)


# count = 0
# for i in range(100, 10000):
#     if i < 1000:
#         a = i // 100
#         b = i // 10 % 10
#         c = i % 10
#         if a != b and a != c and b != c:
#             count += 1
#     else:
#         a = i // 1000
#         b = i // 100 % 10
#         c = i // 10 % 10
#         d = i % 10
#         if a != b and a != c and a != d and b != c and b != d and c != d:
#             count += 1
# print(count)


# num = int(input("Number: "))
#
# new = ""
# while num > 0:
#     temp = num % 10
#     num = num // 10
#     if temp == 3 or temp == 6:
#         continue
#     else:
#         new
# print(new)

# new = ""
# for i in str(num):
#     if i == "3" or i == "6":
#         continue
#     else:
#         new += i
# print(new)


# num = int(input("Number "))
# for i in range(num):
#     for j in range(0, i + 1):
#         print("*", end=" ")
#     print()


# num = int(input("Number "))
# for i in range(num):
#     for j in range(0, num - 1):
#         print("*", end=" ")
#     print()


# num = int(input("Number "))
# for i in range(num):
#     for j in range(0, i + 1):
#         if i == 0 or j == 0 or i == j or num == i or num == j or i == num -1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


num = int(input("Number "))
for i in range(num + 1):
    for j in range(num):
        if i == 0 or j == 0 or i == j or num == i or num == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

    # num1 = int(input("Number1 "))   #прямокутник незаповнений
    # for i in range(num + 1):
    #     for j in range(num1):
    #         if i == 0 or i == num or j == 0 or j == num1-1:
    #             print("*", end=" ")
    #         else:
    #             print(" ", end=" ")
    #     print()