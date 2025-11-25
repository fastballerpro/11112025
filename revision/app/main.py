

from revision.utils import is_strong_password, has_duplicates, temperature_validator

if __name__ == "__main__":
    password = "StrongPass123"
    if is_strong_password(password):
        print("password is strong")
    else:
        print("password is easy")

    
    items = [1, 2, 3, 2]
    if has_duplicates(items):
        print("there are duplicates")
    else:
        print("there arent any duplicates")

  
    temp = 25
    if temperature_validator(temp):
        print("temperature is warm")
    else:
        print("temperature is cold")
