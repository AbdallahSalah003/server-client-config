import pytest
from utils import validate_inputs, generate_combinations


# Integration test cases for validate_inputs() and generate_combinations()

def test_validate_and_generate_combinations():
    """Test valid inputs for validate_inputs function and generate_combinations function."""
    valid_inputs = ['BufferData', 'TimeOut']
    try:
        validate_inputs(valid_inputs)
    except Exception as e:
        pytest.fail(f"validate_inputs raised an exception: {e}")

    result = generate_combinations(valid_inputs)

    expected_header = ["TestCase ID", "Master Option For BufferData", "Master Option For TimeOut",
                       "Client Option For BufferData", "Client Option For TimeOut"]
    assert result[0] == expected_header, "Header row does not match expected header"

    expected_combinations_length = 3 ** (2 * len(valid_inputs))
    assert len(result) == expected_combinations_length + 1, "Number of combinations is incorrect"
