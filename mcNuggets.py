def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    aMax = n//6
    bMax = n//9
    cMax = n//20
    for a in range(0,aMax+1):
         for b in range(0,bMax+1):
             for c in range(0,cMax+1):
                 if a * 6 + b * 9 +c * 20 == n:
                     return True
    return False

print(McNuggets(6))

