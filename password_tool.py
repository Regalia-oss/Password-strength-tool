import re
import bcrypt

def password_length(password):
"""Returns a strength score from 0-5 and feedback"""
	score = 0
	feedback = []

#length check
if len(password) >= 8:
	score += 1
else:
	feedback.append("Password should be at least 8 characters.")
if re.search(r"[A-Z]", password):
	score += 1
else:
	feedback.append("Add at least one uppercase letter.")
if re.search(r"[a-z]", password):
	score += 1
else:
	feedback.append("Add at least one lowercase letter.")
if re.search(r"[0-9]", password):
	score += 1
else:
	feedback.append("Add at least one number.")
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
	score += 1
else:
	feedback.append("Add at least one special character (!@#$...).")
return score, feedback
def hash_password(password):
    """Hashes a password with bcrypt"""
    # bcrypt requires bytes, not str
    password_bytes = password.encode('utf-8')
    # Generate salt and hash
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed
def main():
    print("🔐 Password Strength & Hashing Tool 🔐\n")

    # Get user input
    password = input("Enter a password: ")

    # Check strength
    score, feedback = password_strength(password)
    print(f"\nStrength score: {score}/5")
    if feedback:
        print("Suggestions to improve:")
        for f in feedback:
            print("-", f)
    else:
        print("Your password is strong ✅")

    # Hash the password
    hashed_password = hash_password(password)
    print(f"\nHashed password (bcrypt): {hashed_password.decode()}")


if __name__ == "__main__":
    main()
initial password tool code
