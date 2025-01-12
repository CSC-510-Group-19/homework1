from myfile import non_recursive_fib

def test_fifth_num():
    assert non_recursive_fib(5) == 3

def test_tenth_num():
    assert non_recursive_fib(10) == 55
