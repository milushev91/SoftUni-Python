#ABxyBA 

##@11@#|$A12A$|%B13B%|&C21C&|'D22D'|(E23E(|

x = int(input())
y = int(input())
max_password_count = int(input())

a = 35
b = 64
password_counter = 0
stop_loops = False

for x_val in range(1, x + 1):
    for y_val in range(1, y + 1):

        password_counter += 1
        if password_counter > max_password_count:
            stop_loops = True
            break
        a_char = chr(a)
        b_char = chr(b)
        
        print(F"{a_char}{b_char}{x_val}{y_val}{b_char}{a_char}", end="|")


        a += 1
        b += 1

        if a == 56:
            a = 35

        if b == 97:
            b = 64

    if stop_loops:
        break

