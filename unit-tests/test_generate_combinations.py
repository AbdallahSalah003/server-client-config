from utils import generate_combinations


def test_generate_combinations_with_no_options():
    result = generate_combinations([])
    expected_header = ["TestCase ID"]
    assert result == [expected_header], f"Expected {[expected_header]}, but got {result}"


def test_generate_combinations_one_option():
    result = generate_combinations(["Option1"])
    expected_header = ["TestCase ID", "Master Option For Option1", "Client Option For Option1"]
    assert result[0] == expected_header, f"Expected {expected_header}, but got {result[0]}"
    assert len(result) == 10, f"Expected 10 rows, but got {len(result)}"  # 3^2 = 9 combinations + header
    assert result[1] == [1, "TRUE", "TRUE"], f"Unexpected combination: {result[1]}"
    assert result[9] == [9, "NA", "NA"], f"Unexpected combination: {result[9]}"


def test_generate_combinations_multiple_options():
    result = generate_combinations(["Option1", "Option2"])
    expected_header = ["TestCase ID", "Master Option For Option1", "Master Option For Option2", "Client Option For Option1", "Client Option For Option2"]
    assert result[0] == expected_header, f"Expected {expected_header}, but got {result[0]}"
    assert len(result) == 82, f"Expected 82 rows, but got {len(result)}"
    assert result[1] == [1, "TRUE", "TRUE", "TRUE", "TRUE"], f"Unexpected combination: {result[1]}"
    assert result[81] == [81, "NA", "NA", "NA", "NA"], f"Unexpected combination: {result[81]}"