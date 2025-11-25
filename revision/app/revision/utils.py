

def is_strong_password(password: str) -> bool:
   
    has_number = any(ch.isdigit() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    
    return len(password) >= 8 and has_number and has_upper and has_lower


def has_duplicates(items: list[int | float | str | bool]) -> bool:
    
    return len(set(items)) != len(items)


def temperature_validator(temp: float) -> bool:
    
    return temp > 20
