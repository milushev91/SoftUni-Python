string_1 = input()
string_2 = input()

strings_len = len(string_1)
unique_strings = set()

for idx in range(strings_len):
    if string_1[idx] != string_2[idx]:
        result_string = string_2[:idx+1] + string_1[idx + 1::]
    
        print(result_string)
