#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from datetime import date
from django.conf import settings


def main():
    """Run administrative tasks."""
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mserwer.settings')
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc
        
        # ZADANIE 1A
        port = settings.SERVER_PORT # pobranie portu z ustawień
        print("Autor: {}".format("Bartosz Kędziorek"))
        print("Port: {}".format(port))
        print("Data: {}".format(date.today()))
        execute_from_command_line(sys.argv)
    except Exception as e:
        file = open("error.txt", 'w')
        file.write(e)
        raise e


if __name__ == '__main__':
    main()
