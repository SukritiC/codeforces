
def can_divided(w):
    return w > 2 and w % 2 == 0



if __name__ == "__main__":
    w = int(input("Enter the weight of the watermelon "))
    if can_divided(w):
        print("YES")
    else:
        print("NO")