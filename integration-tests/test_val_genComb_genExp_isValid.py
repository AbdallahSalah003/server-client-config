import pytest
from utils import validate_inputs, generate_combinations, generate_expected_values, is_valid_tc


def test_validate_genComb_genExp_isValid():
    """Test the integrated flow of validate_inputs, generate_combinations, generate_expected_values, and is_valid_tc functions."""
    valid_inputs = ['BufferData']
    try:
        validate_inputs(valid_inputs)
    except Exception as e:
        pytest.fail(f"validate_inputs raised an exception: {e}")

    result = generate_combinations(valid_inputs)

    expected_header = ["TestCase ID", "Master Option For BufferData",
                       "Client Option For BufferData"]
    assert result[0] == expected_header, "Header row does not match expected header"

    expected_combinations_length = 3 ** (2 * len(valid_inputs))
    assert len(result) == expected_combinations_length + 1, "Number of combinations is incorrect"

    result = generate_expected_values(result, valid_inputs)

    expected_header_extended = expected_header + ["Valid TC", "Expected BufferData"]
    assert result[0] == expected_header_extended, "Extended header row does not match expected extended header"

    result = is_valid_tc(result, valid_inputs)
    expected_output_after_is_valid = [
        ["TestCase ID", "Master Option For BufferData", "Client Option For BufferData", "Valid TC",
         "Expected BufferData"],
        [1, "TRUE", "TRUE", "YES", "TRUE"],
        [2, "TRUE", "FALSE", "NO", "NA"],
        [3, "TRUE", "NA", "YES", "TRUE"],
        [4, "FALSE", "TRUE", "NO", "NA"],
        [5, "FALSE", "FALSE", "YES", "FALSE"],
        [6, "FALSE", "NA", "YES", "FALSE"],
        [7, "NA", "TRUE", "YES", "TRUE"],
        [8, "NA", "FALSE", "NO", "NA"],
        [9, "NA", "NA", "YES", "TRUE"]
    ]
    assert result == expected_output_after_is_valid, "Ouput from is_valid_tc() is not as expected"
