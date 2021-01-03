#bubble sort
#O(n^2) complexity

array = [10,5,9,8,7,1,2,25,101]
for i in range(len(array)):
    for j in range(i+1, len(array)):
        if array[j] < array[i]:
            x = array[i]
            array[i] = array[j]
            array[j] = x
                
print(array)
