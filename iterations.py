def factorial(n):
    factorial_ =1
    for i in range(1,n+1):
        factorial_ *= i
    return factorial_


def star(n_rows):
    for i in range(n_rows, 0, -1):
        for j in range(n_rows-i):
            print(' ', end=" "),
        for k in range(2*i-1):
            print('*', end=" "),
        print("\n")


#commands
print(factorial(5))
print(star(5))
