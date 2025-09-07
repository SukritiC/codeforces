if __name__ == "__main__":

    # taking input string from the end user
    expression = input()

    #checking if the input is of length 1
    if len(expression) == 1:
        print(expression)
    else:
        # converting each character in string to individual list element
        exp_list = list(expression)
        nums = []
        #iterating on the list to sort the numbers and skip the operators
        for element in exp_list:
            if element != '+':
                nums.append(int(element))

        #sorting the numbers
        nums.sort()

        #rejoining the elements back into expression
        sorted_expression = '+'.join(map(str,nums))
        print(sorted_expression)
