def calculateSum(calibration_txt):
    sum = 0
    
    for line in calibration_txt:
        # Find the first and last digits and combine them to form a two-digit number
        first_digit = next(char for char in line if char.isdigit())
        last_digit = next(char for char in reversed(line) if char.isdigit())
        new_digit = int(first_digit + last_digit)

        # Add the calibration value to the total sum
        sum += new_digit

    return sum
calibration_document = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
]

result = calculateSum(calibration_document)

# Print the result
print("The sum of all calibration values is:", result)