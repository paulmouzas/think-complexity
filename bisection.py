def bisection(l, v):
    """returns the index of the target value (v)
    in the sorted list (l)
    """
    low = 0
    high = len(l)
    
    while high-low != 1:
        mid_index = (low+high)/2
        guess = l[mid_index]
        if guess > v:
            high = mid_index
        elif guess < v:
            low = mid_index
        else:
            return mid_index
    print 'number not in given list'
    return None
l = [1,3,4,5,7,8,9,10]
print bisection(l,9)