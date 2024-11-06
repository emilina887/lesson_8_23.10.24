# a = input("Enter: ")
#
# print(a[::-1])

# my_str = "Hello World!"
#
# print(my_str.count(""))


# str = input("Enter: ")
# count_letters, count_number = 0, 0
#
# for i in range(0, len(str)):
#     if str[i].isalpha():
#         count_letters += 1
#     if str[i].isnumeric():
#         count_number += 1
#
# print(f"Letters {count_letters}, Number {count_number}")
# print(len(str))


# str = input("Enter: ")
# count_letters, count_number = 0, 0
#
# for let in str:
#     if let.isalpha():
#         count_letters += 1
#     if let.isnumeric():
#         count_number += 1
#
# print(f"Letters {count_letters}, Number {count_number}")
# print(len(str))


# import time
#
# str = input("Enter: ")
# count_letters, count_number = 0, 0
# start = time.time()
#
# for let in str:
#     if let.isalpha():
#         count_letters += 1
#     if let.isnumeric():
#         count_number += 1
#
# print(f"Time {time.time() - start}")
# print(f"Letters {count_letters}, Number {count_number}")
# print(len(str))


# str = input("Enter: ")
#
# print(str.count('із'))


# str = input("W: ")
# strs = input("S: ")
#
# print(str.count(strs))


# str = input("S ")
# str2 = input("W O ")
# str3 = input("W N ")
#
# result = str.replace(str2, str3)
# print(result)


# a = input("Enter: ")
# b = a[::-1].capitalize()
# if a == b:
#     print("Паліндром")
# else:
#     print("Не є паліндромом")


# a = input("Enter: ")
# b = a[::-1].replace(" ", "").lower()
# if a.replace(" ", "").lower() == b:
#     print("Паліндром")
#     print(b)
# else:
#     print("Не є паліндромом")


url = "https://pythoncod.club/stroki-v-python-i-metody-raboty/"
index_one_sl = url.find("/")
index_two_sl = url.find("/")
print(url.find("/", index_one_sl+1))
temp_url = url[url.find("/", index_one_sl+1)+1:]
print(temp_url[:temp_url.find("/")])