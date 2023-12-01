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
def calibration_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

file_path = 'puzzleInput.txt'
calibration_document = calibration_file(file_path)
if calibration_document:
    result = calculateSum(calibration_document)
    print("The sum of all calibration values is:", result)