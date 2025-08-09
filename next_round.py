
if __name__ == '__main__':
    nk = list(map(int, input().split()))
    n = nk[0]
    k = nk[1]

    nums = list(map(int, input().split()))


    target = nums[k-1]
    count = 0
    # print("target",target)
    for num in nums:
        if num >0 and num >= target:
            # print(num,"----------")
            count += 1

    print(count)
