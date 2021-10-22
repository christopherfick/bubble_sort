from bubblesort import main

def test_main():
    assert main.bubble_sort([3, 2, 1]) == [1, 2, 3], 'incorrect'
    assert main.bubble_sort([5, 10, 100, 7, 2, 3, 1]) == [1, 2, 3, 5, 7, 10, 100], 'incorrect'
    assert main.bubble_sort([5, 4, 3, 3, 2, 1]) == [1, 2, 3, 3, 4, 5], 'incorrect'