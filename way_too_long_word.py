


if __name__ == "__main__":
    ctr = int(input())
    lst = []
    for i in range(ctr):
        word = input()
        lst.append(word)

    for element in lst:
        n = len(element)
        if n > 10:
            print(element[0] + str(n - 2) + element[n - 1])
        else:
            print(element)

