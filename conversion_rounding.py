def round_ans(val):




def to_celsius(to_convert):




def to_fahrenheit(to_convert):




# Main Routine / Testing starts here
to_c_test = [0, 100, -459]
to_f_test = [0, 100, 40, -273]

for item in to_f_test:
    ans = to_fahrenheit(item)
    print(f"{item} C is {ans} F")

print()

for item in to_c_test:
    ans = to_celsius(item)
    print(f"{item} F is {ans} C")
