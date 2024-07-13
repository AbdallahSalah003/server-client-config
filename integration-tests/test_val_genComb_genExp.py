import pytest
from utils import validate_inputs, generate_combinations, generate_expected_values


# Integration test cases for validate_inputs(), generate_combinations(), and generate_expected_values()

def test_validate_generate_combinations_expected_values():
    """Test the integration of validate_inputs, generate_combinations, and generate_expected_values functions."""
    valid_inputs = ['BufferData', 'TimeOut']

    try:
        validate_inputs(valid_inputs)
    except Exception as e:
        pytest.fail(f"validate_inputs raised an exception: {e}")

    combinations = generate_combinations(valid_inputs)

    expected_header = ["TestCase ID", "Master Option For BufferData", "Master Option For TimeOut",
                       "Client Option For BufferData", "Client Option For TimeOut"]
    assert combinations[0] == expected_header, "Header row does not match expected header"

    extended_combinations = generate_expected_values(combinations, valid_inputs)

    expected_extended_header = expected_header + ["Valid TC", "Expected BufferData", "Expected TimeOut"]
    assert extended_combinations[0] == expected_extended_header, "Extended header row does not match expected header"

    expected_combinations_length = 3 ** (2 * len(valid_inputs))
    assert len(extended_combinations) == expected_combinations_length + 1, "Number of extended combinations is incorrect"
