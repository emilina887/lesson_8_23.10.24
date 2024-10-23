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


count = 0
for i in range(100, 10000):
    if i < 1000:
        a = i // 100
        b = i // 10 % 10
        c = i % 10
        if a != b and a != c and b != c:
            count += 1
    else:
        a = i // 1000
        b = i // 100 % 10
        c = i // 10 % 10
        d = i % 10
        if a != b and a != c and a != c and b != c and b != d and c != d:
            count += 1
# print(count)
