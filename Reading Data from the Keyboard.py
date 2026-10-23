print("========================================")
print("     SIMPLE CONSOLE INPUT & DISPLAY     ")
print("========================================")

# ---------------------------------------------------------
# 1. Read a sequence of numbers from the keyboard
# ---------------------------------------------------------
print("\n--- Part 1: Sequence of Numbers ---")
user_input = input("Enter a few numbers separated by spaces (e.g., 5 10 15): ")

# Split the string into a list of strings based on spaces
string_list = user_input.split()

# Convert each string in the list into an integer using a basic loop
sequence = []
for item in string_list:
    number = int(item)
    sequence.append(number)

print("You entered this sequence:", sequence)


# ---------------------------------------------------------
# 2. Read an array (matrix) with user-specified dimensions
# ---------------------------------------------------------
print("\n--- Part 2: 2D Array (Matrix) ---")
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []

# Loop to create each row
for i in range(rows):
    row_input = input(f"Enter {cols} numbers for row {i + 1} separated by spaces: ")
    row_string_list = row_input.split()
    
    # Convert the row items into integers
    row_numbers = []
    for item in row_string_list:
        row_numbers.append(int(item))
        
    # Add the row to our matrix
    matrix.append(row_numbers)


# ---------------------------------------------------------
# 3. Display the results in a readable format
# ---------------------------------------------------------
print("\n========================================")
print("             FINAL DISPLAY              ")
print("========================================")

print("1. Your sequence:")
print(sequence)

print("\n2. Your array (matrix):")
for row in matrix:
    print(row)

print("========================================")