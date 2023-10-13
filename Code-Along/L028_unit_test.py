from L027_module import square, greet


def test_positive_square():
    assert square(2) == 4
    assert square(5) == 25

def test_negative_square():
    assert square(-2) == 4
    assert square(-5) == 25

def test_zero_square():
    assert square(0) == 0

def test_greet_default():
    assert greet() == "Hello, world"
    
def test_greet_argument():
    assert greet("Joakim") == "Hello, Joakim"

if __name__ == "__main__":
    main()

