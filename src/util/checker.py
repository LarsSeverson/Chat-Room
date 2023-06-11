import re

# for later use
email_regex = r'\b[A-Za-z0-0._%+-]+@[A-Za-z0-9.-]+\[A-Z|a-z]{2,7}\b'
id_regex = r'^\d{4}$'

def check_user(user) -> bool:
    if user:
        return True
    return False

def check_id(id) -> bool:
    global id_regex
    int_check = bool(re.match(id_regex, id))

    if id and int_check:
        return True

    return False