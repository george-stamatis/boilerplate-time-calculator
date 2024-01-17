# This entrypoint file to be used in development. Start by reading README.md
from unittest import main

from time_calculator import add_time

print(add_time("11:59 PM", "24:05", "Wednesday"))


# Run unit tests automatically
main(module='test_module', exit=False)