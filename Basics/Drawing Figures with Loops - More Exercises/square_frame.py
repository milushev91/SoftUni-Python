def print_line(side, length) -> None: 
    """
    Print a line of a shape with customizable start/end characters and length.

    Parameters:
        side (str): The character used at the beginning and end of the line.
        length (int): The total number of characters in the printed line.

    Returns:
        None
    """
    print(side + " " + "- " * (length - 2) + side)


n = int(input())

for line_number in range(1, n + 1):
    side_char = "+" if line_number == 1 or line_number == n else "|"
    print_line(side_char, n)
