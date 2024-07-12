from utils import validate_inputs
from error_handling import InvalidLogic, InvalidInput


def test_valid_inputs():
    try:
        validate_inputs(["option1", "option2"])
    except Exception as e:
        assert False, f"validate_inputs() raised Exception unexpectedly: {e}"


def test_no_input_provided():
    try:
        validate_inputs([])
    except InvalidLogic as e:
        assert str(e) == "No server options provided"
    else:
        assert False, "Expected InvalidLogic exception"


def test_input_with_special_characters():
    try:
        validate_inputs(["validInput", "invalid@Input"])
    except InvalidInput as e:
        assert str(e) == "Special chars are not allowed"
    else:
        assert False, "Expected InvalidInput exception"


def test_duplicate_inputs():
    try:
        validate_inputs(["option1", "option1"])
    except InvalidLogic as e:
        assert str(e) == "Duplicate server options are not allowed"
    else:
        assert False, "Expected InvalidLogic exception"


def test_inputs_with_spaces():
    try:
        validate_inputs(["validInput", "invalid Input"])  # Space is considered a special char in this context
    except InvalidInput as e:
        assert str(e) == "Special chars are not allowed"
    else:
        assert False, "Expected InvalidInput exception"


def test_inputs_with_empty_string():
    try:
        validate_inputs(["", "option2"])
    except InvalidInput:
        pass
    except Exception as e:
        assert False, f"validate_inputs() raised Exception unexpectedly: {e}"
