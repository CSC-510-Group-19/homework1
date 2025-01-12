def non_recursivefib(num):
    last, curr = 0, 1
    for ( in range(2, num + 1)):
        print(last, end = ' ')
        last, curr = curr, last + curr
    print(curr)
    return curr

non_recursive_fib(10)