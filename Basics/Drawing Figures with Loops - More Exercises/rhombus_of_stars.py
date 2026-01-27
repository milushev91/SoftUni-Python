def print_triangle(start, end, step) -> None:
    """
    Print one half of a triangle by looping from start to end with a given step.

    The function prints rows where each row contains a decreasing number of
    spaces and an increasing (or decreasing) number of stars, depending on
    the loop direction. It relies on an external variable `n` that determines
    the maximum triangle width.

    Parameters:
        start (int): Initial value of the loop counter.
        end (int): Stop value of the loop counter (non-inclusive).
        step (int): Step value that controls whether the loop increments or decrements.

    Returns:
        None
    """
    
    for i in range(start, end, step):
        spaces = n - i
        stars = i
        print(spaces * " " + stars * "* ")

n = int(input())

print_triangle(start=1, end=n + 1, step=1)
print_triangle(start=n-1, end=0, step=-1)
