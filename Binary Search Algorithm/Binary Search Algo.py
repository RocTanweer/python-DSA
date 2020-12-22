def Bsa(arr, x):
    """This function is used to find index of an element in a sorted list."""
    if x == arr[0] or x == arr[len(arr)-1]:
        return f"Your number {x} is at index {arr.index(x)}"
    first = 0
    last = len(arr) - 1
    while True:
        mid = (first+last)//2
        if x == arr[mid]:
            break
        elif x > arr[mid] and x <= arr[len(arr)-1]:
            first = mid
            continue
        elif x < arr[mid] and x >= arr[0]:
            last = mid
            continue
        else:
            print("invalid")
            break
    return f"Your number {x} is at index {mid}."









