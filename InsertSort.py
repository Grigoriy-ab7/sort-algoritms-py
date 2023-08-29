arr = [3, 1, 4, 8, 7, 10, 9, 5, 6]

def Sort(arr):
    n = len(arr)

    for i in range(1, n):
        temp = arr[i]
        j = i

        while j > 0 and arr[j-1] > temp:
            arr[j] = arr[j-1]
            j-=1
        arr[j] = temp

    return arr

print(arr)
print(Sort(arr))    