def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """

    i=1
    j=x
    while i<=j:
        m = i+ (j-i)//2
        print(i," ",m," ",j)
        if m*m <= x:
            i = m +1
        else:
            j = m-1
    return j
    