def convert_to_decimal(number, base): #A function that converts a number from a specified base to decimal.
    return int(str(number), base) #This int() function converts the given number from its base to decimal.

first_number = 11 #Sets the variable first_number equal to 11.
first_base = 8 #Sets the variable first_base to have a value of 8, specifying that it is in base 8 (octal).
second_number = 24 #Sets the variable second_number equal to 24.
second_base = 5 #Sets second_base as 5, showing it is in base 5.
result = convert_to_decimal(first_number, first_base)+convert_to_decimal(second_number, second_base) #Calls the convert_to_decimal function for both first_number and second_number using their specific bases, and then combines the outcomes.

print(f"Result:{result} (base 10)") #Prints the outcome of the sum in decimal.