def cyclic_rotation(A, k):
    B = [0] * len(A)
    for i, val in enumerate(A):
        rotate = i + k
        if rotate < len(A) - 1:
            ind = rotate
        else:
            ind = (i + k) % len(A)
        B[ind] = val
    return B


arr = [1, 2, 3, 4]
rot = 4
print("ANSWER", cyclic_rotation(arr, rot))
