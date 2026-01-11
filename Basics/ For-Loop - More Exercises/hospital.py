days = int(input())

doctors_count = 7
treated_patiens_count = untreated_patiens_count = 0

for day in range(1, days + 1):
    patiens_count = int(input())

    if day % 3 == 0 and untreated_patiens_count > treated_patiens_count:
        doctors_count += 1
    
    if doctors_count >= patiens_count:
        treated_patiens_count += patiens_count
    else:
        treated_patiens_count += doctors_count
        untreated_patiens_count += patiens_count - doctors_count
    
print(f"Treated patients: {treated_patiens_count}.")
print(f"Untreated patients: {untreated_patiens_count}.")
    
