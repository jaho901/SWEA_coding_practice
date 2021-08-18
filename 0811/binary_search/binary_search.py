def binarySearch(data, key):
    start = 0
    end = len(data)-1
    while start <= end:
        middle = (start + end) // 2
        if data[middle] == key:
            return True
        elif data[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False

data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
print(binarySearch(data, 5))