digit_list = [int(digit) for digit in input()]
print("".join(sorted((str(digit) for digit in digit_list), reverse=True)))
