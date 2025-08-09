if __name__=="__main__":
    str1 = input().lower()
    str2 = input().lower()
    flag = 0
    for i in range(len(str1)):
        v1 = ord(str1[i])
        v2 = ord(str2[i])

        if v1 < v2:
            flag = -1
            break
        elif v1 > v2:
            flag = 1
            break
    print(flag)