binarysearch(x,array,low,high)
if low>high:
    return false
else:
    mid=(low+high)/2
    if x==array[mid]:
        return mid
    else:
        if x>array[mid]:
            return (array,x,mid+1,high)
        else:
            return(array,x,mid-1,low)
    
