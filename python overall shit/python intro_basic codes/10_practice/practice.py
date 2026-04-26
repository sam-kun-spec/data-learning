def swap(arr):
    mi = arr.index(min(arr))
    mk = arr.index(max(arr))
    arr[mk],arr[mi] = arr[mi],arr[mk]

    print(arr)
    
arr = [2,6,9,3,5]
swap(arr)
