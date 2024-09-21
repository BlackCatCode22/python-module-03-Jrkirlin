count = 0
total = 0.0
biggest_number = None
smallest_number = None
while True:
    stringvalue = input("Enter a number: ")
    if stringvalue == "done":
        break
    try:
        float_value = float(stringvalue)
    except:
        print("Invalid input. Please enter a number or type 'done' to compute.")
        continue

    if biggest_number is None:
        biggest_number = float_value
    elif float_value > biggest_number:
        biggest_number = float_value
    if smallest_number is None:
        smallest_number = float_value
    elif float_value < smallest_number:
        smallest_number = float_value
    count = count + 1
    total = total + float_value

average = total / count

print("Total:",total,"Count:",count,"Largest Number:",biggest_number,"Smallest Number:",smallest_number)