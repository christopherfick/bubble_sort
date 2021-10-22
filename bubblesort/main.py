def bubble_sort(seq):
    """
    Returns a sorted list using the bubble sort algorithm

    Args:
        seq (list): unsorted list
    
    Returns:
        seq (list): A sorted version of the list in asscending order

    Examples:
        >>> bubble_sort([3,2,1])
        [1,2,3]

        >>> bubble_sort([10,2,4,100,7,8])
        [2,4,7,8,10,100]

        >>> bubble_sort([1])
        [1].
    """
    while True:
        triggered_swop = False
        for index, number in enumerate(seq):
            last_index = len(seq) - 1
            
            if index != last_index:
                next_number = seq[index + 1]
                if number > next_number:
                    seq[index], seq[index + 1] = swop(seq[index], seq[index + 1])
                    triggered_swop = True
                    
        if not triggered_swop:
            return seq


def swop(x, y):
    """Return the values x, y as y, x."""
    return y, x