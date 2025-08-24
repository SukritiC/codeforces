if __name__ =="__main__":
    str_value = input()
    val = ord(str_value[0])

    if val >= 97 and val <= 122:
        val -= 32

    new_str = chr(val)+str_value[1:]

    print(new_str)