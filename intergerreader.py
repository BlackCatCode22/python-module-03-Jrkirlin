count = 0
total = 0.0
while True:
    stringvalue = input("Enter a number: ")
    if stringvalue == "done":
        break
    try:
        float_value = float(stringvalue)
    except
        print("Invalid input. Please enter a number or type 'done' to compute.")
        continue
    #print(float_value)
    count = count + 1
    total = total + float_value
average = total / count

#print("All Done")
print("Total:",total,"Count:",count,"Average:",average)