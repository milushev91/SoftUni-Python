pool_volume = int(input())
pipe_1_debit = int(input())
pipe_2_debit = int(input())
hours = float(input())

pipe_1_volume = pipe_1_debit * hours
pipe_2_volume = pipe_2_debit * hours
pipes_volume = pipe_1_volume + pipe_2_volume

if pipes_volume <= pool_volume:
    pool_filled_percent = pipes_volume / pool_volume * 100
    pipe1_filling_percent = pipe_1_volume / pipes_volume * 100
    pipe2_filling_percent = pipe_2_volume / pipes_volume * 100
    print(f"The pool is {pool_filled_percent:.2f}% full. Pipe 1: {pipe1_filling_percent:.2f}%. Pipe 2: {pipe2_filling_percent:.2f}%.")
else:
    print(f"For {hours} hours the pool overflows with {pipes_volume - pool_volume:.2f} liters.")
