import string
import itertools
from error_handling import InvalidLogic, InvalidInput


def validate_inputs(inputs):
    if not len(inputs):
        raise InvalidLogic(f"No server options provided")
    special_chars = set(string.punctuation)
    for arg in inputs:
        if any(char in special_chars for char in arg):
            raise InvalidInput(f"Special chars are not allowed")
    if len(inputs) != len(set(inputs)):
        raise InvalidLogic(f"Duplicate server options are not allowed")


def generate_combinations(options):
    header = ["TestCaseID"]
    for i in range(0, len(options)):
        header.append(f"Master Option For {options[i]}")
    for i in range(0, len(options)):
        header.append(f"Client Option For {options[i]}")
    formatted_combinations = [header]
    counter = 0
    values = ["TRUE", "FALSE", "NA"]
    n = 2 * len(options)
    combinations = list(itertools.product(values, repeat=n))
    for i in range(0, 3 ** n):
        counter += 1
        tmp = [counter] + list(combinations[i])
        formatted_combinations.append(tmp)
    return formatted_combinations


def generate_expected_values(formatted_combinations, options):
    extend_header = ["Valid TC"]
    for op in options:
        extend_header.append(f"Expected {op}")
    formatted_combinations[0] = formatted_combinations[0] + extend_header
    # start index of expected values
    # we need to skip field "Valid TC"
    start = 2 * len(options) + 2
    for i in range(1, len(formatted_combinations)):
        formatted_combinations[i].append("placeholder")
        for j in range(1, len(options) + 1):
            if formatted_combinations[i][j] != "NA":
                formatted_combinations[i].append(formatted_combinations[i][j])
            else:
                formatted_combinations[i].append("TRUE")
    return formatted_combinations

