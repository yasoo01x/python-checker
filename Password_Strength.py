import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    if criteria_met == 5:
        return "Strong"
    elif criteria_met >= 3:
        return "Moderate"
    else:
        return "Weak"

password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password Strength: {strength}")
