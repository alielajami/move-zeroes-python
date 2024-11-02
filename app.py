''' Application for moving zeroes to the end of a list '''

array_size = int(input("Enter the size of the array: "))
integers_array = []

for i in range(array_size):
    integers_array.append(int(input(f"Enter the integer {i+1}: ")))

def move_zeroes(array):
    ''' Function to move zeroes to the end of the list without using .count and .remove '''
    non_zero_index = 0

    for j in range(len(array)):
        if array[j] != 0:
            array[non_zero_index] = array[j]
            non_zero_index += 1

    for k in range(non_zero_index, len(array)):
        array[k] = 0
    
    return array

print(move_zeroes(integers_array))
