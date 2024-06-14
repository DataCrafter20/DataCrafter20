def count_character_frequency(input_string):
    frequency ={} #Creates a dictionary named frequency with no items in it.
    for char in input_string: #Goes through every character in the input string.
        if char in frequency: #Verifies whether the character char already exists as a key in the frequency dictionary.
            frequency[char] +=1 #If the character is already a key, increase its corresponding value in the frequency.
        else: #If the character is not a frequency key.
            frequency[char] =1 #Includes character as a new entry in frequency with a count of 1.
    for key,value in frequency.items(): #Goes through every key-value pair in the frequency dictionary.
        print(f"{key}: {value}") #prints every character key together with its respective frequency value.
    
input_sequence = "My name is Bob Ross"
count_character_frequency(input_sequence)