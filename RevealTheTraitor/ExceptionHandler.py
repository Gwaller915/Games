def get_valid_number():
    try:
        number = int(input("    Please enter a number: "))
        print()
        # Additional validation can be added here if needed
        return number  # Return the number if no exception is raised
    except ValueError:
        print("    Hmm, I don't think I can do that. You should try again.")
        print()
        return get_valid_number()  # Recursively call the function to prompt again

def get_yes_or_no():
    while True:
        try:
            user_input = input("Enter 'y' to continue or 'n' to exit: ").strip().lower()
            if user_input == 'y':
                return True
            elif user_input == 'n':
                return False
            else:
                raise ValueError("Invalid input. Enter 'y' or 'n'.")
        except ValueError as e:
            get_yes_or_no()

