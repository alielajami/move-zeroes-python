''' Application for moving zeroes to the end of a list '''

array_size = int(input("Enter the size of the array: "))
integers_array = []

for i in range(array_size):
    integers_array.append(int(input(f"Enter the integer {i+1}: ")))

def move_zeroes(array):
    ''' Function to move zeroes to the end of the list '''
    for j in range(array.count(0)):
        array.remove(0)
        array.append(0)
    return array

print(move_zeroes(integers_array))
