#if condition
#compare minimum marks to mark of the studentdef get_userpassword():

def get_user_password():
    try:
        user_password = int(input("Enter your password: "))  # Prompt user for input
        if user_password == 12345:
            print("Access granted")  # If password matches
        else:
            print("Access denied")  # If password does not match
    except ValueError:
        print("Invalid input. Please enter a numeric password.")  # Handle non-integer input
    except Exception as e:  # Catch any other exceptions
        print("An error occurred:", e)  # Print the error message
        return None  # Optionally return None in case of an error

    return user_password  # Return the user password



