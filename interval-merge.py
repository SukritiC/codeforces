if __name__ == "__main__":
    # list_interval = [[1,2], [3,4], [6,7], [8,10], [12,16]]
    list_interval = [[3,5], [7,9]]

    new_interval = [1,10]

    beg = new_interval[0]
    end = new_interval[1]
    beg_list = []
    end_list = []
    for element in list_interval:
        if beg < element[0]:
            list_interval.insert(list_interval.index(element), new_interval)
            break
        elif beg > element[1]:
            beg_list.append(element[0])
            end_list.append(element[1])
        elif element[0] <= beg <= element[1]:
            element[1] = end
            break

    print(list_interval)
    for element in list_interval:
        if len(end_list) > 0 and element[0] <= end_list[-1]:
            if element[1] > end_list[-1]:
                end_list[-1] = element[1]
        else:
            beg_list.append(element[0])
            end_list.append(element[1])

    print(beg_list, end_list)



