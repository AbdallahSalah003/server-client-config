from error_handling import InvalidLogic, InvalidInput
import string


def validate_inputs(inputs):
    if not len(inputs):
        raise InvalidLogic(f"No server options provided")
    special_chars = set(string.punctuation)
    for arg in inputs:
        if any(char in special_chars for char in arg):
            raise InvalidInput(f"Special chars are not allowed")
    if len(inputs) != len(set(inputs)):
        raise InvalidLogic(f"Duplicate server options are not allowed")
