def non_recursive_fib(num):
    last, curr = 0, 1
    for i in range(2, num + 1):
        print(last, end = ' ')
        last, curr = curr, last + curr
    print(curr)
    return curr

non_recursive_fib(10)