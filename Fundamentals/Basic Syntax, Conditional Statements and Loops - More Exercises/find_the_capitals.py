string = input()
string_len = len(string)
print([idx for idx in range(string_len) if string[idx].isupper()])
