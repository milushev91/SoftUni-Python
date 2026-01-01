DAYS_IN_YEAR = 365
TOM_REST_NORM = 30000
WORK_DAYS_PLAY_MINUTES = 63
OFF_DAYS_PLAY_MINUTES = 127

off_days_count = int(input())

work_days_count = DAYS_IN_YEAR - off_days_count

work_days_play_minutes = work_days_count * WORK_DAYS_PLAY_MINUTES
off_days_play_minutes = off_days_count * OFF_DAYS_PLAY_MINUTES

total_play_time = work_days_play_minutes + off_days_play_minutes

difference = abs(total_play_time - TOM_REST_NORM)
play_hours = difference // 60
play_minutes = difference % 60

if total_play_time <= TOM_REST_NORM:
    print("Tom sleeps well")
    print(f"{play_hours} hours and {play_minutes} minutes less for play")
else:
    print("Tom will run away")
    print(f"{play_hours} hours and {play_minutes} minutes more for play")
