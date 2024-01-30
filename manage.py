#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# first_name = "Richard"
# last_name = "Totolo"

# names = ["Richard", "Marta", "Mel"]
# print(names)

# # dictionary

# car = {
#   "brand" : "Ford",
#   "model" : "Mustang",
#   "year" : 1985
# }


# if "model" in car: print("Yes this is one of the keys in dictionary")
# else: print('nope')


# # user_name = first_name + " " + last_name
# # print(len(user_name))



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
