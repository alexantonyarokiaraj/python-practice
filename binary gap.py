def decimalToBinary(n):
    return bin(n).replace("0b", "")


def binary_gap(num):
    x = str(decimalToBinary(num))
    print(x)
    ind = [i for i, val in enumerate(x) if val == '0']
    print(ind)
    if not ind:
        return 0
    else:
        lengths = []
        counter = 1
        B = []
        for j, val in enumerate(ind):
            if j != len(ind) - 1:
                if ind[j + 1] == ind[j] + 1:
                    counter += 1
                    B.append(ind[j])
                    print('list', j, ind[j], B)
                else:
                    B.append(ind[j])
                    print('list', j, ind[j], B)
                    if B[-1] != len(x) - 1:
                        print('check first', j, B[0], B[-1], x[B[0] - 1], x[B[-1] + 1])
                        if B[0] != 0 and x[B[0] - 1] == '1' and x[B[-1] + 1] == '1':
                            print('APPENDING COUNTER', counter)
                            lengths.append(counter)
                    counter = 1
                    B = []
            else:
                B.append(ind[j])
                print('list', j, ind[j], B)
                if B[-1] != len(x) - 1:
                    print('check', B[0], B[-1], x[B[0] - 1], x[B[-1] + 1])
                    if B[0] != 0 and x[B[0] - 1] == '1' and x[B[-1] + 1] == '1':
                        lengths.append(counter)
        if lengths:
            return max(lengths)
        else:
            return 0


print('ANSWER', binary_gap(1041))
