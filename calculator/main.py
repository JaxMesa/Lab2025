import logging
import uuid
import os
from datetime import datetime
from pythonjsonlogger.json import JsonFormatter
from functions import *

# Logger setup
logger = logging.getLogger("calculator")
logger.setLevel(logging.INFO)

# Directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(script_dir, "calculations.json")

# File handler with JsonFormatter
file_handler = logging.FileHandler(log_file)
json_formatter = JsonFormatter(
    fmt='%(timestamp)s %(level)s %(name)s %(message)s',
    reserved_attrs=['timestamp', 'level', 'name', 'message']
)
file_handler.setFormatter(json_formatter)
logger.addHandler(file_handler)

# Operations definition
operations_map = {
    1: ("+", lambda a, b: a + b),
    2: ("-", lambda a, b: a - b),
    3: ("*", lambda a, b: a * b),
    4: ("/", lambda a, b: a / b)
}

# Choice of an operation
while True:
    print("Please, choose an operation")
    operations = [ "1. Add", "2. Subtract", "3. Multiply", "4. Divide"]
    for i in operations:
        print(i)
    
    try:
        userChoice = int(input("Your choice: "))
        n1 = float(input("Choose first number: "))
        n2 = float(input("Choose second number: "))
        break
    except ValueError:
        print("Invalid")

Calculation(userChoice, operations_map, n1, n2, uuid, logger)