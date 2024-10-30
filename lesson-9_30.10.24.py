size = 10
choise_user = input("a, b, c... ")
if choise_user == "a":
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1 or i == j or j > i:
                print("*", end="")
            else:
                print(" ", end="")
        print()