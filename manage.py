#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pdfmerge.settings.local")
    settings=os.environ.get('DJANGO_SETTINGS_MODULE')
    if(settings is None):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.local")
    else:
	os.environ.setdefault("DJANGO_SETTINGS_MODULE",settings)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
    execute_from_command_line(sys.argv)
