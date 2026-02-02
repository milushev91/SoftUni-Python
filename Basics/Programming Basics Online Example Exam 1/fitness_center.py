visitors_count = int(input())

visitors_info = {
  "back": 0,
  "chest": 0,
  "legs": 0, 
  "abs": 0,
  "protein shake": 0,
  "protein bar": 0,
}
training_visitors_count = 0

for _ in range(visitors_count):
    activity = input().casefold()
    
    visitors_info[activity] += 1
    
    if "protein" not in activity:
        training_visitors_count += 1

for activity, count in visitors_info.items():
    print(f"{count} - {activity}")

training_visitors_percent = training_visitors_count / visitors_count * 100

print(f"{training_visitors_percent:.2f}% - work out")
print(f"{(100 - training_visitors_percent):.2f}% - protein")
