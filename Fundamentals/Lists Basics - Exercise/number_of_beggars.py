num_list = [int(num) for num in input().split(", ")]
beggars_count = int(input())

beggars = [0] * beggars_count
num_list_length = len(num_list)
beggars_length = len(beggars)
beggars_idx = 0

for idx in range(num_list_length):
    if beggars_idx == beggars_length:
        beggars_idx = 0
    
    beggars[beggars_idx] += num_list[idx]
    beggars_idx += 1

print(beggars)
