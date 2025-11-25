def is_strong_password(password: str) -> bool:
  
    check_for_numbers = any(ch.isdigit() for ch in password)
   
    has_capital_letter = any(ch.isupper() for ch in password)
   
    has_small_letter = any(ch.islower() for ch in password)

  
    return len(password) >= 8 and d and u and l

def has_duplicates(list: list[int | float | str | bool]) -> bool:
    return len(set(list)) != len(list)



def temperature_validator(temp: float) -> str:
    
    if temp > 20:
        return "тепло"
    else:
        return "холодно"
