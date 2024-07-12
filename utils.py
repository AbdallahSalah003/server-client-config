import string
import itertools
import csv
from error_handling import InvalidLogic, InvalidInput


def validate_inputs(inputs):
    if not len(inputs):
        raise InvalidLogic(f"No server options provided")
    special_chars = set(string.punctuation)
    special_chars.add(' ')
    for arg in inputs:
        if any(char in special_chars for char in arg):
            raise InvalidInput(f"Special chars are not allowed")
    if len(inputs) != len(set(inputs)):
        raise InvalidLogic(f"Duplicate server options are not allowed")


def generate_combinations(options):
    header = ["TestCase ID"]
    for i in range(0, len(options)):
        header.append(f"Master Option For {options[i]}")
    for i in range(0, len(options)):
        header.append(f"Client Option For {options[i]}")
    formatted_combinations = [header]
    counter = 0
    values = ["TRUE", "FALSE", "NA"]
    n = 2 * len(options)
    combinations = list(itertools.product(values, repeat=n))
    if n:
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
    # iterate over all test cases combinations
    for i in range(1, len(formatted_combinations)):
        formatted_combinations[i].append("ValidTC_placeholder")
        # iterate over master options' values
        for j in range(1, len(options) + 1):
            if formatted_combinations[i][j] != "NA":
                formatted_combinations[i].append(formatted_combinations[i][j])
            else:
                formatted_combinations[i].append("TRUE")
    return formatted_combinations


def is_valid_tc(combinations, options):
    #  a test case is valid if the client values is "NA" or same as Expected
    n = len(options)
    start_ind = n + 1
    end_ind = 2 * n + 1
    # iterate over all test cases
    for i in range(1, len(combinations)):
        invalid = 0
        # iterate over the client options' values
        for j in range(start_ind, end_ind):
            if combinations[i][j] not in ("NA", combinations[i][j+n+1]):
                invalid = 1
                break
        if invalid:
            combinations[i][end_ind] = "NO"
        else:
            combinations[i][end_ind] = "YES"
    set_expected_values_to_na_if_invalid(combinations, len(options))
    return combinations


def set_expected_values_to_na_if_invalid(combinations, n):
    for i in range(1, len(combinations)):
        # invalid test case
        if combinations[i][2 * n + 1] == "NO":
            for j in range(2 * n + 2, len(combinations[i])):
                combinations[i][j] = "NA"



def csv_output(result):
    with open('output.csv', 'w') as outputfile:
        csv_writer = csv.writer(outputfile, delimiter=',')
        for row in result:
            csv_writer.writerow(row)