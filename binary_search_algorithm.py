# def binary_search(array,searching):
#     half_array = len(array)//2
#     first_half = array[:half_array]
#     second_half = array[half_array:]

#     while True:
#         if searching in first_half:
#             print(f"Got it in first half at position {first_half.index(searching)}")
#             break
#         if searching in second_half:
#             print(f"Got it in second half at position {second_half.index(searching)+half_array}")
#             break  
#         else:
#             print("Sorry, the item you are searching is not in this list")
#             break       

# searching = int(input("Give me the number you are searching for\n"))

def binary_search(array, x, low, high):
    if high >= low:

        mid = low + (high - low)//2

        if array[mid] == x:
            print(f"Got the element at position {mid}")
        elif array[mid] > x:
            return binary_search(array, x, low, mid - 1)
        else:
            return binary_search(array, x, mid + 1, high)
    else:
        print('The element you are searching for is not on this list')
        



array = [2,4,6,8,10,12,14,16,18]
x = int(input("Give me the number you are searching for\n"))
binary_search(array,x,0,len(array))
