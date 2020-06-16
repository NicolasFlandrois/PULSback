#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 16 June 2020 11:16:40
# Last Modified time: Tue 16 June 2020 12:05:01 

# Description:#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
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
