def get_user_info():
    
    filename = input("Enter filename: ")
    with open(filename, 'w') as file:
        name = input("What is your name: ")
        file.write(f"{name} \n")

        surname = input("What is your surname: ")
        file.write(f"{surname} \n")

        date_of_birth = input("What is your date of birth: ")
        file.write(f"{date_of_birth} \n")

        favourite_duck = input("What is your favourite duck: ")
        file.write(f"{favourite_duck} \n")

        kitchen_sink = input("Is the kitchen sink an important accessory (yes or no): ")
        while kitchen_sink.lower() not in ["yes","no"]:
            kitchen_sink = input("Is the kitchen sink an important accessory (yes or no): ")
        file.write(f"{kitchen_sink} \n")

        phone_number = input("What are your digits (digits only): ")
        while not phone_number.isdigit():
            phone_number = input("What are your digits (digits only): ")
        file.write(f"{phone_number} \n")

        custom_question = input("Your favourite six characters? (exactly 6 characters): ")
        while len(custom_question)!=6:
            custom_question = input("Your favourite six characters? (exactly 6 characters): ")
        file.write(f"{custom_question} \n")

    print(f"File contents of {filename} after program completion:")
    with open(filename, 'r') as file:
        print(file.read())

get_user_info()