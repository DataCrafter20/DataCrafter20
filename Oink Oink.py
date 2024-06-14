def pig_latin_converter(word): #A function called pig_latin_converter which accepts one parameter called word.
    
    vowels = "AEIOUaeiou" #A string variable called vowels that stores the vowels found in the English alphabet.
    if word[0] in vowels: #Verifies if the initial letter of the word is included in the vowels string.
        return word + 'way' #If word begins with a vowel, it will be combined with 'way' before returning.
    else: #Starts the code block that will run if the initial letter of the word is not a vowel.
        return word[1:] + word[0] + 'ay' #Changes word by moving its initial letter to the end and adding 'ay' if it begins with a consonant.
    
def main(): #Describes the main purpose, the starting point of the program.

    user_input = input("Enter a normal text: ") #Asks the user to enter some text, and saves it into the variable user_input.
    terms = user_input.split() #Breaks down user_input into a series of individual words.
    pig_latin_terms = [pig_latin_converter(word) for word in terms] #Uses a list comprehension with pig_latin_converter to change every word in terms to Pig Latin.
    pig_latin_text = ''.join(pig_latin_terms) #Joins the pig_latin_terms list to create one string called pig_latin_text.
    print("Pig latin text: ", pig_latin_text) #Outputs the Pig Latin text with the prefix "Pig latin text: ".

if __name__== "__main__": #Verifies if the script is executed directly
    main() #Calls the main() function, initiating the program's execution.