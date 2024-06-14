def caesar_cipher(input_string):
    
    def encrypt_char(char): # This function takes a single character, capitalizes it, and determines whether it's a letter
        char_upper = char.upper() # Changes character to uppercase
        
        if "A"<=char_upper<="Z": # Verifies if the character (A–Z) is a letter.
            char_val = ord(char_upper)
            rotated_val = char_val+13
            
            if rotated_val>ord("Z"): # If rotated_val exceeds 'Z', wrap around
                rotated_val-=26
                
            return chr(rotated_val)
        
        else:
            return char # This makes sure that the Caesar Cipher encryption does not affect non-letter characters like numbers, punctuation, or spaces.
        
 
    encrypted_chars = [encrypt_char(char) for char in input_string] # This produces a list with each entry representing the outcome of encrypting each character in the input_string using the encrypt_char function.
    encrypted_string = ''.join(encrypted_chars) # Makes the final encrypted result of the input string using the Caesar Cipher, transforming the list of encrypted characters back into a single string.
    return encrypted_string

input_text = input("Enter a message to encrypt: ") # Asks the user for their preffered input 
encrypted_text = caesar_cipher(input_text) # Calls the caesar function

print("Encrypted:", encrypted_text) # Prints the encrypted text






 
        
        