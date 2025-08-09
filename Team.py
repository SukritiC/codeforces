
if __name__ == "__main__":
    n = int(input())

    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    count = 0
    for i in range(n):
        if sum(matrix[i]) >= 2:
            count += 1
    print(count)