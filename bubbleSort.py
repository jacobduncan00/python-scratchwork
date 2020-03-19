def bubbleSort(arr):
    length = len(arr)
    result = []
    for i in range(length - 1):
        swapped = False 
        for j in range(length - i - 1):
            if arr[j] > arr[j+1]:
                swapped = True 
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swapped:
            break
    return arr

def main():
    arr = [9, 4, 5, 2, 6, 2, 1]
    print("Original Array:")
    for element in arr:
        print(element)
    bubbleSort(arr)
    print(" ")
    print("Sorted Array:")
    for element in arr:
        print(element)

if __name__ == "__main__":
    main()
