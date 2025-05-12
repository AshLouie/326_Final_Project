import re

def valid_name(name):
    """
    Check if the input's name is valid

    Args:
        name (str): player's name
    """
    pattern = r"[a-zA-Z]*$"
    return re.match(pattern, name) is not None