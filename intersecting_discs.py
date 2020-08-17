from itertools import combinations


def check_intersect(c1, c2, r1, r2):
    d = abs(c1 - c2)
    r = abs(r1 + r2)
    if d > r:
        return False
    else:
        return True


def solution(A):
    if A:
        a = list(range(0, len(A)))
        c = list(combinations(a, 2))
        print(c)
        counter = 0
        for i in c:
            bool_ = check_intersect(i[0], i[1], A[i[0]], A[i[1]])
            if bool_:
                counter += 1
        if counter > 10000000:
            return -1
        else:
            return counter
    else:
        return 0


print('NUMBER OF INTERSECTING PAIRS', solution([1, 5, 2, 1, 4, 0]))
