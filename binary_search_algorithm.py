def binary_search(array, x, low, high):
    mid = (low + high)//2

    if mid < high:
        if array[mid] == x:
            print(f"Got the element at position {mid}")
        elif array[mid] > x:
            return binary_search(array, x, low, mid-1)
        elif array[mid] < x:
            return binary_search(array, x, mid+1, high)
    else:
        print('The element you are searching for is not on this list')
        



array = [2,4,6,8,10,12,14,16,18]
x = int(input("Give me the number you are searching for\n"))
binary_search(array,x,0,len(array))
