# lab 1.2 => Binary search

def binary_search(data, target, low, high):
    """
        ...
    """
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            # ...
            return binary_search(data, target, low, mid - 1)
        else:
            # ...
            return binary_search(data, target, mid + 1, high)

data = [1, 3, 5, 7, 9, 11, 13, 15, 17]
print(binary_search(data, 7, 0, len(data)-1))
print(binary_search(data, 10, 0, len(data)-1))
print(binary_search(data, 7, 0, len(data)-1))
print(binary_search(data, 9, 0, len(data)-1))
print(binary_search(data, 20, 0, len(data)-1))
print(binary_search(data, 13, 0, len(data)-1))