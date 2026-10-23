print("\"1 December 1918\" University of Alba Iulia")
print("Computer Science Department")
print("Course: Fundamental Algorithms")
print("Lab 1: Reading a String from a Filerint")
print("By: Osatohanmwen Davidson Ikponmwenosa")


# ---------------------------------------------------------
# 1. Read the name of the file from the keyboard
filename = input("Enter the name of the text file: ")

# 2. Try to open the file and handle the case where it doesn't exist
try:
    file = open(filename, "r")
    
    # Read the string of numbers from the file
    content = file.read()
    
    # Display the read values
    print("The numbers in the file are:")
    print(content)
    
    # Always close the file when you are done
    file.close()

except:
    # Display a message if the file does not exist
    print("Error: The file could not be found.")