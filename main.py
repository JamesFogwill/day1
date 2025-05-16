import numpy as np

with open("input.txt", "r") as file:

    # print(input.read())

    lines = file.readlines() # read lines into lines array

    #print(lines)

    array_1 = []
    array_2 = []

    for line in lines:

        firstNumber = line[0:5]
        secondNumber = line[8:14]
        
        array_1.append(firstNumber)
        array_2.append(secondNumber)

    # arrange array 1 and array 2 in asceding order

    # np.arr(array_1)
    sortedArray_1 = np.sort(array_1)
    sortedArray_2 = np.sort(array_2)

    #compare each line of array 1 with array 2

    distances = []

    for index, item in enumerate(sortedArray_1):
        distances.append(abs(int(item) - int(sortedArray_2[index])))

    #print(distances)

    total_distance = 0
    for number in distances:
        total_distance += number

    print(total_distance)

    