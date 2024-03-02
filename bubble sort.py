def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array),i-1):
            if array[i]>array[j+1]:
                temp=array[i]
                array[j]=array[j+1]
                array[j+1]=temp
data=[9,5,7,9,5,7]
bubblesort=(data)
print('assending order',(data))

