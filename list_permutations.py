def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    if len(L1) != len(L2):
        return False
    max = None
    element = None
    typ = None
    if len(L1) == 0:
        return element, max, typ
    tempL2 = L2[:]
    for e in L1:
        if e in tempL2:
            tempL2.remove(e)
    if len(tempL2) != 0:
        return False
    max = 0
    for e in L1:
        count = 0
        for j in L2:
            if e==j:
                count+=1
        if count > max:
            max=count
            element = e
            typ = type(e)
    return element, max, typ


# print(is_list_permutation([1],[1,2]))
# print(is_list_permutation([],[]))
print(is_list_permutation([1,1,2],[2,1,1]))
