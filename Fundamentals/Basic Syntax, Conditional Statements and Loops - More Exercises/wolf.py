wolves = input().split(", ")

wolves_len = len(wolves)

if wolves[wolves_len - 1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    wolf_index = wolves.index("wolf")
    print(f"Oi! Sheep number {wolves_len - wolf_index - 1}! You are about to be eaten by a wolf!")
