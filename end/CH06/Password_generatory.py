"""
Password Generator

A secure password generator that has a minimum length of 8
"""
#Libaries utilized
import random
import string


#Define character pools
UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGTTS = string.digits
SPECIAL = r"!@#$%^&*()_-|\;<>"

# Minimum password length
MIN_LENGTH = 8

#Helper function

def get_yes_or_no(prompt: str) -> bool:
    """ Ask the user for a yes or no question"""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
          return True
        if answer in ("n", "no"):
          return True
    print(" Please enter yes or no: ")

def get_password_length() -> int:
     while True:
        try:
           length = int(input("How long do you want the password?"))
           if length >= MTN_LENGTH: 
            return length
           print("Please enter a valid length try again")
        except ValueError:
           print("Please enter a whole number")   


def get_criteria() -> dict:
    """Take length, uppercase, lowercase, digits, special input from user"""
    length = get_password_length()
    criteria ={
        "length": length,
        "uppercase": get_yes_or_no(" Do you want uppercase letters?"),
        "lowercase": get_yes_or_no(" Do you want lowercase letters?"),
        "digits": get_yes_or_no("Numbers (0-9)"),
        "special": get_yes_or_no(" Do you want special characters"),
    }

    #Validator of criteria
    if not any ([criteria["uppercase"], criteria["lowercase"],
                 criteria["digits"], criteria["special"]]):
      print("You must select one character type")
      return get_criteria()
    return criteria

def build_pool(criteria: dict) -> tuple[str,list[str]]:
    """This is a character pool"""
    pool = ""
    required = []

    if criterial["uppercase"]:
        pool += UPPERCASE
        required.append(random.choice(UPPERCASE))

    if criteria["lowercase"]:
        pool += LOWERCASE
        required.append(random.choice(LOWERCASE))

    if criteria["digits"]:
        pool += DIGITS 
        required.append(random.choice(DIGITS)) 

    if  ["special"]: 
      pool += SPECIAL
    required.append(random.choice(SPECIAL))  
    
def generate_password(criteria: dict) -> str:
    """Generation of password creator """
    pool, required = build_pool(criteria)
    length = criterial["length"]    

    #Fill any remaining slot with random characters
    reamining_count = length - len(required)
    remaing = [random.choice(pool)for _ in range(reamining_count)]

    password_chars = required + remaing
    random.shuffle(password_chars)


    return"".join(password_chars)


def main():

    while True:
        criteria = het_criteria()
        password = generate_password()
        print("This is your generated password")
        print(f"{password}")

        if not get_yes_or_no("Generate another password (y/n)"):
            print("Stay secure")
            break
        print()

    if __name__ == "__main__":
      main()