def is_strong_password(password: str) -> bool:
  
    has_number = any(ch.isdigit() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    
    return len(password) >= 8 and has_number and has_upper and has_lower


def has_duplicates(items: list[int | float | str | bool]) -> bool:
   
    return len(set(items)) != len(items)


def is_temperature_warm(temp: float) -> bool:
    
    return temp > 20

def is_valid_email(value: str) -> bool:
    if not value or value.startswith(("@", ".")) or value.endswith(("@", ".")):
        return False

    if value.count("@") != 1:
        return False

    local, domain = value.split("@")

    if "." not in domain:
        return False

    return True


def avg(values: list[float]) -> float:
    if not values:
        raise ValueError("List is empty")

    return sum(values) / len(values)


def uah_to_usd(amount: float, rate: float) -> float:
    if amount <= 0:
        raise ValueError("Amount must be > 0")
    if rate <= 0:
        raise ValueError("Rate must be > 0")

    return amount / rate