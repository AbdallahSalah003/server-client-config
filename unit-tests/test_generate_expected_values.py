from utils import generate_expected_values


def test_generate_expected_values_with_no_options():
    formatted_combinations = [["TestCase ID"]]
    options = []
    result = generate_expected_values(formatted_combinations, options)
    expected = [["TestCase ID", "Valid TC"]]
    assert result == expected, f"Expected {expected}, but got {result}"


def test_generate_expected_values_one_option():
    formatted_combinations = [
        ["TestCase ID", "Master Option For Option1", "Client Option For Option1"],
        [1, "TRUE", "FALSE"],
        [2, "NA", "TRUE"]
    ]
    options = ["Option1"]
    result = generate_expected_values(formatted_combinations, options)
    expected = [
        ["TestCase ID", "Master Option For Option1", "Client Option For Option1", "Valid TC", "Expected Option1"],
        [1, "TRUE", "FALSE", "ValidTC_placeholder", "TRUE"],
        [2, "NA", "TRUE", "ValidTC_placeholder", "TRUE"]
    ]
    assert result == expected, f"Expected {expected}, but got {result}"


def test_generate_expected_values_multiple_options():
    formatted_combinations = [
        ["TestCase ID", "Master Option For Option1", "Master Option For Option2", "Client Option For Option1",
         "Client Option For Option2"],
        [1, "TRUE", "FALSE", "NA", "TRUE"],
        [2, "NA", "TRUE", "TRUE", "FALSE"]
    ]
    options = ["Option1", "Option2"]
    result = generate_expected_values(formatted_combinations, options)
    expected = [
        ["TestCase ID", "Master Option For Option1", "Master Option For Option2", "Client Option For Option1",
         "Client Option For Option2", "Valid TC", "Expected Option1", "Expected Option2"],
        [1, "TRUE", "FALSE", "NA", "TRUE", "ValidTC_placeholder", "TRUE", "FALSE"],
        [2, "NA", "TRUE", "TRUE", "FALSE", "ValidTC_placeholder", "TRUE", "TRUE"]
    ]
    assert result == expected, f"Expected {expected}, but got {result}"
