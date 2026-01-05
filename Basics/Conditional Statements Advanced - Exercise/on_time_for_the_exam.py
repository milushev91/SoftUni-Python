exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_minutes = exam_hour * 60 + exam_minute
arrival_minutes = arrival_hour * 60 + arrival_minute
difference = abs(exam_minutes - arrival_minutes)

hours = 0
minutes = difference % 60
units = "minutes"
arrival_time = ""

if difference > 59:
    hours = difference // 60

if exam_minutes >= arrival_minutes:
    
    if difference == 0: #On time 
        print("On time")
        quit()
    elif difference <= 30:
        print("On time")
    else:
        print("Early")
    
    arrival_time = "before"
        
else:
    print("Late")
    arrival_time = "after"

if hours:
    units = "hours"
    print(f"{hours}:", end="")
    
    if minutes < 10:
        minutes = f"0{minutes}"

print(f"{minutes} {units} {arrival_time} the start")
