from utils import is_strong_password, has_duplicates, temperature_validator

if __name__ == "__main__":
    print(is_strong_password("StrongPass123"))
    print(has_duplicates([1, 2, 3, 2]))
    print(temperature_validator(25))
