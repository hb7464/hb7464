def splitarray(arr):

    if arr is None:
        return arr
    
    elif len(arr) <= 1:
        return arr
    
    else:
        mid = len(arr)//2
        arr[:mid] = splitarray(arr[:mid])
        arr[mid:] = splitarray(arr[mid:])
        arr[0:] = mergesort(arr[:mid],arr[mid:])
        print(arr)
        return arr

def mergesort(left,right):
    
    if not right:
        return left
    
    if not left:
        return right
    
    if left[0] <= right[0]:
        return [left[0]] + mergesort(left[1:],right)
    
    else:
        return [right[0]] + mergesort(left,right[1:])
    
def main():
    import time
    begin = time.perf_counter_ns()
    L=[2,6,5,5,1,7,4,3]
    print(f'Original Array {L}')
    splitarray(L)
    end = time.perf_counter_ns()
    Total = end - begin
    print(f"Total Time Taken (in Nanoseconds): {Total}")

if __name__ == '__main__':
    main()