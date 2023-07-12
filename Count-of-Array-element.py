def Count_of_number(array):
    size = len(array)
    max = -float('inf')
    count=0
    for i in array:
        if i>max:
            max=i
    for i in array:
        if max==i:
            count+=1
    return size-count





array=list(map(int,input().split()))
print(Count_of_number(array))
