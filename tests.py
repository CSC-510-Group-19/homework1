from myfile import non_recursive_fib

# tests that the fifth fib number is 3
def test_fifth_num():
    assert non_recursive_fib(5) == 3

# tests that the tenth fib number is 55 (should be 34. designed to fail for assignment)
def test_tenth_num():
    assert non_recursive_fib(10) == 55
