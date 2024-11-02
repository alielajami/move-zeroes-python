''' Application for moving zeroes to the end of a list '''

array_size = int(input("Enter the size of the array: ")) # Getting the size of the array
integers_array = [] # Empty list to store the integers

for i in range(array_size): # Getting the integers from the user
    integers_array.append(int(input(f"Enter the integer {i+1}: "))) # Appending the integers

def move_zeroes(array):
    ''' Function to move zeroes to the end of the list '''
    for j in range(array.count(0)): # Counting the number of zeroes in the
        array.remove(0) # Removing the zeroes from the list
        array.append(0) # Appending the zeroes to the end of the list
    return array # Returning the list

print(move_zeroes(integers_array)) # Printing the list after moving the zeroes to the end
