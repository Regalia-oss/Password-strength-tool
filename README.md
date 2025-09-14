# Password Strength & Hashing Tool

## Description
This is a Python tool that evaluates the strength of a user-provided password and securely hashes it. The tool demonstrates understanding of password security best practices, including scoring password strength and using modern hashing algorithms.

---

## Features
- Takes user password input.
- Scores password strength based on length, uppercase/lowercase letters, numbers, and special characters.
- Provides feedback as a score out of 5, with 1/5 being weak and 5/5 being the strongest.
- Hashes passwords securely using `bcrypt`

---

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/Regalia-oss/Password-strength-tool.git
cd Password-strength-tool
pip install bycrypt
python password_tool.py
