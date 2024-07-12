from utils import is_valid_tc


def test_is_valid_tc_with_valid_cases():
    options = ["Option1", "Option2"]
    combinations = [
        ["TestCase ID", "Master Option For Option1", "Master Option For Option2", "Client Option For Option1",
         "Client Option For Option2", "Valid TC", "Expected Option1", "Expected Option2"],
        [1, "NA", "TRUE", "TRUE", "NA", "ValidTC_placeholder", "TRUE", "TRUE"],
        [2, "FALSE", "NA", "NA", "TRUE", "ValidTC_placeholder", "FALSE", "TRUE"]
    ]
    result = is_valid_tc(combinations, options)
    expected = [
        ["TestCase ID", "Master Option For Option1", "Master Option For Option2", "Client Option For Option1",
         "Client Option For Option2", "Valid TC", "Expected Option1", "Expected Option2"],
        [1, "NA", "TRUE", "TRUE", "NA", "YES", "TRUE", "TRUE"],
        [2, "FALSE", "NA", "NA", "TRUE", "YES", "FALSE", "TRUE"]
    ]
    assert result == expected, f"Expected {expected}, but got {result}"


def test_is_valid_tc_with_invalid_cases():
    options = ["Option1"]
    combinations = [
        ["TestCase ID", "Master Option For Option1", "Client Option For Option1", "Valid TC", "Expected Option1"],
        [1, "FALSE", "TRUE", "ValidTC_placeholder", "FALSE"],
        [2, "NA", "FALSE", "ValidTC_placeholder", "TRUE"]
    ]
    result = is_valid_tc(combinations, options)
    expected = [
        ["TestCase ID", "Master Option For Option1", "Client Option For Option1", "Valid TC", "Expected Option1"],
        [1, "FALSE", "TRUE", "NO", "NA"],
        [2, "NA", "FALSE", "NO", "NA"]
    ]
    assert result == expected, f"Expected {expected}, but got {result}"
