hall_rent = int(input())

statuettes_price = hall_rent - hall_rent * 0.30
catering_price = statuettes_price - statuettes_price * 0.15 
audio_price = catering_price / 2 

total_price = hall_rent + statuettes_price + catering_price + audio_price

print(f"{total_price:.2f}")
