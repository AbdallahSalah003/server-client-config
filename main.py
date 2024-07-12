import sys
import logging
from utils import validate_inputs, generate_combinations, generate_expected_values, is_valid_tc, csv_output
from error_handling import InvalidInput, InvalidLogic

options = sys.argv[1:]
while True:
    try:
        validate_inputs(options)
    except (InvalidLogic, InvalidInput) as e:
        print(str(e))
        options = input(f"Please provide valid options with space in between\n")
        if options == 'q':
            break
        options = options.split()
        continue
    except Exception as e:
        logging.exception(e)
    else:
        print("Valid inputs")
        combinations = generate_combinations(options)
        combinations_expected_values = generate_expected_values(combinations, options)
        result = is_valid_tc(combinations_expected_values, options)
        csv_output(result, "output.csv")
        break
