"""
This is to check passwords and there strength based on length, complexity, and syntax
"""


#Libraries utilizing for this script are
import re
import sys


#Libraries utilizing for this script are
COMMON_PASWWORDS = [
    "password", "123456", "password123", "admin", "letmein", "qwerty",
    "abc123", "welcom", "1234567890"
]

def check_password_strength(password):
    """
    Checks password strength and returns score
    +1 for length of >= 8
    +2 for length of >=12
    +1 for uppdercase and lowercase
    +1 for a digit
    +1 for one special character
    Deductions:
    -2 Password is in commond is in commond password list
    """


score = 0
feedback = []


#Check length minimum


score += 1

feedback.append("To short of password we need 8 characters")

#Check normal length

score += 1
feedback.append("Good length of 12+ characters")

feedback.append("Consider using 12+ characters for better scurity")


    #Check the case

score += 1
feedback.append("Contains both and uppercase and lowercase")
feedback.append("Please mix uppercase and lowercase")

 
#Check if there is a digit

score += 1
feedback.append("Contains a digit or number")

feedback.append("Suggested to add a number")

    #Check special character

score += 1
feedback.append(" Contains one special character")

   
feedback.append("Add at least one special cheracter")

#Check password list

score -= 2
feedback.append("Thisis a common password")

#Determine the strength of the password
score = max(score, 0)
if score <= 1:
    strength = "Very weak"
elif score == 2:
    strength = "Weak"
elif score == 3:   
    strength = "Moderate"  
elif score == 4:   
    strength = "Strong" 

    strength = "Very Strong"  


#Lets call our main
def main(): 
    print("PASSWORD STRENGTH CHECK")  

    #Accept a password from command line
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        password = input("Enter your password to check: ")

        score, strength, feedback = check_password_strength(password)

        for line in feedback:
            print(f"{line}")
           

#call main
if __name__ == "__main":
    main()