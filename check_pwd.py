import re

def check_password_strength(password):
    # Check minimum length
    if len(password) < 8:
        return False
    
    # Check for uppercase and lowercase letters
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False

    # Check for at least one digit
    if not re.search(r'[0-9]', password):
        return False

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    return True


# Main program
if __name__ == "__main__":
    password = input("Enter your password: ")

    if check_password_strength(password):
        print("✅ Strong password! Your password meets all security criteria.")
    else:
        print("❌ Weak password! It should have:")
        print("- At least 8 characters")
        print("- Both uppercase and lowercase letters")
        print("- At least one number")
        print("- At least one special character (!, @, #, $, %, etc.)")