#!/usr/bin/env python
import os
import sys
#change
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "classroom.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
