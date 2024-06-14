userName = input()
even_odd_char = len(userName)
for i in range(even_odd_char):
    print(userName[i], end="")
    if ord(userName[i]) % 2 == 0:
        print("*", end="")
