def findMinXor(A):
    A = sorted(A)
    ln = len(A)
    xr = A[0]^A[1]
    for i in range(1,ln):
        xr = min(xr,A[i]^A[i-1])
    return xr