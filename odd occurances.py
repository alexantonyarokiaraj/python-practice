def odd_occurances(A):
    B = set(A)
    for i in B:
        list_ = [j for j, val in enumerate(A) if val == i]
        if len(list_) == 1:
            return i


print('ANSWER', odd_occurances([9,3,9,3,9,7,9]))