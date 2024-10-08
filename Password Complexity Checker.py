import re

def assess_password_strength(password):
    score = 0
    feedback = []
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.") #Check Legnth
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.") #Check Uppercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.") #Check Lowercase letters
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.") #Checks digits
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., !, @, #, etc.).") #Check special characters
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    print(f"Password Strength: {strength}") #Password Stregnth
    if feedback:
        print("Suggestions to improve your password--> ")
        for suggestion in feedback:
            print(f"> {suggestion}")


def main():
    print(">>>> Password Complexity Checker <<<<")
    password = input("Enter a password to assess its strength--> ")
    assess_password_strength(password)


if __name__ == "__main__":
    main()
