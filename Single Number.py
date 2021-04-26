def singleNumber(A):
    result = A[0]
    ln = len(A)
    for i in range(1,ln):
        result = result ^ A[i]
    return result