import sys
import logging
from utils import validate_inputs
from error_handling import InvalidInput, InvalidLogic

try:
    validate_inputs(sys.argv[1:])
except InvalidLogic as e:
    print(str(e))
except InvalidInput as e:
    print(str(e))
except Exception as e:
    logging.exception(e)
else:
    print("Valid inputs")
