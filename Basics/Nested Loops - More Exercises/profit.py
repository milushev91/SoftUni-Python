one_lv_count = int(input())
two_lv_count = int(input())
five_lv_count = int(input())
amount = int(input())

for multiplier1 in range(one_lv_count + 1):
    for multiplier2 in range(two_lv_count + 1):
        for multiplier3 in range(five_lv_count + 1):
            ones = multiplier1 * 1
            twos = multiplier2 * 2
            fives = multiplier3 * 5

            sum_money = ones + twos + fives

            if sum_money == amount:
                print(f"{multiplier1} * 1 lv. + {multiplier2} * 2 lv. + {multiplier3} * 5 lv. = {amount} lv.")
